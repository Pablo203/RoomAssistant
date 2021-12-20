import speech_recognition as sr
import talk

class Recognize:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recognize(self):
        with self.mic as source:
            audio = self.r.listen(source)
            try:
                recognized = self.r.recognize_google(audio)
                recognized = recognized.lower()
                return recognized
            except(sr.RequestError, sr.UnknownValueError):
                talk.tellSentence("Nie zrozumiałem")
                return ""