import random

recentDiceResults = []

def diceRoller(numberOfDice, diceType, modifier):    
    i = 0
    sum = 0
    while i < numberOfDice:
        randomNumber = random.randint(1, diceType)
        result = randomNumber + modifier
        print (f"The roll was '{result}'. {randomNumber} + {modifier} on a d{diceType}")
        recentDiceResults.append(result)
        sum += result
        i += 1
    print(f"The sum is: {sum}")
    print("")
    return sum

def viewRecentDiceResults():
   for result in recentDiceResults:
    print(f"History of rolls: {result}")

def deleteRecentDiceResults():
    recentDiceResults.clear()
    print("Cleared recent dice history.")

def rollAdvantage():
    advantageDice1 = diceRoller(1,20,0)
    advantageDice2 = diceRoller(1,20,0)
    if advantageDice1 > advantageDice2:
        return print(f"The higher roll was: {advantageDice1}")
    elif advantageDice1 == advantageDice2:
        return print(f"The higher roll was: {advantageDice1}")
    else: return print(f"The higher roll was: {advantageDice2}")

def rollDisadvantage():
    advantageDice1 = diceRoller(1,20,0)
    advantageDice2 = diceRoller(1,20,0)
    if advantageDice1 > advantageDice2:
        return print(f"The lower roll was: {advantageDice2}")
    elif advantageDice1 == advantageDice2:
        return print(f"The lower roll was: {advantageDice1}")
    else: return print(f"The lower roll was: {advantageDice1}")

def criticalFailureCheck(result):
    if result == 1:
        print("CRITICAL FAILURE!")

   