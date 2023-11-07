import userKeys
import os
import random

def clearCmd():
    os.system("cls")

def getRandomWord(wordsArr):
    randomNum = random.randint(0, len(wordsArr) - 1)
    return wordsArr[randomNum]

def printGallow(stage):
    if stage == 1:
        print ('|\n|\n|\n|\n|\n|\n|\n|\n|\n|')
    if stage == 2:
        print ('|---------')
        print ('|\n|\n|\n|\n|\n|\n|\n|\n|')
    if stage == 3:
        print ('|---------')
        print ('|        |')
        print ('|        |')
        print ('|\n|\n|\n|\n|\n|\n|')
    if stage == 4:
        print ('|---------')
        print ('|        |')
        print ('|        |')
        print ('|        -')
        print ('|       /_\\')
        print ('|\n|\n|\n|\n|\n|')      
    if stage == 5:
        print ('|---------')
        print ('|        |')
        print ('|        |')
        print ('|        -')
        print ('|       /_\\')
        print ('|\n|\n|\n|')
        print ('|        __')
        print ('|       |  |')
    if stage == 6:
        print ('|---------')
        print ('|        |')
        print ('|        |')
        print ('|        O')
        print ('|       /|\\')
        print ('|      / | \\')
        print ('|       / \\')
        print ('|      /   \\')
        print ('|')
        print ('|           ')
        print ('|       DIED') 

def encryptWord(word):
    result = ''
    for i in word:
        result += '*'
    return result

def openLetters(word, letter):
    return word

def askUser(encWord):
    state = 0
    userLetters = []

    while state <= 6:
        print (f"Guess the word: {encWord}")
        print ("Enter a letter:")
        userKey = userKeys.getLetter()
        userLetters.append(userKey)
        print (f"You entered: {userLetters}")


def startGame():
    with open("words.txt", "r", encoding="utf-8") as file:
        file_contents = file.read()
    
    #Setting word
    wordsArr = file_contents.split()
    word = getRandomWord(wordsArr)
    encWord = encryptWord(word)

    #User Interface
    askUser(encWord)

    
    # printGallow(6)

    

    
    # Print the contents of the file
    





