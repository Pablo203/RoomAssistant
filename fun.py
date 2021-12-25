import gtts
from playsound import playsound


def redAlert():
    tts = gtts.gTTS("Du solltest nicht hierher kommen", lang="de")
    tts.save("Audio/redalert.wav")
    playsound("Audio/redalert.wav")
    playsound("Audio/doom.wav")
