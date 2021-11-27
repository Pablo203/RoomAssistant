import datetime
from playsound import playsound
import time
import os
import sys
from time import sleep

class Alarm:
    def __init__(self):
        #User gives after how many hours and minutes he wish alarm to go off
        self.hours = input("In how many hours you want me to wake you up? ")
        self.minutes = input("In how many minutes you want me to wake you up? ")
    
    def setAlarm(self):
        #Turns hours and minutes to seconds
        self.timeToWake = float(self.hours) * 3600 + float(self.minutes) * 60

    def evokeAlarm(self):
        #Clones proccess then sleeps for earlier getted seconds and runs alarm
        pid = os.fork()
        if pid == 0:
            print("Running task")
            self.setAlarm()
            print(self.timeToWake)
            sleep(self.timeToWake)
            self.runAlarm()
            print("Task ended")
            sys.exit()
        else:
            print("Running another task")

    def runAlarm(self):
        #When used plays alarm audio
        playsound("Audio/alarm_2015.mp3")
        print("ALARM GOES OFFFFFFFF \n")

def tellTime():
    #Tells current time
    currentTime = datetime.datetime.now()
    hours = currentTime.hour
    minutes = currentTime.minute
    print(hours)
    print(minutes)