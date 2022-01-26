import pymysql
import datetime
import json
import os
import sys
from time import sleep
import talk
import speech


class Calendar:
    def __init__(self):
        #Open config file and get all credentials from it
        with open("config.json", "r") as configFile:
            data = json.load(configFile)
            #Get hour at which reminder will work
            self.hourToTellEvent = data["calendar"]["hourToTellEvents"]
            self.afterHowManyDaysDelete = data["calendar"]["afterHowManyDaysDeleteEvent"]
            #Get all variables for connecting to DB
            self.mydb = pymysql.connect(
                host = data["database"]["host"],
                user = data["database"]["user"],
                password = data["database"]["password"],
                database = data["database"]["databaseName"]
            )
    

    def addEvent(self):
        recognition = speech.Recognize()
        #Get clean date
        date = self.cleanDate()
        if(date == False):
            return ""
        
        #Gets description of event and how many days before inform user
        talk.tellSentence("Proszę opisz to wydarzenie")
        description = recognition.recognize()
        talk.tellSentence("Ile dni wcześniej Cię poinformować?")
        daysbefore = recognition.recognize()
        #If days before is impossible to cast into int stop function
        try:
            daysBefore = int(daysbefore)
        except ValueError:
            talk.tellSentence("Coś poszło nie tak")
            return
        
        #Get cursor, execute query and save changes into database
        mycursor = self.mydb.cursor()
        query = "INSERT INTO Events (EventDate, Description, DaysBefore) VALUES (%s, %s, %s)"
        mycursor.execute(query, (date, description, daysBefore))
        self.mydb.commit()
        talk.tellSentence("Dodałem wydarzenie do kalendarza")

    def cleanDate(self):
        recognition = speech.Recognize()
        #Get year, month and day from user
        talk.tellSentence("Na który rok?")
        year = recognition.recognize()
        talk.tellSentence("Na który miesiąc")
        month = recognition.recognize()
        talk.tellSentence("Na który dzień")
        day = recognition.recognize()

        #Try to cast getted data into int, else stop function
        #Cast year
        try:
            year = int(year)
        except ValueError:
            talk.tellSentence("Nie zrozumiałem roku")
            return False
        #Cast month
        try:
            if(month == "jeden"):
                month = 1
            else:
                month = int(month)                    
        except ValueError:
            talk.tellSentence("Nie zrozumiałem miesiąca")
            return False
        #Cast day
        try:
            if(day == "jeden"):
                day = 1
            else:
                day = int(day)
        except ValueError:
            talk.tellSentence("Nie zrozumiałem dnia")
            return False

        if(int(month) <= 12):
            if(int(day) <=31):
                date = str(year) + "-" + str(month) + "-" + str(day)
                return date
            
        talk.tellSentence("Podałeś zły dzień lub miesiąc")
        return False
        

    def getEvents(self):
        mycursor = self.mydb.cursor()
        #Get Event Date, Description of event and how many days before to tell about it and prepare it for display
        mycursor.execute("SELECT EventDate FROM Events")
        result = mycursor.fetchall()
        self.eventDate = result

        mycursor.execute("SELECT Description FROM Events")
        result = mycursor.fetchall()
        self.description = result

        mycursor.execute("SELECT DaysBefore FROM Events")
        result = mycursor.fetchall()
        self.daysBefore = result

    def displayEvents(self):
        #Get all events from database
        self.getEvents()
        counter = 0
        for x in self.daysBefore:
            for y in self.eventDate:
                howManyDaysEarlier = x
                EventDate = y
                #Get next element from days before and event date
                howManyDaysEarlier = howManyDaysEarlier[0]
                EventDate = EventDate[0]
                #Calculate date on which remind user about event
                EventDate = EventDate - datetime.timedelta(days = howManyDaysEarlier)
                #Get today data and extract Year, Month and Day
                todayDate = datetime.datetime.now()
                todayDate = str(todayDate)[:10]
                #Check if today date is matching with date calculated from days before
                if(str(EventDate) == todayDate):
                    talk.tellSentence(f"Dnia {y} masz wydarzenie {self.description[counter][0]}")
            counter += 1      
    

    def deleteEvents(self):
        #Calculate date on which record should be deleted
        date = datetime.datetime.now()
        date = date - datetime.timedelta(days = self.afterHowManyDaysDelete)
        date = str(date)[:11]
        print(date)
        mycursor = self.mydb.cursor()
        #Delete all records with calculated date
        query = ("DELETE FROM Events WHERE EventDate = %s")
        mycursor.execute(query, (date))
        self.mydb.commit()

    def evokeSelectDelete(self):
        #Calculate how much time is left to next evoke
        #First get date from __init__(), then get current hour and minute and count how many hours and minutes is left to date from __init__()
        timenow = datetime.datetime.now().strftime('%H:%M')
        deadline = self.hourToTellEvent
        start = datetime.datetime.strptime(timenow,'%H:%M')
        ends = datetime.datetime.strptime(deadline, '%H:%M')
        result = ends-start
        #Create proccess that will go off after seconds gotten from calculations
        pid = os.fork()
        if pid == 0:
            print("Running task")
            sleep(result.seconds)
            self.displayEvents()
            self.deleteEvents()
            self.evokeSelectDelete()
            print("Task ended")
            
            sys.exit()
        else:
            print("Running another task")