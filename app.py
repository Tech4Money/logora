import os
import io
import csv
import zipfile
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, send_file
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key')

# ---------- DATABASE SETUP ----------
DB_FILE = "users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT NOT NULL,
                  role TEXT,
                  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# ---------- STARTUP IDEA PROMPTS ----------
startup_prompts = [
    "Build an AI Resume Builder with ATS optimization and Stripe payments",
    "Create an AI Storybook Creator that turns prompts into illustrated books with PDF export",
    "Build a Doctor Appointment Scheduler with Twilio SMS + Retell AI calls",
    "Create a Smart Shop Platform with Shopify API + AI product descriptions",
    "Generate a Viral Waitlist SaaS with referral campaigns and email capture",
    "Build a Sales CRM SaaS with AI-powered lead scoring and outreach automation",
    "Create an Invoice Generator Pro with branded templates and tax compliance rules",
    "Build a Kanban Flow SaaS with AI task suggestions & automation",
    "Create a Project Management Lite app with AI task summaries",
    "Build an Expense & Finance Tracker with Plaid API + AI insights",
    "Create a Customer Segmentation Dashboard with clustering & visualization",
    "Build a Fintech Dashboard for real-time transaction analytics",
    "Create an Ergonomics Research Dashboard with IoT wearables API",
    "Build a Content Tracking Dashboard for digital asset usage",
    "Create a Legal AI contract analyzer with compliance flagging",
    "Build an AI Cognitive Insights Dashboard for reasoning pattern analysis",
    "Create a Mental Health Platform with journaling + AI chatbot",
    "Build a Women's Safety App with SOS alerts + GPS tracking",
    "Create a Pediatric Health Tracker with growth and vaccination logs",
    "Build an AI Nutrition Coach with meal tracking and balanced diet recommendations",
    "Create a Crypto Payment Gateway with fiat + crypto support",
    "Build a Car Parts Marketplace with inventory sync",
    "Create a Luxury Goods Marketplace with escrow & NFT provenance",
    "Build an AI Spreadsheet with formula auto-generation and automations",
    "Create an AI Animation Studio for drag-and-drop video creation with AI narration",
    "Build a Music Visualizer Studio synced with uploaded music",
    "Create an Interactive 3D Portfolio Builder with animated case studies",
    "Build a Metaware Logo Particles generator for brands",
    "Create an Event Gifting Platform with AI gift recommendations & logistics",
    "Build a Smart Resume Interview Coach with AI feedback on answers"
]

def save_user(email, role):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO users (email, role) VALUES (?, ?)", (email, role))
    conn.commit()
    conn.close()

# ---------- OPENAI CLIENT ----------
def get_openai_client():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return OpenAI(api_key=api_key)

# ---------- PLANNING + CODE GENERATION ----------
def hrm_plan(user_request):
    client = get_openai_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert architect. Break coding requests into 4–5 subtasks."},
            {"role": "user", "content": f"Break down this request:\n{user_request}"}
        ]
    )
    subtasks_text = response.choices[0].message.content.strip()
    subtasks = [line.lstrip("0123456789.-•) ").strip() for line in subtasks_text.splitlines() if line.strip()]
    return subtasks[:5]

def generate_code(subtask, user_request):
    client = get_openai_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert engineer. Output only valid code."},
            {"role": "user", "content": f"Original request: {user_request}\nSubtask: {subtask}\nGenerate code."}
        ]
    )
    return response.choices[0].message.content.strip()

# ---------- ROUTES ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    template_prompts = [
        "Build a SaaS landing page with signup and pricing",
        "Create a Flask API with JWT authentication",
        "Generate a Next.js app with Firebase auth and Stripe checkout",
        "Build a React dashboard with Tailwind and Chart.js",
        "Write a Python script to scrape a website and save results to CSV"
    ]

    if request.method == 'POST':
        user_request = request.form.get('user_request', '').strip()
        if not user_request:
            return render_template("index.html", error="Please enter a request", template_prompts=template_prompts, startup_prompts=startup_prompts)

        subtasks = hrm_plan(user_request)
        results = [{"subtask": st, "code": generate_code(st, user_request)} for st in subtasks]
        request.session_results = results
        request.session_request = user_request
        return render_template("index.html", user_request=user_request, results=results, template_prompts=template_prompts, startup_prompts=startup_prompts)

    return render_template("index.html", template_prompts=template_prompts, startup_prompts=startup_prompts)

@app.route('/download', methods=['POST'])
def download():
    email = request.form.get("email")
    role = request.form.get("role", "Unknown")

    if not email:
        return "Email is required to download.", 400

    # Save user info
    save_user(email, role)

    # Get session results
    user_request = getattr(request, "session_request", "AI Project")
    results = getattr(request, "session_results", [])

    # Create ZIP in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        zf.writestr("README.md", f"# Generated Project\n\nRequest: {user_request}\n\nCreated with Logora AI")
        for idx, res in enumerate(results, 1):
            filename = f"subtask_{idx}.py"
            zf.writestr(filename, res["code"])
    zip_buffer.seek(0)

    return send_file(zip_buffer, as_attachment=True, download_name="logora_project.zip", mimetype="application/zip")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
