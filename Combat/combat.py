import dice

def rollAttack(minNumNeededToCrit, combatModifier):
    

    result = dice.diceRoller(1,20,combatModifier)
    
    if result >= minNumNeededToCrit:
        print("A CRITICAL HIT!")
    dice.criticalFailureCheck(result)
    return 




