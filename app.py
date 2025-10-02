import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key')

def get_openai_client():
    """Initialize OpenAI client with error handling."""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return OpenAI(api_key=api_key)

def hrm_plan(user_request):
    """
    Uses AI to break down a user request into 4-5 logical subtasks for code generation.
    This provides intelligent, context-aware task decomposition.
    """
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software architect. Break down coding requests into 4-5 logical, specific subtasks. Each subtask should be a clear, actionable step. Return only the subtasks as a numbered list, nothing else."
                },
                {
                    "role": "user",
                    "content": f"Break down this coding request into 4-5 specific subtasks:\n\n{user_request}"
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        subtasks_text = response.choices[0].message.content or ""
        subtasks_text = subtasks_text.strip()
        subtasks = []
        
        for line in subtasks_text.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
                subtask = line.lstrip('0123456789.-•) ').strip()
                if subtask:
                    subtasks.append(subtask)
        
        if len(subtasks) < 3:
            subtasks = [
                f"Set up the basic project structure and dependencies for: {user_request}",
                f"Implement the core functionality and main logic for: {user_request}",
                f"Add error handling and input validation for: {user_request}",
                f"Create helper functions and utilities for: {user_request}"
            ]
        
        return subtasks[:5]
        
    except Exception as e:
        print(f"Error in hrm_plan: {str(e)}")
        return [
            f"Set up the basic project structure for: {user_request}",
            f"Implement the core functionality for: {user_request}",
            f"Add error handling for: {user_request}",
            f"Add documentation for: {user_request}"
        ]

def generate_code(subtask, user_request):
    """
    Uses OpenAI API to generate code for a specific subtask with comprehensive error handling.
    """
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer. Generate clean, well-commented code based on the user's request. Only output the code, no explanations unless asked. Include proper error handling and follow best practices."
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
    except ValueError as e:
        print(f"Configuration error: {str(e)}")
        return f"# Configuration Error: {str(e)}\n# Please ensure OPENAI_API_KEY is set in your environment variables."
    except Exception as e:
        print(f"Error generating code: {str(e)}")
        return f"# Error generating code: {str(e)}\n# Please check your API key and internet connection."

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
