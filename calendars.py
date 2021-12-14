import pymysql
import datetime
import os

class calendar:
    def __init__(self):
        self.mydb = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'Calendar'
        )
    

    def addEvent(self, date, description, daysBefore):
        mycursor = self.mydb.cursor()
        query = "INSERT INTO Events (EventDate, Description, DaysBefore) VALUES (%s, %s, %s)"
        mycursor.execute(query, (date, description, daysBefore))
        self.mydb.commit()

    def getEvents(self):
        mycursor = self.mydb.cursor()

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
        self.getEvents()
        counter = 0
        #Get today date => Get DaysBefore from query => Modify set date => if EventDate == toModifiedDate display info
        #Get event date - daysbefore == today print
        for x in self.daysBefore:
            for y in self.eventDate:
                howManyDaysEarlier = x
                EventDate = y
                howManyDaysEarlier = howManyDaysEarlier[0]
                EventDate = EventDate[0]
                EventDate = EventDate - datetime.timedelta(days = howManyDaysEarlier)
                todayDate = datetime.datetime.now()
                todayDate = str(todayDate)[:10]
                if(str(EventDate) == todayDate):
                    print("Hi")
                    print(self.description[counter][0])
            counter += 1      
    
    def deleteEvent(self):
        date = datetime.datetime.now()
        date = date - datetime.timedelta(days = 7)
        date = str(date)[:11]
        print(date)
        mycursor = self.mydb.cursor()
        query = ("DELETE FROM Events WHERE EventDate = %s")
        mycursor.execute(query, (date))
        self.mydb.commit()