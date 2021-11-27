import weather
import times
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