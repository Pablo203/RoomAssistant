import datetime
from playsound import playsound
import os
import sys
from time import sleep
import talk
import speech

hour = {
    0 : "północ",
    1 : "pierwsza",
    2 : "druga",
    3 : "trzecia",
    4 : "czwarta",
    5 : "piąta",
    6 : "szósta",
    7 : "siódma",
    8 : "ósma",
    9 : "dziewiąta",
    10 : "dziesiąta",
    11 : "jedenasta",
    12 : "dwunasta",
    13 : "trzynasta",
    14 : "czternasta",
    15 : "piętnasta",
    16 : "szesnasta",
    17 : "siedemnasta",
    18 : "osiemnasta",
    19 : "dziewiętnasta",
    20 : "dwudziesta",
    21 : "dwudziesta pierwsza",
    22 : "dwudziesta druga",
    23 : "dwudziesta trzecia"
}
minute = {
    0 : "",
    1 : "zero jeden",
    2 : "zero dwie",
    3 : "zero trzy",
    4 : "zero cztery",
    5 : "zero pięć",
    6 : "zero sześć",
    7 : "zero siedem",
    8 : "zero osiem",
    9 : "zero dziewięć",
    10 : "dziesięć",
    11 : "jedenaście",
    12 : "dwunaście",
    13 : "trzynaście",
    14 : "czternaście",
    15 : "piętnaście",
    16 : "szesnaście",
    17 : "siedemnaście",
    18 : "osiemnaście",
    19 : "dziewiętnaście",
    20 : "dwadzieścia",
    21 : "dwadzieścia jeden",
    22 : "dwadzieścia dwie",
    23 : "dwadzieścia trzy",
    24 : "dwadzieścia cztery",
    25 : "dwadzieścia pięć",
    26 : "dwadzieścia sześć",
    27 : "dwadzieścia siedem",
    28 : "dwadzieścia osiem",
    29 : "dwadzieścia dziewięć",
    30 : "trzydzieści",
    31 : "trzydzieści jeden",
    32 : "trzydzieści dwie",
    33 : "trzydzieści trzy",
    34 : "trzydzieści cztery",
    35 : "trzydzieści pięć",
    36 : "trzydzieści sześć",
    37 : "trzydzieści siedem",
    38 : "trzydzieści osiem",
    39 : "trzydzieści dziewięć",
    40 : "czterdzieści",
    41 : "czterdzieści jeden",
    42 : "czterdzieści dwie",
    43 : "czterdzieści trzy",
    44 : "czterdzieści cztery",
    45 : "czterdzieści pięć",
    46 : "czterdzieści sześć",
    47 : "czterdzieści siedem",
    48 : "czterdzieści osiem",
    49 : "czterdzieści dziewięć",
    50 : "pięćdziesiąt",
    51 : "pięćdziesiąt jeden",
    52 : "pięćdziesiąt dwie",
    53 : "pięćdziesiąt trzy",
    54 : "pięćdziesiąt cztery",
    55 : "pięćdziesiąt pięć",
    56 : "pięćdziesiąt sześć",
    57 : "pięćdziesiąt siedem",
    58 : "pięćdziesiąt osiem",
    59 : "pięćdziesiąt dziewięć"
}

class Alarm:
    def __init__(self):
        #User gives after how many hours and minutes he wish alarm to go off
        recognition = speech.Recognize()
        talk.tellSentence("Na za ile godzin ustawić alarm?")
        self.hours = recognition.recognize()
        talk.tellSentence("Na za ile minut ustawić alarm?")
        self.minutes = recognition.recognize()
    
    def setAlarm(self):
        #Turns hours and minutes to seconds and if failed stops programm
        pass

    def evokeAlarm(self):
        #Clones proccess then sleeps for earlier getted seconds and runs alarm        
        try:
            self.hours = float(self.hours)
            print(self.hours)
        except ValueError:
            return ""
        try:
            self.minutes= float(self.minutes)
            print(self.minutes)
        except ValueError:
            return ""

        self.timeToWake = float(self.hours) * 3600 + float(self.minutes) * 60
        print(self.timeToWake)


        if(self.hours > 24 or self.hours < 0):
            talk.tellSentence("Podałeś złą godzinę")
            return ""
        elif(self.minutes > 60 or self.minutes < 0):
            talk.tellSentence("Podałeś złą minutę")
            return ""
        else:
            pass

        talk.tellSentence("Ustawiono alarm na za " + str(int(self.hours)) + " godzin i " + str(int(self.minutes)) + " minut")
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
        playsound("Audio/alarm_2015.wav")
        print("ALARM GOES OFFFFFFFF \n")

def tellTime():
    #Tells current time
    currentTime = datetime.datetime.now()
    hours = currentTime.hour
    minutes = currentTime.minute
    print(hours)
    print(minutes)
    talk.tellSentence("Jest " + hour[hours] + minute[minutes])