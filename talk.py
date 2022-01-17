import gtts
from playsound import playsound
import json

def tellSentence(text):
    with open("config.json", "r") as configFile:
        data = json.load(configFile)
        tts = gtts.gTTS(text, lang=data["language"]["response"])
        tts.save("Audio/response.wav")
        playsound("Audio/response.wav")