import datetime
from playsound import playsound
import os
import sys
from time import sleep
import talk
import speech
import fun

class Alarm:
    def __init__(self):
        #User gives after how many hours and minutes he wish alarm to go off
        recognition = speech.Recognize()
        talk.tellSentence("Na za ile godzin ustawić alarm?")
        self.hours = recognition.recognize()
        talk.tellSentence("Na za ile minut ustawić alarm?")
        self.minutes = recognition.recognize()


    def evokeAlarm(self):
        #Try to cast string values for hour and minute into floats
        try:
            self.hours = float(self.hours)
            print(self.hours)
            #Check if given hour is not negative
            if(self.hours < 0):
                talk.tellSentence("Podałeś złą godzinę")
                return ""
        except ValueError:
            talk.tellSentence("Nie zrozumiałem")
            return ""
        try:
            self.minutes= float(self.minutes)
            print(self.minutes)
            #Check if given minute is not negative
            if(self.minutes < 0):
                talk.tellSentence("Podałeś złą minutę")
                return ""
        except ValueError:
            talk.tellSentence("Nie zrozumiałem")
            return ""

        #If casting and validating ended with success change hours and minutes into seconds
        self.timeToWake = float(self.hours) * 3600 + float(self.minutes) * 60
        print(self.timeToWake)

        #Confirm setting alarm for user
        talk.tellSentence("Ustawiono alarm na za " + str(int(self.hours)) + " godzin i " + str(int(self.minutes)) + " minut")
        #Clone process and run it in background. Go off after given amount of time
        pid = os.fork()
        if pid == 0:
            print("Running task")
            print(self.timeToWake)
            sleep(self.timeToWake)
            self.runAlarm()
            print("Task ended")
            sys.exit()
        else:
            print("Running another task")

    def runAlarm(self):
        #When used plays alarm audio
        playsound("/home/a4ch3r/RoomAssistant/Audio/alarm_2015.wav")
        print("ALARM GOES OFFFFFFFF \n")

def tellTime():
    #Lists with hours and minutes for more human like speaking
    hour = ["północ", "pierwsza", "druga", "trzecia", "czwarta", "piąta", "szósta", "siódma", "ósma", "dziewiąta", "dziesiąta", "jedenasta", "dwunasta", "trzynasta", "czternasta", "piętnasta", "szesnasta", "siedemnasta", "osiemnasta", "dziewiętnasta", "dwudziesta", "dwudziesta pierwsza", "dwudziesta druga", "dwudziesta trzecia"]
    minute = ["", "zero jeden", "zero dwa", "zero trzy", "zero cztery", "zero pięć", "zero sześć", "zero siedem", "zero osiem", "zero dziewięć", "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście", "dwadzieścia", "dwadzieścia jeden", "dwadzieścia dwa", "dwadzieścia trzy", "dwadzieścia cztery", "dwadzieścia pięć", "dwadzieścia sześć", "dwadzieścia siedem", "dwadzieścia osiem", "dwadzieścia dziewięć", "trzydzieści ","trzydzieści jeden", "trzydzieści dwa", "trzydzieści trzy", "trzydzieści cztery", "trzydzieści pięć", "trzydzieści sześć","trzydzieści siedem", "trzydzieści osiem", "trzydzieści dziewięć", "czterdzieści ", "czterdzieści jeden", "czterdzieści dwa", "czterdzieści trzy", "czterdzieści cztery", "czterdzieści pięć", "czterdzieści sześć", "czterdzieści siedem", "czterdzieści osiem", "czterdzieści dziewięć", "pięćdziesiąt", "pięćdziesiąt jeden", "pięćdziesiąt dwa", "pięćdziesiąt trzy", "pięćdziesiąt cztery", "pięćdziesiąt pięć", "pięćdziesiąt sześć", "pięćdziesiąt siedem", "pięćdziesiąt osiem", "pięćdziesiąt dziewięć"]
    
    #Tells current time
    currentTime = datetime.datetime.now()
    hours = currentTime.hour
    minutes = currentTime.minute
    talk.tellSentence("Jest " + hour[hours] + minute[minutes])

def timer():
    talk.tellSentence("Na za ile minut ustawić minutnik?")
    recognizer = speech.Recognize()
    recognized = recognizer.recognize()

    try:
        if(recognized == "jedną"):
            timerTime = 1
        else:
            timerTime = int(recognized)
        talk.tellSentence("Ustawiłem minutnik")
        sleep(timerTime * 60)
        fun.sendMail() 
        playsound("/home/a4ch3r/RoomAssistant/Audio/alarm_2015.wav")

    except ValueError:
        talk.tellSentence("Nie zrozumiałem ")