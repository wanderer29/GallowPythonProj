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
        return
    elif key == b'\r':
    
        GameInterface.startGame()
        StartInterface.printStartPage()

        while True:
            key = userKeys.getKey()
            if (key == b'\x1b'):
                return
            elif key == b'\r':
                GameInterface.startGame()
                StartInterface.printStartPage()
            




        
        
        
    
