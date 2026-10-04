# 🌍 AI Travel Guide

An interactive AI-powered travel guide web application that provides rich destination overviews, detailed cultural stories, and high-quality voice audio narrations in multiple languages using **Gemini** and **Murf AI**.

---

## ✨ Features

- **Dynamic Overview & Detailed Stories**: Generates structured summaries or detailed narrative histories for global landmarks using **Google Gemini 3.1 Flash Lite**.
- **Multilingual Audio Guides**: Generates audio guides in multiple languages (English, Hindi, Tamil, Telugu) with gender-specific voices powered by **Murf AI**.
- **Interactive UI**: Clean, responsive travel explorer interface built with Tailwind CSS, supporting interactive card browsing and search previews.
- **Audio Streaming & Playback**: Real-time synthesized speech encoded and streamed directly to the browser player.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS
- **Backend**: Python 3, Flask, Flask-CORS, python-dotenv
- **AI & Speech APIs**: Google GenAI SDK (`google-genai`), Murf AI API

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10+
- A Google Gemini API key
- A Murf AI API key

### 2. Environment Configuration

Navigate to the `Backend` directory and configure your `.env` file:

```bash
cd Backend
cp .env.example .env
```

Add your API keys to `Backend/.env`:

```env
MURF_API_KEY=your_murf_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Installation

Create and activate a virtual environment, then install dependencies:

```bash
cd Backend
python -m venv .venv

# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 4. Running the Application

**Start the Backend server:**
```bash
cd Backend
python app.py
```
The Flask backend runs at `http://127.0.0.1:5000`.

**Start the Frontend server:**
```bash
cd Frontend
python -m http.server 8000
```
Open [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

---

## 📁 Project Structure

```
AI_Travel_Guide/
├── Backend/
│   ├── app.py               # Flask application & API routes
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Example environment variables template
│   └── .env                 # Secret API keys (ignored in git)
├── Frontend/
│   ├── index.html           # Main user interface
│   └── index.js             # UI state, event handling & API integration
├── .gitignore               # Ignored files (secrets, venvs, cache)
└── README.md                # Project documentation
```
