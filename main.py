import commands
import os
import speech
import talk
import speech_recognition as sr
import calendars

os.system("sudo /opt/lampp/./xampp start")
setup = calendars.Calendar()
setup.evokeSelectDelete()


def executeCommand(command):
    command = command.lower()
    toExecute = commands.command()

    #Time functions
    if("która jest godzina" in command):
        toExecute.timeTell()

    #Set alarm
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
    
    elif("czerwony alert" in command):
        toExecute.redAlert()

    #Human interactions functions
    #elif("jesteś uroczy" or "jesteś słodki" or "jesteś kochany" in command):
        #toExecute.complimentResponse()




def listenCommand():
    #Listens to command
    recognition = speech.Recognize()
    talk.tellSentence("Słucham")

    #Pass recognized word into function as string
    recognized = recognition.recognize()
    print(recognized)
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

talk.tellSentence("Już wstałem")

while(True):
    awaitCommand()