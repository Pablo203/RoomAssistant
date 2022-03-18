import gtts
from playsound import playsound
import pyjokes
from googletrans import Translator
import wikipediaapi
import talk
import speech
import yagmail


def redAlert():
    tts = gtts.gTTS("Du solltest nicht hierher kommen", lang="de")
    tts.save("Audio/redalert.wav")
    playsound("Audio/redalert.wav")
    playsound("Audio/doom.wav")

def tellJoke():
    translator = Translator()
    joke = pyjokes.get_joke()
    result = translator.translate(joke, dest='pl')
    print(joke)
    print(result.text)
    talk.tellSentence(result.text)


def getWikipediaInfo():
    recognition = speech.Recognize()
    talk.tellSentence("O jakim temacie chcesz usłyszeć?")
    subject = recognition.recognize()
    wiki = wikipediaapi.Wikipedia('pl')
    page_py = wiki.page(subject)
    if(page_py.summary == ""):
        talk.tellSentence("Nie znalazłem żadnych informacji")
    else:
        talk.tellSentence(page_py.summary)

def sendMail():
    receiver = "pawelrosa686@gmail.com"
    body = "You asked me to remind you something. \n I hope you remember what it was cause I don't :P"
    yag = yagmail.SMTP("manfredAssistant@gmail.com")

    yag.send(
        to=receiver,
        subject="Something important, I think",
        contents=body
    )