import weather

def executeCommand(command):
    command = command.lower()
    #Time functions
    if("what time is it" in command):
        print("Its some time now")
        pass
    elif("set alarm" in command):
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