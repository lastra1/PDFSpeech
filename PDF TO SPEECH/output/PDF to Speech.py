import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    return tts

def save_audio(tts, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    tts.save(output_file)

def main():
    pdf_path = 'Beginning Programming for Dummies.pdf'
    output_audio_path = 'output/audio.mp3'

    # Convert PDF to text
    pdf_text = pdf_to_text(pdf_path)

    # Convert text to speech
    tts = text_to_speech(pdf_text)

    # Save the audio file
    save_audio(tts, output_audio_path)

    print(f"Audio file saved at: {output_audio_path}")

if __name__ == "__main__":
    main()
