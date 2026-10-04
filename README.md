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

### 4. Running the Application Locally

```bash
cd Backend
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) directly in your browser. The unified server serves both the interactive frontend and the audio guide API.

---

## ☁️ Deployment (Render)

This repository includes a `render.yaml` Blueprint for one-click setup on Render.

1. Go to **[dashboard.render.com](https://dashboard.render.com)**.
2. Click **New +** → **Web Service** (or **Blueprint**).
3. Connect your GitHub repository: `Sharan126/AI_Travel_Guide`.
4. Configure the settings:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r Backend/requirements.txt`
   - **Start Command**: `gunicorn --chdir Backend app:app`
5. Under **Environment Variables**, add:
   - `MURF_API_KEY`: *(Your Murf AI API key)*
   - `GEMINI_API_KEY`: *(Your Gemini API key)*
6. Click **Deploy Web Service**.

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
