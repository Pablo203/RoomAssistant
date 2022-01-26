import speech_recognition as sr
import talk
import json

class Recognize:
    def __init__(self):
        #Define classes for speech recognition
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recognize(self):
        #Get audio using microphone
        with self.mic as source:
            #self.r.adjust_for_ambient_noise(source, duration = 1)
            #Get language of recognizing from config file
            with open("config.json", "r") as configFile:
                    data = json.load(configFile)
            #Listen with microphone
            audio = self.r.listen(source, phrase_time_limit=2)

            #Try to recognize what was said
            #If successfull return string with recognized sentence
            try:            
                    recognized = self.r.recognize_google(audio, language=data["language"]["speech"])
                    recognized = recognized.lower()
                    return recognized
            #Else give user information about error
            except(sr.RequestError, sr.UnknownValueError):
                talk.tellSentence("Nie zrozumiałem")
                return ""