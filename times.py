import datetime
import time
import os
import sys
from time import sleep

class Alarm:
    def __init__(self):
        self.hours = input("In how many hours you want me to wake you up? ")
        self.minutes = input("In how many minutes you want me to wake you up? ")
    
    def setAlarm(self):
        self.timeToWake = float(self.hours) * 3600 + float(self.minutes) * 60

    def evokeAlarm(self):
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
        print("ALARM GOES OFFFFFFFF \n")

def tellTime():
        currentTime = datetime.datetime.now()
        hours = currentTime.hour
        minutes = currentTime.minute
        print(hours)
        print(minutes)