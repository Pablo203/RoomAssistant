import requests
import datetime
import json

class getWeather:
    def __init__(self, days):
        self.days = days
        self.date = ""
    def getJSONFile(self):
        #writes values returned by API into JSON file
        url = "https://community-open-weather-map.p.rapidapi.com/forecast"

        querystring = {"q":"rybnik,pl"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "eb93f8fd3emsh381900d05a32aecp165355jsnb75ede5ea3c9"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        #Opens a file or creates if file doesn't exist, writes values to it and closes it
        saveFile = open("weather.json", "w")
        saveFile.write(response.text)
        saveFile.close()

    def getWantedDay(self):
        currentDate = datetime.datetime.now()
        self.days = int(self.days)
        newDate = str(currentDate + datetime.timedelta(days = self.days))
        self.date = newDate

    def getInfo(self):
        self.getJSONFile()
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
        day = self.date[:10]

        with open("weather.json") as json_file:
            hourCounter = 0
            currentRun = 0
            '''currentDate = [None] * 5
            currentHour = [None] * 5
            currentTemperature = [None] * 5
            currentFelt = [None] * 5
            currentWeather = [None] * 5
            currentWind = [None] * 5'''
            gettedData = []
            data = json.load(json_file)
            for p in data["list"]:
                if((p["dt_txt"])[:10] == day and (p["dt_txt"])[11:] == hour[hourAccess[hourCounter]]):
                    currentObject = p
                    
                    #What day and hour is given
                    #whichDate = (currentObject["dt_txt"])[:10]
                    #whichHour = (currentObject["dt_txt"])[11:]
                    #What temperature is, what weather and wind
                    #Temperature
                    temperature = currentObject["main"]["temp"]
                    #temperature = round(int(temperature) - 273.15) 
                    feltTemperature = currentObject["main"]["feels_like"]
                    #feltTemperature = round(int(feltTemperature) - 273.15)
                    #Weather
                    #weatherDescription = currentObject["weather"][0]["description"]
                    #Wind
                    #wind = currentObject["wind"]["speed"]
                    gettedData.append(currentObject["wind"]["speed"])
                    gettedData.append(currentObject["weather"][0]["description"])
                    gettedData.append(round(int(feltTemperature) - 273.15))
                    gettedData.append(round(int(temperature) - 273.15))
                    gettedData.append((currentObject["dt_txt"])[11:])
                    gettedData.append((currentObject["dt_txt"])[:10])
                    '''currentDate[currentRun] = whichDate
                    currentHour[currentRun] = whichHour
                    currentTemperature[currentRun] = temperature
                    currentFelt[currentRun] = feltTemperature
                    currentWeather[currentRun] = weatherDescription
                    currentWind[currentRun] = wind'''
                    hourCounter = hourCounter + 1
                    currentRun = currentRun + 1
            '''gettedData = {
                "date": currentDate,
                "hour": currentHour,
                "temperature": currentTemperature,
                "felt": currentFelt,
                "weather": currentWeather,
                "wind": currentWind
            }'''
            return gettedData
x = getWeather(1)
print(x.getInfo())