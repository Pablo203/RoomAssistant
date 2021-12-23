import commands
import os
import speech
import talk
import speech_recognition as sr


#os.system("sudo /opt/lampp/.xampp start")


def executeCommand(command):
    command = command.lower()
    toExecute = commands.command()

    #Time functions
    if("która jest godzina" in command):
        toExecute.timeTell()

    elif("ustaw alarm" in command):
        toExecute.alarm()

    #Weather function
    elif("pogoda" in command):
        toExecute.tellWeather()

    #Add event to calendar
    elif("zapisz w kalendarzu" in command):
        toExecute.addEvents()
    #Check Events in calendar
    elif("sprawdź w kalendarzu" in command):
        toExecute.checkEvents()
    #Play song
    elif("puść piosenkę" in command):
        toExecute.playSong()
    #Led function
    elif("led" in command):
        print("LED's")



def listenCommand():
    #Listens to command
    recognition = speech.Recognize()
    talk.tellSentence("Słucham")

    recognized = recognition.recognize()
    executeCommand(recognized)

        
def awaitCommand():
    #Waits for "manfred" word in string
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        try:
            recognized = r.recognize_google(audio, language='pl-PL')
            recognized = recognized.lower()
            print(recognized)
            if("manfred" in recognized):
                listenCommand()
        except(sr.RequestError, sr.UnknownValueError):
            pass
    

while(True):
    awaitCommand()