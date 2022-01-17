import weather
import times
import calendars
import music
import talk
import speech
import fun
import interaction

#Class to control all functions of programm
class command:
    def __init__(self):
        pass
    
    def alarm(self):
        setTime = times.Alarm()
        setTime.evokeAlarm()

    def timeTell(self):
        times.tellTime()

    def tellWeather(self):
        outside = weather.GetWeather()
        outside.displayInfo()

    def addEvents(self):
        recognition = speech.Recognize()
        #Get year, month and day from user
        talk.tellSentence("Na który rok?")
        year = recognition.recognize()
        talk.tellSentence("Na który miesiąc")
        month = recognition.recognize()
        talk.tellSentence("Na który dzień")
        day = recognition.recognize()
        #Try to cast getted data into int, else stop function
        try:
            year = int(year)
        except ValueError:
            talk.tellSentence("Nie zrozumiałem roku")
            return False
        try:
            if(month == "jeden"):
                month = 1
            else:
                month = int(month)                    
        except ValueError:
            talk.tellSentence("Nie zrozumiałem miesiąca")
            return False
        try:
            if(day == "jeden"):
                day = 1
            else:
                day = int(day)
        except ValueError:
            talk.tellSentence("Nie zrozumiałem dnia")
            return False
        
        #Check if month or days is out of scale
        if(int(month) <= 12):
            if(int(day) <= 31):
                date = str(year) + "-" + str(month) + "-" + str(day)
                print(date)
                #Gets description of event and how many days before inform user
                talk.tellSentence("Proszę opisz to wydarzenie")
                description = recognition.recognize()
                talk.tellSentence("Ile dni wcześniej Cię poinformować?")
                daysbefore = recognition.recognize()
                print(daysbefore)
                #If days before is impossible to cast into int stop function
                try:
                    daysbefore = int(daysbefore)
                except ValueError:
                    talk.tellSentence("Coś poszło nie tak")
                    return
                #If everything went well add event to calendar
                calendarModule = calendars.Calendar()
                calendarModule.addEvent(date, description, daysbefore)
                talk.tellSentence("Dodałem wydarzenie do kalendarza")
            else:
                talk.tellSentence("Give a valid day")
        else:
            talk.tellSentence("Give a valid month")

    def checkEvents(self):
        calendarModule = calendars.Calendar()
        calendarModule.displayEvents()

    def deleteEvents(self):
        calendarModule = calendars.Calendar()
        calendarModule.deleteEvents()

    def redAlert(self):
        fun.redAlert()

    #To finish to controll with voice
    def playSong(self):
        songPlay = music.useSpotify()
        songPlay.use()

    def complimentResponse():
        wayToInteract = interaction.Interactions()
        wayToInteract.lookComplimentResponse()