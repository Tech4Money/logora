import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key')

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def hrm_plan(user_request):
    """
    Breaks down a user request into logical subtasks for code generation.
    This is a simple implementation that returns 4-5 subtasks.
    """
    subtasks = [
        f"Set up the basic project structure and dependencies for: {user_request}",
        f"Implement the core functionality and main logic for: {user_request}",
        f"Add error handling and input validation for: {user_request}",
        f"Create helper functions and utilities for: {user_request}",
        f"Add documentation and usage examples for: {user_request}"
    ]
    return subtasks

def generate_code(subtask, user_request):
    """
    Uses OpenAI API to generate code for a specific subtask.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer. Generate clean, well-commented code based on the user's request. Only output the code, no explanations unless asked."
                },
                {
                    "role": "user",
                    "content": f"Original request: {user_request}\n\nSubtask: {subtask}\n\nGenerate the code for this subtask."
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        code = response.choices[0].message.content
        return code
    except Exception as e:
        return f"Error generating code: {str(e)}"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_request = request.form.get('user_request', '').strip()
    
    if not user_request:
        return render_template('index.html', error="Please enter a request")
    
    # Generate subtasks
    subtasks = hrm_plan(user_request)
    
    # Generate code for each subtask
    results = []
    for subtask in subtasks:
        code = generate_code(subtask, user_request)
        results.append({
            'subtask': subtask,
            'code': code
        })
    
    return render_template('index.html', 
                         user_request=user_request, 
                         results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
