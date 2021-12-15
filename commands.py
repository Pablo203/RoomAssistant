import weather
import times
import calendars
import music
class command:
    def __init__(self):
        pass
    
    def alarm(self):
        setTime = times.Alarm()
        setTime.evokeAlarm()
        print("Alarm set")

    def timeTell(self):
        times.tellTime()

    def tellWeather(self):
        days = input("At what day you want weather?\n")
        outside = weather.getWeather(days)
        print(outside.getInfo())

    def addEvents(self):
        year = input("At what year: ")
        month = input("At what month: ")
        day = input("At what day: ")
        if(int(month) <= 12):
            if(int(day) <= 31):
                date = year + "-" + month + "-" + day
                print(date)
                description = input("Please describe it: ")
                daysbefore = input("How many days before inform you? ")
                calendarModule = calendars.calendar()
                calendarModule.addEvent(date, description, daysbefore)
            else:
                print("Give a valid day")
        else:
            print("Give a valid month")

    def checkEvents(self):
        calendarModule = calendars.calendar()
        calendarModule.displayEvents()

    def deleteEvents(self):
        calendarModule = calendars.calendar()
        calendarModule.deleteEvents()

    def playSong(self):
        songPlay = music.useSpotify()
        songPlay.use()