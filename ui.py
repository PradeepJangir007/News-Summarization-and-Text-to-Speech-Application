import streamlit as st
import requests

BASE_URL = "https://3da5-35-240-242-126.ngrok-free.app"
# Initialize session state for news_data
if "news_data" not in st.session_state:
    st.session_state.news_data = None
st.title("News Sentiment Analysis and TTS")
st.write("This application analyzes the news sentiment of a company and generates an audio file in Hindi.")

company_name = st.text_input("Enter Company Name:")

if st.button("Analyze News"):
    if company_name:
        with st.spinner("Fetching and analyzing news..."):
            response = requests.get(f"{BASE_URL}/analyze", params={"company": company_name})
            if response.status_code == 200:
                st.session_state.news_data = response.json()
                st.success("News analyzed successfully!")
                st.json(st.session_state.news_data)
            else:
                st.error("Failed to fetch data. Try again.")
    else:
        st.warning("Please enter a company name.")

if st.button("Generate Hindi Audio"):
    print(st.session_state.news_data)
    if st.session_state.news_data is not None:
        text = str(st.session_state.news_data["Final Sentiment Analysis"]).strip()
        print(text)
        with st.spinner("Generating Hindi audio..."):
            response = requests.get(f"{BASE_URL}/generate_audio", params={"text": text})
            if response.status_code == 200:
                with open("downloaded_sample.mp3", "wb") as file:
                    file.write(response.content)
                st.success("Audio generated successfully!")
                st.audio("downloaded_sample.mp3", format="audio/mp3")
            else:
                st.error("Failed to generate audio. Try again.")
    else:
        st.warning("Please analyze news first before generating audio.")
