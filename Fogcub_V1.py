###############################################################################
#                             CHATBOT                                         #
###############################################################################
# Setup
## for speech-to-text
import speech_recognition as sr

## for text-to-speech
#from gtts import gTTS

## for language model
import transformers

## for data
import os
import datetime
import numpy as np


# Build the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")

    def classify(self):
        
# Run the AI
if __name__ == "__main__":
    
    ai = ChatBot(name="Fogcub")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    while True:
        ai.speech_to_text()