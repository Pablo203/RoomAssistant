import requests
import datetime
import json
import talk
import speech

class GetWeather:
    def __init__(self):
        self.days = 1
        self.date = ""

    def getJSONFile(self):
        #Gets data from Weather API and saves it in JSON file
        with open("/home/a4ch3r/RoomAssistant/config.json", "r") as configFile:
            #Gets info about url, city, and API credentials from config file
            data = json.load(configFile)
            url = data["weather"]["url"]

            querystring = {"q":data["weather"]["city"]}

            headers = {
                'x-rapidapi-host': data["weather"]["rapid-api-host"],
                'x-rapidapi-key': data["weather"]["rapid-api-key"]
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            #Opens a file or creates if file doesn't exist, writes values to it and closes it
            saveFile = open("/home/a4ch3r/RoomAssistant/weather.json", "w")
            saveFile.write(response.text)
            saveFile.close()

    def getWantedDay(self):
        #Ask user at what day it want weather
        recognizes = speech.Recognize()
        talk.tellSentence("Na za ile dni chcesz pogodę?")
        recognized = recognizes.recognize()
        #Try to cast gotten string into number
        if("jeden" in recognized):
            self.days = 1
        else:
            try:
                self.days = int(recognized)
            except ValueError:
                talk.tellSentence("Nie zrozumiałem dnia")
                return ""
        #Gets wanted date which is few days ahead to compare with dates in JSON
        currentDate = datetime.datetime.now()
        self.days = int(self.days)
        newDate = str(currentDate + datetime.timedelta(days = self.days))
        self.date = newDate

    def getInfo(self):
        #Get info from API
        self.getJSONFile()
        #Get wanted date
        self.getWantedDay()
        hour = {
            "01" : "01:00:00",
            "06" : "06:00:00",
            "09" : "09:00:00",
            "12" : "12:00:00",
            "15" : "15:00:00",
            "18" : "18:00:00"
        }
        hourAccess = ["06", "09", "12", "15", "18", "01"]

        #Slice year, month and day from date
        day = self.date[:10]

        #Extract data from JSON file
        with open("/home/a4ch3r/RoomAssistant/weather.json") as json_file:
            #Define variables for later use
            hourCounter = 0
            currentRun = 0
            gettedData = []
            #Load JSON file
            data = json.load(json_file)
            for p in data["list"]:
                #If date and hour in file is matching with day and hour specified by user append data to array
                if((p["dt_txt"])[:10] == day and (p["dt_txt"])[11:] == hour[hourAccess[hourCounter]]):
                    currentObject = p

                    #Append matching data into list
                    #What day and hour are given
                    gettedData.append((currentObject["dt_txt"])[:10])
                    gettedData.append((currentObject["dt_txt"])[11:])

                    #What temperature is it
                    gettedData.append(round(int(currentObject["main"]["temp"]) - 273.15))
                    gettedData.append(round(int(currentObject["main"]["feels_like"]) - 273.15))
                    
                    #Weather description
                    gettedData.append(currentObject["weather"][0]["description"])
                    gettedData.append(currentObject["wind"]["speed"])

                    hourCounter = hourCounter + 1
                    currentRun = currentRun + 1
            #Return array with all data
            return gettedData
    
    #Give more human like text to read based on temperature
    def determineTemperatureName(self, temperatureNumber):
        temperatureIndicator = abs(int(temperatureNumber))
        temperature = ["stopni", "stopień", "stopnie", "stopnie", "stopnie", "stopni"]

        if(temperatureIndicator == 0):
            temperatureName = temperature[temperatureIndicator]
        elif(temperatureIndicator == 1):
            temperatureName = temperature[temperatureIndicator]
        elif(temperatureIndicator == 2 or temperatureIndicator == 3 or temperatureIndicator == 4):
            temperatureName = temperature[temperatureIndicator]
        elif(temperatureIndicator >= 5):
            temperatureName = temperature[5]

        return temperatureName
            
    #Give more human like text to read based on hour
    def determineHour(self, date):
        hour = date[0:2]
        if(hour == "06"):
            return "szóstej"
        elif(hour == "09"):
            return "dziewiątej"
        elif(hour == "12"):
            return "dwunastej"
        elif(hour == "15"):
            return "piętnastej"
        elif(hour == "18"):
            return "osiemnastej"
        elif(hour == "21"):
            return "dwudziestej pierwszej"

    #Main function to display all informations about weather
    def displayInfo(self):
        #Write created list into data variable
        data = self.getInfo()
        print(data)
        #Extract date from beginnig of list
        date = data[0]
        #Extract day, month and year from date
        day = date[8:]
        month = date[5:7]
        year = date[:4]
        #Tell date for which weather will be given
        talk.tellSentence("Dnia " + day + " " + month + " " + year)
        for i in range(5):
            for j in range(7):
                if(((i*6) + j) % 6 == 0):
                    #Pass all other dates
                    pass
                else:
                    if(j == 1):
                        #Inform about hour for which weather is given
                        print(data[(i*6) + j])
                        hour = self.determineHour(data[(i*6) + j])
                        talk.tellSentence(f"O godzinie {hour}")
                    elif(j == 2):
                        #Inform about temperature in specific hour
                        temp = data[(i*6) + j]
                        temperatureName = self.determineTemperatureName(temp)
                        print(temp)
                        talk.tellSentence(f"Temperatura będzie wynosić {data[(i*6) + j]} {temperatureName}")
                    elif(j == 3):
                        #Inform about feel temperature in specific hour
                        temp = data[(i*6) + j]
                        temperatureName = self.determineTemperatureName(temp)
                        print(data[(i*6) + j])
                        talk.tellSentence(f"Temperatura odczuwalna będzie wynosić {data[(i*6) + j]} {temperatureName}")
                    elif(j == 4):
                        #Inform about falls in specific hour
                        print(data[(i*6) + j])
                    elif(j == 5):
                        #Inform about wind speed in specific hour
                        print(data[(i*6) + j])
                        talk.tellSentence(f"Wiatr będzie wiał z prdkością {data[(i*6) + j]} kilometrów na godzinę")