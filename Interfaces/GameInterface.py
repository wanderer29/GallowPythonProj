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

def checkLetter(letter, word, userLetters):
    return ((letter in word) )

def openLetter(letter, word, encWord):
    for i in range(len(word)):
        if (letter == word[i]):
            encWord = encWord[:i] + letter + encWord[(i+1):]
    return encWord
    
def isGuessed(encWord):
    return not ('*' in encWord)

def askUser(encWord, word):
    state = 0
    userLetters = []
    outputWord = ""

    while state < 6 and isGuessed(encWord) == False:
        printGallow(state)
        print (f"\nGuess the word: {encWord}")
        print ("Enter a letter:")

        
        # Read user Key if it not in userLetters
        while True:
            userKey = userKeys.getLetter().lower()
            if (userKey not in userLetters):
                break

        userLetters.append(userKey)

        # Output word for user
        outputWord = " ".join(userLetters)
        print (f"You entered: {outputWord}")

        if (userKey == '\x1b'):
            break
        elif (not ('*' in encWord)):
            break
        elif (checkLetter(userKey, word, userLetters)):
            encWord = openLetter(userKey, word, encWord)
        else:
            state += 1
    printGallow(state)
    
    if isGuessed(encWord):
        print ('You guessed right!')
    else:
        print('Game is over!')
        print('Unfortunately you guessed wrong')
        


def startGame():
    with open("words.txt", "r", encoding="utf-8") as file:
        file_contents = file.read()
    
    #Setting word
    wordsArr = file_contents.split()
    word = getRandomWord(wordsArr)
    encWord = encryptWord(word)

    #User Interface
    askUser(encWord, word)

    





