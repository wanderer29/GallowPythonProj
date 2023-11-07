import msvcrt

def getKey():
    return msvcrt.getch()

def getLetter():
    letter = ''
    
    while True:
        try:
            letter = msvcrt.getch().decode()
            break
        except Exception as e:
            continue

    return letter


