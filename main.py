import commands

def executeCommand(command):
    command = command.lower()
    toExecute = commands.command()

    #Time functions
    if("what time is it" in command):
        toExecute.timeTell()

    elif("set alarm" in command):
        toExecute.alarm()

    #Weather function
    elif("weather" in command):
        toExecute.tellWeather()

    #Led function
    elif("led" in command):
        print("LED's")



def listenCommand():
    #Listens to command
    command = input("Tell me what i need to do:\n")
    executeCommand(command)


def awaitCommand():
    #Waits for "manfred" word in string
    awake = input("What do you want?\n")
    awake = awake.lower()
    if("manfred" in awake):
        listenCommand()

while(True):
    awaitCommand()