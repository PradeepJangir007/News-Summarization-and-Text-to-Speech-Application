# News Summarization and Text-to-Speech Application

## Objective
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool allows users to input a company name and receive a structured sentiment report along with an audio output.

## Features
1. **News Extraction**: Extract and display the title, summary, and relevant metadata from news articles using BeautifulSoup (bs4).
2. **Sentiment Analysis**: Classify the article content as positive, negative, or neutral using `mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis`.
3. **Comparative Analysis**: Compare sentiment across the articles to understand how the company's news coverage varies using `TinyLlama/TinyLlama-1.1B-Chat-v1.0`.
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
    "Audio": "/tmp/audio/Tesla_summary.mp3",
    "Company": "Tesla",
    "Comparative Sentiment Score": {
        "Coverage Differences": [
            {
                "Comparison": "Both articles focus on safety concerns related to tesla and its CEO, Elon Musk. However, Article 1 emphasizes the potential security risks while Article 2 highlights the selfish reasons for removing tesla from the auto show.",
                "Impact": "Both articles have a significant impact on public perception, with Article 1 being more influential due to its focus on safety concerns and Article 2 being more influential due to its focus on selfish reasons."
            },
            {
                "Comparison": "Both articles highlight the use of external cameras and sensors to monitor surroundings when parked, but Tesla's Sentry Mode feature is more effective against criminals. The system records suspicious activity, alerts owners in real-time, and stores footage locally. Kim Kardashian's photoshoot with tesla products sparked controversies surrounding Elon Musk and tesla's business practices. The provocative images sparked criticism over the timing and potential insensitivity, given allegations of poor labor conditions and Musk's political stances.",
                "Impact": "The impact of both articles is to influence public perception by highlighting the effectiveness of Tesla's Sentry Mode feature against criminals, while also highlighting the controversies surrounding Elon Musk and tesla's business practices."
            },
            {
                "Comparison": "Both articles focus on the impact of protests and criticism on tesla executives, but Article 5 provides more detail on the frustration and anger towards the company.",
                "Impact": "Article 5 has a greater impact on public perception, as it provides more specific examples of the frustration and anger towards tesla."
            },
            {
                "Comparison": "President Donald Trump suggested that arson attacks on tesla cars were acts of 'domestic political terrorism' by left-wing operatives. Recent incidents include vandalism, shootings, and arson at tesla dealerships across multiple states. Trump claimed that perpetrators are linked to highly political groups and praised tesla CEO Elon Musk as a 'patriot.'",
                "Impact": "This article has a significant impact on public perception, as it highlights the potential for political influence and violence in the electric vehicle industry. The article's focus on left-wing operatives and the potential for political violence could impact consumer trust and long-term sales."
            },
            {
                "Comparison": "Both articles focus on Elon Musk's Department of Government Efficiency, but the impact is different. Article 9 focuses on Musk's commitment to saving federal money, while Article 10 focuses on protests and vandalism due to his role in the Department of Government Efficiency.",
                "Impact": "Article 9 is more focused on the impact of Musk's Department of Government Efficiency on federal money, while Article 10 is more focused on the impact of Musk's role in the Department of Government Efficiency on protests and vandalism."
            },
            {
                "Comparison": "Both articles focus on the impact of Elon Musk's political involvement on Tesla's sales and public perception. However, Article 11 provides more detailed information on the targeting of Tesla vehicles and showrooms, while Article 12 provides more information on the attacks on Tesla in the US.",
                "Impact": "Article 11 highlights the targeting of Tesla vehicles and showrooms, while Article 12 provides more information on the attacks on Tesla in the US. This impacts public perception by highlighting the potential for violence and disruption in the Tesla community."
            },
            {
                "Comparison": "Musk's position as the top shareholder in Tesla has been revealed, while Trump's purchase of a Model S has been reported. This highlights the importance of Musk's leadership in Tesla's growth and the potential impact of his actions on the company's stock price.",
                "Impact": "Musk's leadership has been a significant factor in Tesla's growth, and his purchase of a Model S has been a significant factor in its stock price. Trump's purchase of a Model S has been a potential negative factor in Tesla's stock price."
            },
            {
                "Comparison": "Both articles focus on the impact of tesla's falling stock price on the company's reputation and investors' confidence.",
                "Impact": "Both articles have a significant impact on public perception, with RBC Capital Markets' downgrade and the arrest of an individual for keying a tesla at a Costco car park being particularly noteworthy."
            },
            {
                "Comparison": "Chinese customers who once flocked to tesla are turning more and more to local brands that offer more efficient cars with better technology, sometimes at half the price.",
                "Impact": "This article has a significant impact on public perception, as it suggests that Chinese customers are shifting their focus towards local brands that offer more efficient cars with better technology. This shift is likely to have a positive impact on the local automotive industry, as it will lead to increased demand for local brands and potentially lower prices for consumers."
            },
            {
                "Comparison": "Both articles focus on the potential fallout from President Trump's trade war on the US electric vehicle industry. Article 19 suggests retaliatory tariffs could harm American businesses, while Article 20 urges caution to avoid negative impacts on American businesses and recommends a phased implementation approach for any new trade measures.",
                "Impact": "Article 19 influences public perception by highlighting the potential negative impacts of the trade war on American businesses, while Article 20 suggests a phased implementation approach to avoid negative impacts."
            }
        ],
        "Sentiment Distribution": {
            "Negative": 11,
            "Neutral": 9,
            "Positive": 0
        },
        "Topic Overlap": {
            "Common Topics": [
                "elon musk",
                "tesla stock",
                "bought tesla",
                "protests",
                "tesla"
            ],
            "unique_topics in Article 1": [
                "tesla dealerships",
                "targeted tesla",
                "removed vancouver",
                "tesla removed"
            ],
            "unique_topics in Article 10": [
                "organized protests",
                "facing protests",
                "protests vandalism",
                "protest"
            ],
            "unique_topics in Article 11": [
                "protest movement",
                "takedown protest",
                "tesla vehicles",
                "urges tesla",
                "tesla takedown"
            ],
            "unique_topics in Article 12": [
                "musk behavior",
                "tesla faces",
                "musk defense"
            ],
            "unique_topics in Article 13": [
                "support vandalism",
                "targeting tesla",
                "violence tesla",
                "vandalism targeting"
            ],
            "unique_topics in Article 14": [
                "shareholder tesla",
                "musk electric"
            ],
            "unique_topics in Article 15": [
                "tesla falling",
                "cut tesla",
                "stock dropped",
                "tesla price"
            ],
            "unique_topics in Article 16": [
                "keying tesla",
                "arrested keying",
                "tesla costco",
                "jose police"
            ],
            "unique_topics in Article 17": [],
            "unique_topics in Article 18": [
                "tesla turning",
                "local brands",
                "chinese customers",
                "efficient cars"
            ],
            "unique_topics in Article 19": [],
            "unique_topics in Article 2": [
                "violent crockett",
                "accused destroying",
                "destroying tesla"
            ],
            "unique_topics in Article 20": [
                "tariffs harm",
                "retaliatory tariffs",
                "tesla warns",
                "tariffs"
            ],
            "unique_topics in Article 3": [
                "sensors monitor",
                "cameras",
                "cameras sensors",
                "sentry mode",
                "tesla highlighted"
            ],
            "unique_topics in Article 4": [
                "kardashian promoting",
                "photoshoot tesla",
                "accused kardashian",
                "kardashian faced",
                "kim kardashian"
            ],
            "unique_topics in Article 5": [
                "tesla executives",
                "remarks tesla"
            ],
            "unique_topics in Article 6": [
                "tesla violence",
                "tesla attacks",
                "details tesla",
                "tesla owners",
                "anti tesla"
            ],
            "unique_topics in Article 7": [
                "arson tesla",
                "tesla ceo",
                "attacks tesla",
                "tesla cars"
            ],
            "unique_topics in Article 8": [
                "uk tesla",
                "protests uk",
                "tesla market",
                "protests impact"
            ],
            "unique_topics in Article 9": [
                "tesla shares",
                "buy tesla",
                "money tesla"
            ]
        }
    },
    "Final Sentiment Analysis": " Summarize in one line whether the overall news coverage is positive, neutral, or negative",
    "articles": [
        {
            "Topics": [
                "tesla removed",
                "targeted tesla",
                "tesla",
                "tesla dealerships",
                "removed vancouver"
            ],
            "sentiment": "negative",
            "summary": " tesla has been removed from the Vancouver International Auto Show due to safety concerns stemming from ongoing protests against the company and its CEO, Elon Musk. The decision came after activists targeted tesla dealerships and promoted boycotts, raising potential security risks. Organizers emphasized the move aimed at ensuring a safe environment for all participants. ",
            "title": " tesla removed from Vancouver International Auto Show over safety concerns amid protests against Elon Musk "
        },
        {
            "Topics": [
                "destroying tesla",
                "elon musk",
                "tesla",
                "violent crockett",
                "accused destroying"
            ],
            "sentiment": "neutral",
            "summary": " \u201cI am truly here for very selfish reasons, starting with on March 29 it\u2019s my birthday and all I want to see happen on my birthday is for Elon to be taken down,\" Crockett said adding that whatever she is promoting is non-violent. Crockett's call for 'taking down' Elon Musk came as Attorney General Pam Bondi announced that three people accused of destroying tesla cars and charging stations are facing 20 years in reason for 'domestic terrorism'. ",
            "title": " Jasmine Crockett wants 'Elon Musk to be taken down' as her birthday present amid violence against tesla "
        },
        {
            "Topics": [
                "sentry mode",
                "tesla highlighted",
                "sensors monitor",
                "cameras",
                "cameras sensors"
            ],
            "sentiment": "neutral",
            "summary": " tesla highlighted its Sentry Mode feature, which uses external cameras and sensors to monitor surroundings when parked. The system records suspicious activity, alerts owners in real-time, and stores footage locally. Blinkit acknowledged the technology, and Elon Musk emphasized its effectiveness against criminals. ",
            "title": " tesla says: 'Smile, you\u2019re on camera' after the addition of new feature; India's Blinkit responds "
        },
        {
            "Topics": [
                "kardashian faced",
                "accused kardashian",
                "kardashian promoting",
                "photoshoot tesla",
                "kim kardashian"
            ],
            "sentiment": "negative",
            "summary": " Kim Kardashian faced backlash following her photoshoot with tesla products, amid controversies surrounding Elon Musk and tesla's business practices. The provocative images sparked criticism over the timing and potential insensitivity, given allegations of poor labor conditions and Musk's political stances. Fans accused Kardashian of promoting tesla for financial gain despite the company's current issues. ",
            "title": " Watch | Kim Kardashian poses intimately with tesla robot\u2014and the internet isn\u2019t happy "
        },
        {
            "Topics": [
                "tesla executives",
                "remarks tesla",
                "tesla",
                "tesla stock",
                "elon musk"
            ],
            "sentiment": "negative",
            "summary": " tesla executives, including engineer Dhaval Shroff, have expressed frustration over protests and criticism towards the company. Shroff responded sharply to former vice presidential candidate Tim Walz\u2019s mocking remarks about tesla's stock decline. Elon Musk also chimed in, referencing Vice President JD Vance in response to Walz's statements. ",
            "title": " tesla Autopilot AI engineer Dhaval Shroff's Angry post for Tim Walz on his 'tesla joke' gets CEO Elon Musk's reply "
        },
        {
            "Topics": [
                "tesla attacks",
                "tesla violence",
                "details tesla",
                "tesla owners",
                "anti tesla"
            ],
            "sentiment": "neutral",
            "summary": " Dogequest has published personal details of tesla owners in the US, prompting Elon Musk to denounce it as 'Extreme Domestic Terrorism.' The website demands proof of vehicle sale for data removal. This follows anti-tesla violence linked to Musk's role in Trump's administration. FBI is investigating recent tesla attacks, including arson and shootings. ",
            "title": " Extreme Domestic Terrorism ..., says Elon Musk as website publishes Names, Addresses, and Phone Numbers of tesla owners across America in an interactive map "
        },
        {
            "Topics": [
                "arson tesla",
                "attacks tesla",
                "tesla ceo",
                "tesla cars",
                "tesla"
            ],
            "sentiment": "neutral",
            "summary": " President Donald Trump suggested that arson attacks on tesla cars were acts of 'domestic political terrorism' by left-wing operatives. Recent incidents include vandalism, shootings, and arson at tesla dealerships across multiple states. Trump claimed that perpetrators are linked to highly political groups and praised tesla CEO Elon Musk as a 'patriot.' ",
            "title": " Attacks on tesla 'domestic terrorism' paid by 'highly political on the left', says Donald Trump "
        },
        {
            "Topics": [
                "protests uk",
                "protests impact",
                "protests",
                "uk tesla",
                "tesla market"
            ],
            "sentiment": "neutral",
            "summary": " Protests in the UK against tesla and Elon Musk have intensified, with groups like 'tesla Takedown UK' and 'Everybody Hates Elon' campaigning against Musk's political influence. Despite Musk's dismissive response and tesla\u2019s continued market dominance, the protests could impact consumer trust and long-term sales. The UK accounts for 4.6% of tesla\u2019s market. ",
            "title": " \"Honk If You Hate Elon\": Who is leading the anti-Elon Musk protests against tesla in London "
        },
        {
            "Topics": [
                "buy tesla",
                "bought tesla",
                "tesla shares",
                "money tesla",
                "tesla"
            ],
            "sentiment": "negative",
            "summary": " As the head of the Department of Government Efficiency, Elon Musk ran his chainsaw through government departments to cut them into halves in his commitment to save federal money. tesla shares experienced a massive fall as Donald Trump promised to buy a tesla car and bought tesla S model for White House staff as a gesture of support for Elon. Musk said tesla would double the production in the US over the next two years. ",
            "title": " 'Never physically hurt anyone': Elon Musk reacts to tesla coming under attack "
        },
        {
            "Topics": [
                "facing protests",
                "protests",
                "protests vandalism",
                "organized protests",
                "protest"
            ],
            "sentiment": "neutral",
            "summary": " tesla facilities and vehicles in the US are facing protests and vandalism due to CEO Elon Musk's role in the Department of Government Efficiency. Some protests have led to arson at showrooms and charging stations. Jackron claimed to have infiltrated a protest, revealing Democrat-funded Facebook-organized protests. President Trump warned perpetrators, promising strict action. ",
            "title": " A 'mechanical engineer' on Twitter claims 'Facebook link' in tesla protests, Elon Musk responds "
        },
        {
            "Topics": [
                "tesla takedown",
                "takedown protest",
                "urges tesla",
                "tesla vehicles",
                "protest movement"
            ],
            "sentiment": "negative",
            "summary": " tesla vehicles and showrooms have been targets of violent attacks and vandalism due to discontent towards Elon Musk's political involvement. The \"tesla Takedown\" protest movement, originating on BlueSky, urges tesla owners to sell their vehicles to counter Musk's influence. Some owners use bumper stickers to distance themselves from Musk. ",
            "title": " Elon Musk's tesla faces severe backlash: Owners paste quirky stickers to save themselves from vandalism "
        },
        {
            "Topics": [
                "tesla",
                "tesla faces",
                "musk behavior",
                "musk defense",
                "elon musk"
            ],
            "sentiment": "negative",
            "summary": " tesla faces attacks in the US, including vandalism and arson on vehicles and showrooms, prompting the Trump administration to label these as acts of domestic terrorism. Despite founder Elon Musk's defense, the company sees declining sales in Europe due to backlash against Musk's behavior. Meanwhile, Chinese company BYD introduces a faster-charging system, increasing competition. ",
            "title": " tesla Fisla: Once an icon for libs, Musk vehicles now a hated MAGA symbol "
        },
        {
            "Topics": [
                "violence tesla",
                "targeting tesla",
                "elon musk",
                "support vandalism",
                "vandalism targeting"
            ],
            "sentiment": "negative",
            "summary": " Elon Musk condemned audience support for vandalism targeting tesla properties shown in a Daily Show clip hosted by Jordan Klepper. The recent surge in attacks coincides with Trump's new Department of Government Efficiency (DOGE), raising concerns over politically motivated violence against tesla. ",
            "title": " 'Super messed up': Elon Musk slams applause for tesla attacks on The Daily Show "
        },
        {
            "Topics": [
                "shareholder tesla",
                "elon musk",
                "bought tesla",
                "tesla",
                "musk electric"
            ],
            "sentiment": "neutral",
            "summary": " Elon Musk shared his pride with a heart emoji upon discovering his position as the top shareholder in tesla with $173 billion. US President Donald Trump recently bought a tesla Model S, showing his support for Musk's electric vehicle company amid ongoing challenges. ",
            "title": " tesla investor shares tesla's 10 Biggest shareholders, Elon Musk responds with a ... "
        },
        {
            "Topics": [
                "tesla stock",
                "tesla price",
                "tesla falling",
                "stock dropped",
                "cut tesla"
            ],
            "sentiment": "negative",
            "summary": " Elon Musk responded to Minnesota Governor Tim Walz\u2019s mockery of tesla\u2019s falling stock price with a pointed remark. tesla's stock has dropped 44% year-to-date amid concerns over sales, competition, and Musk's distractions like Dogecoin. RBC Capital Markets cut tesla's price target by 27%, reflecting lower expectations for its technology rollout. ",
            "title": " Tim Waltz makes fun of tesla stock, Elon Musk replies with a 'JD Vance joke' "
        },
        {
            "Topics": [
                "keying tesla",
                "tesla costco",
                "arrested keying",
                "jose police",
                "tesla"
            ],
            "sentiment": "neutral",
            "summary": " An individual was arrested for keying a tesla at a Costco car park in South San Jose. Both San Jose's Police Chief and Mayor emphasized respecting the law and addressing grievances legally. Elon Musk referred to the incident as 'domestic terrorism' on social media. ",
            "title": " 'Senseless crime': San Jose Police arrest man for keying tesla in viral video "
        },
        {
            "Topics": [],
            "sentiment": "neutral",
            "summary": " ",
            "title": " Protest against tesla: Showrooms, vehicle lots, charging stations, private cars targeted "
        },
        {
            "Topics": [
                "chinese customers",
                "tesla",
                "local brands",
                "tesla turning",
                "efficient cars"
            ],
            "sentiment": "negative",
            "summary": " Chinese customers who once flocked to tesla are turning more and more to local brands that offer more efficient cars with better technology, sometimes at half the price ",
            "title": " It\u2019s not just the US. tesla sales are cratering in China as well "
        },
        {
            "Topics": [],
            "sentiment": "negative",
            "summary": " ",
            "title": " Tim Walz mocks tesla's falling stock price, owner Elon Musk hits back: 'I look at Vance's portrait in White House' "
        },
        {
            "Topics": [
                "tesla warns",
                "tariffs harm",
                "retaliatory tariffs",
                "tesla",
                "tariffs"
            ],
            "sentiment": "negative",
            "summary": " tesla warns of potential fallout from Trump's trade war, suggesting retaliatory tariffs could harm US electric vehicle manufacturers. The company urges caution to avoid negative impacts on American businesses and recommends a phased implementation approach for any new trade measures. ",
            "title": " tesla warns Trump administration that trade war could harm US EV companies: 'Consider the downstream impacts' "
        }
    ]
}
```

## Deployment
The application is deployed on Hugging Face Spaces. Access the live version here: **[Deployment Link](https://huggingface.co/spaces/pradeepjangirml007/News_flask-api/)**

## Assumptions & Limitations
- Only TIME OF INDIA news websites is supported for web scraping.
- Sentiment analysis is based on textual content and may not always be 100% accurate.
- TTS output may vary in quality based on the open-source model used.

---
### Author: Pradeep Jangir
