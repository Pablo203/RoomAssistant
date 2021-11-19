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

x = getWeather(1)
x.getJSONFile()