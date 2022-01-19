import speech_recognition as sr
import talk
import json

class Recognize:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recognize(self):
        with self.mic as source:
            #self.r.adjust_for_ambient_noise(source, duration = 1)
            with open("config.json", "r") as configFile:
                    data = json.load(configFile)
            audio = self.r.listen(source, phrase_time_limit=2)
            try:
                
                    recognized = self.r.recognize_google(audio, language=data["language"]["speech"])
                    recognized = recognized.lower()
                    return recognized
            except(sr.RequestError, sr.UnknownValueError):
                talk.tellSentence("Nie zrozumiałem")
                return ""