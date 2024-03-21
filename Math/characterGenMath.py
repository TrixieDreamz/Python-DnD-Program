import dice 

statSelections = []

def statGenerator():
    j = 0
    while j < 6:
        attributeStatsList = []
        total = 0
        i = 0
        while i < 4:
            result = dice.diceRoller(1, 6, 0)
            attributeStatsList.append(result)
            total += result
            i += 1
        print("Attribute Rolls:", attributeStatsList)
        print("")
        print(f"4d6 roll is = {total}")
        print("")
        if total < 10:  # Check if total is less than 10
            total = 10  # Adjust to 10 if necessary
        statSelections.append(total)
        j += 1

def viewRolledStats():
    i = 0
    while i < len(statSelections):
        print(statSelections[i])
        i += 1
    return

