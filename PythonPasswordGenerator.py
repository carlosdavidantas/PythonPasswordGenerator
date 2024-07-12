import random

lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
upperCaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "@#$%&*"
numbers = "0123456789"

chars = [lowerAlphabet,upperCaseChars,symbols,numbers]

passwordLength = 80000
specialChars = int(passwordLength * 20 / 100)
upperCharsCount = int(passwordLength * 20 / 100)
numbersCount = int(passwordLength * 20 / 100)
lowerCharsCount = passwordLength - (specialChars + upperCharsCount + numbersCount)

freePasswordPositions = []
password = []

for i in range(passwordLength):
    freePasswordPositions.append(i)
    password.append(i)
    
def InsertCharsTypes(charType, charCount):
    while charCount > 0:
        randomPosition = random.choice(freePasswordPositions.copy())
        password[randomPosition] = random.choice(charType)
        freePasswordPositions.remove(randomPosition)
        charCount -= 1
    
InsertCharsTypes(lowerAlphabet, lowerCharsCount)
InsertCharsTypes(upperCaseChars, upperCharsCount)
InsertCharsTypes(symbols, specialChars)
InsertCharsTypes(numbers, numbersCount)

pw = ""
for char in password:
    pw += f"{char}"
    
print(pw)
