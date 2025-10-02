# 🤖 Logora - AI Reasoning-First Coding Agent

An intelligent Flask web application that uses **OpenAI’s GPT-4o-mini** to break down coding requests into logical subtasks and generate **production-ready code** for each.
Logora features a **modern glassmorphism UI**, **dark mode toggle**, and a **comprehensive startup prompt library with 240+ curated project ideas**, plus one-click deployment to **Replit, Vercel, Heroku, and Bolt.new**.

[![Deploy on Replit](https://replit.com/badge/github/yourusername/logora)](https://replit.com/@yourusername/logora)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/logora)
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yourusername/logora)

---

## ✨ Features

* 🧠 **Intelligent Task Decomposition** – Breaks complex requests into clear subtasks
* 💻 **AI-Powered Code Generation** – Uses GPT-4o-mini for high-quality code
* 🎨 **Modern Glassmorphism UI** – Gradient cards, frosted glass styling
* 🌙 **Dark Mode Toggle** – LocalStorage persistence, smooth switching
* 📚 **242+ Startup Prompts** organized into categories:

  * 🚀 Startup Idea Starters (30)
  * 🤖 AI & SaaS Projects (42)
  * 🛒 E-Commerce & Marketplaces (100)
  * 🎨 AI Creative & Media (70)
* 📦 **Project Export** – Download generated code as a ZIP
* 💾 **User Tracking** – SQLite database for emails & roles
* ⚡ **Deploy Anywhere** – Ready for Replit, Vercel, Heroku, Bolt

---

## 🚀 Quick Start

### Local Development

```bash
# Clone repo
git clone https://github.com/yourusername/logora.git
cd logora

# Install dependencies
pip install -r requirements.txt

# Copy env vars
cp .env.example .env
# Add your OPENAI_API_KEY in .env

# Run the app
python app.py

# Open in browser
http://localhost:5000
```

---

## 🔧 Environment Variables

`.env` file in project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
SESSION_SECRET=your_secret_key_here   # optional
```

---

## 📦 Deployment

### Deploy to Replit

* Click **Run on Replit** badge
* Add your `OPENAI_API_KEY` in 🔒 Secrets
* Hit **Run**

### Deploy to Vercel

* Click **Deploy with Vercel** badge
* Add `OPENAI_API_KEY` in Environment Variables
* Deploy 🚀

### Deploy to Heroku

* Click **Deploy to Heroku** badge
* Add `OPENAI_API_KEY` config var
* App boots automatically

### Deploy to Bolt.new

* Copy repo to Bolt.new
* Add `OPENAI_API_KEY` in environment
* Done ✅

---

## 🎯 How It Works

1. Enter a coding request (or click a starter prompt)
2. Logora decomposes it into subtasks
3. GPT-4o-mini generates production-ready code per step
4. Code is displayed + downloadable as ZIP

---

## 🛠️ Tech Stack

**Backend:** Flask, OpenAI API, SQLite, dotenv
**Frontend:** Tailwind CSS, Jinja2, Vanilla JS (dark mode toggle)
**Deployment:** Replit, Vercel, Heroku, Gunicorn

---

## 📂 Project Structure

```
logora/
├── app.py             # Main Flask app
├── templates/         # HTML templates (UI)
├── static/            # CSS & assets
├── users.db           # SQLite database
├── requirements.txt   # Python deps
├── Procfile           # Heroku config
├── vercel.json        # Vercel config
├── .env.example       # Environment example
└── README.md          # This file
```

---

## 🎨 UI Features

* Glassmorphism cards with backdrop blur
* Gradient hero headline text
* Grid pattern background
* Responsive design (mobile-ready)
* Collapsible code blocks
* Smooth animations & hover states

---

## 🔒 Security

* `.env` never committed
* Keys loaded via environment vars
* Friendly error message if `OPENAI_API_KEY` is missing

---

## 🤝 Contributing

We welcome contributions:

* Add new startup prompts
* Improve UI/UX
* Add AI models/features
* Fix bugs

---

## 📄 License

MIT License – Free for personal & commercial use.

---

## 🙏 Credits

Built with ❤️ using Flask, GPT-4o-mini, Tailwind, and modern web tech.

---

**Happy Coding! 🚀**
