import gtts
from playsound import playsound
import json

def tellSentence(text):
    #Get language in which responses should be said
    with open("config.json", "r") as configFile:
        data = json.load(configFile)
        tts = gtts.gTTS(text, lang=data["language"]["response"])
        #Save response to file and play it
        tts.save("Audio/response.wav")
        playsound("Audio/response.wav")