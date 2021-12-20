import gtts
from playsound import playsound

def tellSentence(text):
    tts = gtts.gTTS(text, lang="pl")
    tts.save("Audio/response.wav")
    playsound("Audio/response.wav")