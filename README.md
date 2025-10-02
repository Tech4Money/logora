# Logora - AI Reasoning-First Coding Agent

An intelligent Flask web application that breaks down coding requests into logical subtasks and generates code for each using OpenAI's GPT-4.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key

Create a `.env` file in the project root and add your OpenAI API key:

```bash
OPENAI_API_KEY=your-actual-openai-api-key-here
```

You can copy the `.env.example` file as a template:

```bash
cp .env.example .env
```

Then edit the `.env` file with your actual API key.

### 3. Run the Application

```bash
python app.py
```

### 4. Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

## How It Works

1. **Enter Your Request**: Type your coding request in the textarea (e.g., "Create a Python function to sort a list")
2. **AI Planning**: The app breaks down your request into 4-5 logical subtasks
3. **Code Generation**: For each subtask, the app uses OpenAI GPT-4 to generate relevant code
4. **View Results**: See all subtasks with their generated code displayed in clean, formatted blocks

## Features

- 🧠 Intelligent task decomposition
- 💻 AI-powered code generation using GPT-4
- 🎨 Modern, responsive UI with clean styling
- 🌙 Dark-themed code display for better readability
- ⚡ Fast and simple to use

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection

## Technologies Used

- **Flask** - Web framework
- **OpenAI API** - Code generation (GPT-4o-mini)
- **python-dotenv** - Environment variable management
