# 🤖 Logora - AI Reasoning-First Coding Agent

An intelligent Flask web application that uses OpenAI's GPT-4o-mini to break down coding requests into logical subtasks and generates production-ready code for each. Features a modern glassmorphism UI, dark mode toggle, comprehensive startup prompt library with 242+ curated ideas, and project download capability.

[![Deploy on Replit](https://replit.com/badge/github/yourusername/logora)](https://replit.com/@yourusername/logora)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/logora)
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yourusername/logora)

## ✨ Features

- 🧠 **Intelligent Task Decomposition** - Breaks complex requests into 4-5 actionable subtasks
- 💻 **AI-Powered Code Generation** - Uses GPT-4o-mini for high-quality code output
- 🎨 **Modern Glassmorphism UI** - Beautiful glass morphism design with gradient effects
- 🌙 **Dark Mode Toggle** - Seamless theme switching with localStorage persistence
- 📚 **242+ Startup Prompts** - Categorized library of curated project ideas:
  - 🚀 Startup Idea Starters (30 prompts)
  - 🤖 AI & SaaS Projects (42 prompts)
  - 🛒 E-Commerce & Marketplaces (100 prompts)
  - 🎨 AI Creative & Media (70 prompts)
- 📦 **Project Download** - Export generated code as ZIP files
- 💾 **User Tracking** - SQLite database for email and role tracking
- ⚡ **Production Ready** - Deployable to Vercel, Replit, Heroku, and Bolt.new

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/logora.git
   cd logora
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 🔧 Environment Variables

Create a `.env` file in the project root:

```bash
# Required: Your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Session secret (defaults to 'dev-secret-key')
SESSION_SECRET=your_secret_key_here
```

## 📦 Deployment

### Deploy to Replit

1. Click the "Run on Replit" button above
2. Add your `OPENAI_API_KEY` to Secrets (🔒 icon)
3. Click "Run" - that's it!

### Deploy to Vercel

1. Click the "Deploy with Vercel" button above
2. Add `OPENAI_API_KEY` environment variable in Vercel dashboard
3. Deploy - your app will be live in seconds!

### Deploy to Heroku

1. Click the "Deploy to Heroku" button above
2. Set `OPENAI_API_KEY` config var in Heroku dashboard
3. The app will automatically use the Procfile for deployment

### Deploy to Bolt.new

1. Copy the entire project to Bolt.new
2. Add `OPENAI_API_KEY` to environment variables
3. Bolt.new will handle the rest automatically

## 🎯 How It Works

1. **Enter Your Request** - Type a coding request or click a starter prompt
2. **AI Planning Phase** - Logora uses GPT-4o-mini to decompose the request into 4-5 subtasks
3. **Code Generation** - Each subtask is processed to generate relevant, production-ready code
4. **View & Download** - See formatted results with syntax highlighting, download as ZIP

## 🛠️ Tech Stack

### Backend
- **Flask** - Lightweight Python web framework
- **OpenAI API** - GPT-4o-mini for intelligent code generation
- **SQLite** - User tracking database
- **python-dotenv** - Environment variable management

### Frontend
- **Jinja2 Templates** - Server-side rendering
- **Tailwind CSS** - Utility-first styling (via CDN)
- **CSS Variables** - Dynamic dark/light mode theming
- **Vanilla JavaScript** - Dark mode toggle with localStorage

### Deployment
- **Gunicorn** - Production WSGI server
- **Vercel** - Serverless deployment support
- **Heroku** - Container-based deployment
- **Replit** - Instant cloud IDE deployment

## 📂 Project Structure

```
logora/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html         # Main UI template with glassmorphism design
├── static/
│   └── styles.css         # Additional CSS styles
├── users.db               # SQLite database (auto-created)
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── vercel.json           # Vercel deployment config
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🎨 UI Features

- **Glassmorphism Cards** - Frosted glass effect with backdrop blur
- **Gradient Hero Text** - Silver-to-blue gradient headline
- **Grid Background** - Subtle grid pattern for depth
- **Responsive Layout** - Mobile-first design with 2-column grid
- **Click-to-Fill Prompts** - Interactive starter prompt cards
- **Loading States** - Visual feedback during AI processing
- **Expandable Code Blocks** - Collapsible sections for generated code

## 🔒 Security Notes

- Never commit your `.env` file or expose API keys
- The `.env.example` is provided as a template only
- Use environment variables for all sensitive data
- The app validates API key presence before processing requests

## 📝 API Key Setup

### Get Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign in or create an account
3. Navigate to API Keys section
4. Create a new secret key
5. Copy and paste into your `.env` file

### Friendly Error Handling

If you forget to add your API key, Logora will display a helpful message:

> ⚠️ OpenAI API key is missing. Please add your OPENAI_API_KEY to the .env file to use Logora.

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Add more startup prompts to the library
- Improve the UI/UX design
- Add new AI models or features
- Fix bugs and improve performance

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🙏 Credits

Built with ❤️ using Flask, OpenAI GPT-4o-mini, and modern web technologies.

---

**Happy Coding! 🚀**
