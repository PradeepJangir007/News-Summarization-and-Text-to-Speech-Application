from flask import Flask, request, jsonify, send_file
from main import NewsPipeline
from HindiTTS import Hinditts
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running! Use /analyze or /generate_audio"})


@app.route('/analyze', methods=['GET'])
def analyze():
    company_name = request.args.get('company', default='', type=str)
    if not company_name:
        return jsonify({"error": "Company name is required"}), 400

    pipeline = NewsPipeline(company_name)
    news_data = pipeline.run_pipeline()

    return jsonify(news_data)


@app.route('/generate_audio', methods=['GET'])
def get_audio():
    """Generates Hindi audio from the final sentiment analysis."""
    text = request.args.get('text', default='', type=str)
    if not text:
        return jsonify({"error": "Text is required"}), 400

    tts = Hinditts()
    audio = tts.generate_audio(text)
    del tts  # Free up memory

    return send_file(audio, mimetype="audio/mp3")


if __name__ == '__main__':
    app.run(debug=True)
