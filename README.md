# News Summarization and Text-to-Speech Application

## Objective
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool allows users to input a company name and receive a structured sentiment report along with an audio output.

## Features
1. **News Extraction**: Extract and display the title, summary, and relevant metadata from at least 10 unique news articles using BeautifulSoup (bs4).
2. **Sentiment Analysis**: Classify the article content as positive, negative, or neutral using `mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis`.
3. **Comparative Analysis**: Compare sentiment across the 10 articles to understand how the company's news coverage varies.
4. **Text-to-Speech (TTS)**: Convert the summarized content into Hindi speech using the `Helsinki-NLP/opus-mt-en-hi` model for translation and `gTTS` for speech synthesis.
5. **Topic Analysis**: Extract key topics using `KeyBERT`.
6. **User Interface**: A web-based interface using Streamlit.
7. **API Development**: Communication between frontend and backend via Flask APIs.
8. **Deployment**: Hosted on Hugging Face Spaces for accessibility.

## Installation & Setup
### Prerequisites
Ensure you have Python 3.8+ installed and the following dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the API server:
   ```bash
   python api.py
   ```
4. Run the Streamlit UI:
   ```bash
   streamlit run ui.py
   ```

## Project Structure
```
├── api.py                 # Flask API server
├── main.py                # News processing pipeline
├── HindiTTS.py            # Hindi text-to-speech module
├── sentiment_analyzer.py   # Sentiment analysis module
├── summarization.py       # Summarization using TinyLlama
├── Topic_Analysis.py      # Topic extraction using KeyBERT
├── ui.py                  # Streamlit frontend
├── utils.py               # News fetching module
├── requirements.txt       # Required dependencies
├── README.md              # Documentation
```

## API Usage
- **GET /analyze?company=CompanyName**: Fetches and analyzes news for the given company.
- **GET /generate_audio?text=Text**: Generates Hindi audio from the input text.

## Expected Output
### Input:
```
Company Name: Tesla
```
### Output:
```json
{
    "Company": "Tesla",
    "Articles": [
        {
            "Title": "Tesla's New Model Breaks Sales Records",
            "Summary": "Tesla's latest EV sees record sales in Q3...",
            "Sentiment": "Positive",
            "Topics": ["Electric Vehicles", "Stock Market", "Innovation"]
        }
    ],
    "Comparative Sentiment Score": {
        "Sentiment Distribution": {"Positive": 1, "Negative": 0, "Neutral": 0}
    },
    "Final Sentiment Analysis": "Tesla’s latest news coverage is mostly positive. Potential stock growth expected.",
    "Audio": "[Play Hindi Speech]"
}
```

## Deployment
The application is deployed on Hugging Face Spaces. Access the live version here: **[Deployment Link](#)**

## Assumptions & Limitations
- Only TIME OF INDIA news websites is supported for web scraping.
- Sentiment analysis is based on textual content and may not always be 100% accurate.
- TTS output may vary in quality based on the open-source model used.

---
### Author: Pradeep Jangir
