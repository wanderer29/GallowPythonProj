from Interfaces import StartInterface
from Interfaces import GameInterface
import userKeys
import os

def clearCmd():
    os.system("cls")

def start():
    clearCmd()

    StartInterface.printStartPage()
    
    key = userKeys.getKey()
    
    if key == b'\x1b':
        print("exit")
    elif key == b'\r':
        GameInterface.startGame()
    else:
        print("nothing")
    
