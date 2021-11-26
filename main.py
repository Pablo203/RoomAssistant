import weather
import times

def executeCommand(command):
    command = command.lower()
    #Time functions
    if("what time is it" in command):
        times.tellTime()
    elif("set alarm" in command):
        alarm = times.Alarm()
        alarm.evokeAlarm()
        print("Alarm set")

    elif("weather" in command):
        days = input("At what day you want weather?\n")
        outside = weather.getWeather(days)
        print(outside.getInfo())
        print("There is some shitty weather outside")
    #LED functions
    elif("led" in command):
        print("LED's")



def listenCommand():
    command = input("Tell me what i need to do:\n")
    executeCommand(command)


def awaitCommand():
    awake = input("What do you want?\n")
    awake = awake.lower()
    if("manfred" in awake):
        listenCommand()

while(True):
    awaitCommand()