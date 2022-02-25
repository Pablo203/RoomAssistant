import commands
import os
import speech
import talk
import speech_recognition as sr
import calendars

#Start xampp service at run
os.system("sudo /opt/lampp/./xampp start")

#Run function to check and delete events from Calendar
setup = calendars.Calendar()
setup.evokeSelectDelete()


def executeCommand(command):
    #Use class from another module to provide matching actions
    command = command.lower()
    toExecute = commands.command()

    #Tell current hour
    if("która jest godzina" in command):
        toExecute.timeTell()

    #Set alarm
    elif("ustaw alarm" in command):
        toExecute.alarm()

    #Display weather for next day
    elif("pogoda" in command):
        toExecute.tellWeather()

    #Add event to calendar
    elif("zapisz w kalendarzu" in command):
        toExecute.addEvents()

    #Check Events in calendar
    elif("sprawdź w kalendarzu" in command):
        toExecute.checkEvents()
        
    #Intruder alert
    elif("czerwony alert" in command):
        toExecute.redAlert()

    #Get info from Wikipedia about certain topic
    elif("podaj mi informacje" in command):
        toExecute.getInfo()

    #Gets and tells some programming joke
    elif("powiedz mi żart" in command):
        toExecute.tellSomeJoke()

    #Human interactions functions
    #elif("jesteś uroczy" or "jesteś słodki" or "jesteś kochany" in command):
        #toExecute.complimentResponse()




def listenCommand():
    #Listens to command
    recognition = speech.Recognize()
    talk.tellSentence("Słucham")

    #Pass recognized string into function as string
    recognized = recognition.recognize()
    print(recognized)
    executeCommand(recognized)

#Waits for "manfred" word in recognized string     
def awaitCommand():
    #Define classes necessary for speech recognition
    r = sr.Recognizer()
    mic = sr.Microphone()
    #Get sound from microphone for certain amount of time
    with mic as source:
        audio = r.listen(source, phrase_time_limit=2)
        #Try recognizing speech
        try:
            recognized = r.recognize_google(audio, language='pl-PL')
            recognized = recognized.lower()
            print(recognized)
            #If speech is succesfully recognized check for key word
            if("manfred" in recognized):
                listenCommand()
        except(sr.RequestError, sr.UnknownValueError):
            pass

#Information for user
talk.tellSentence("Już wstałem")

#Listen for keyword in infinite
while(True):
    awaitCommand()