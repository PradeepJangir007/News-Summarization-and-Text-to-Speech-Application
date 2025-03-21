import io
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS

class Hinditts:
    """Class to translate text to Hindi and generate speech output."""
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-hi"
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = self.model.generate(**inputs)
        return self.tokenizer.decode(translated[0], skip_special_tokens=True)

    def generate_audio(self, text_t):
        """Generates Hindi speech output from news summary."""
        translated_text = self.translate(text_t)
        tts = gTTS(translated_text, lang='hi')
        audio_io = io.BytesIO()
        tts.write_to_fp(audio_io)
        audio_io.seek(0)
        return audio_io
