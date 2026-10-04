import os
import base64
import requests
import tempfile
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from google import genai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "Frontend")

# Load environment variables from Backend/.env, root .env, or system environment
load_dotenv(os.path.join(BASE_DIR, ".env"))
load_dotenv(os.path.join(os.path.dirname(BASE_DIR), ".env"))
load_dotenv()

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app)

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

PROMPTS = {
    "Summary": """
You are a professional tourist guide.
Provide a high-level overview of "{place}" in {language}.

Focus on:
- The historical significance
- Why the place is famous
- Key architectural or cultural highlights

Keep the explanation concise, engaging, and easy to follow.
Avoid excessive details and dates.
Limit the response to around 200 words.

Respond ONLY in {language}.
""",

    "Detailed": """
You are a professional tourist guide.
Provide a detailed and immersive explanation of "{place}" in {language}.

Cover:
- Historical background and timeline
- Architectural design and unique features
- Cultural importance and notable events
- Interesting facts and visitor insights

Explain concepts clearly and in a storytelling manner.
Include relevant details and examples to create a rich experience.
Limit the response to around 400 words.

Respond ONLY in {language}.
"""
}

def get_genai_client():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is not set. Please set GEMINI_API_KEY in environment variables.")
    return genai.Client(api_key=key)

def generate_speech(text, voice_id, locale):
    murf_key = os.getenv("MURF_API_KEY")
    if not murf_key:
        raise ValueError("MURF_API_KEY is not set. Please set MURF_API_KEY in environment variables.")

    temp_audio = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    )
   
    url = "https://global.api.murf.ai/v1/speech/stream"
    headers = {
        "api-key": murf_key,
        "Content-Type": "application/json"
    }
    data = {
        "voice_id": voice_id,
        "text": text,
        "locale": locale,
        "model": "FALCON",
        "format": "MP3",
        "sampleRate": 24000,
        "channelType": "MONO"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(temp_audio.name, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("Audio streaming completed")
    else:
        print(f"Error from Murf AI: {response.status_code} - {response.text}")
        raise RuntimeError(f"Murf API error ({response.status_code}): {response.text}")

    return temp_audio

def generate_description(place, answer_type, language):
    client = get_genai_client()
    prompt = PROMPTS[answer_type].format(place=place, language=language)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text

@app.route("/generate-audio-guide", methods=["POST"])
def generate_audio_guide():
    try:
        data = request.json or {}
        place = data.get("place")
        answer_type = data.get("answerType", "Summary")
        language = data.get("language", "English")
        voice_id = data.get("voiceId", "Matthew")
        locale = data.get("locale", "en-US")

        if not place:
            return jsonify({"error": "Place is required"}), 400

        text_description = generate_description(place, answer_type, language)
        audio_path = generate_speech(text_description, voice_id, locale)
        audio_bytes = open(audio_path.name, "rb").read()
        encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")

        return jsonify({
            "description": text_description,
            "audioBase64": encoded_audio
        })
    except Exception as e:
        print(f"Error in generate_audio_guide: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)