import weather
import times
import calendars
import talk
import speech
import fun

#Class to control all functions of programm
class command:
    def __init__(self):
        pass
    
    #Alarm setting
    def alarm(self):
        setTime = times.Alarm()
        setTime.evokeAlarm()

    #Basically clock
    def timeTell(self):
        times.tellTime()

    #Give weather
    def tellWeather(self):
        outside = weather.GetWeather()
        outside.displayInfo()

    #Add event to calendar
    def addEvents(self):
        calendarModule = calendars.Calendar()
        calendarModule.addEvent()

    #Check events
    def checkEvents(self):
        calendarModule = calendars.Calendar()
        calendarModule.displayEvents()

    #Delete events
    def deleteEvents(self):
        calendarModule = calendars.Calendar()
        calendarModule.deleteEvents()

    #Warning intruder
    def redAlert(self):
        fun.redAlert()

    #Get wikipedia info
    def getInfo(self):
        fun.getWikipediaInfo()

    #Tell some jokes
    def tellSomeJoke(self):
        fun.tellJoke()