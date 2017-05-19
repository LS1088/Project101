import random
import time
import sys
import math
import winsound
import numpy
from colorama import init, Fore, Back, Style
from classes import *
from strings import *


'''
TRIGGERS, VARIABLES AND SETTINGS
'''
################################################################################
init(convert=True, autoreset=False)     #Colorama settings for CLI output
expMultiplier = 1   #Amount of exp gained. 1 = Base amount.
defenceReductionMultiplier = 0.06   #Every point of defence is equal to 6% effective HP
# increase. (Same with wc3 and dota) Due to change in the future.
speedMultiplier = 1     #Changes general speed, higher = slower. Do not set to 0.
combatSpeedMultiplier = 0.5     #Combat speed mult. Do not set to 0.
lootChance = 1      #Chance of calling loot function after combat victory. 1 = Always, 0 = Never.
gold = 0
enemyDeathCounter = 0
heroDeathCounter = 0
combatOn = 0
options = {'explore': 1, 'rest': 2, 'shop': 7, 'inventory': 8, 'check stats': 9, 'help': 0}
################################################################################
version = '0.0.8'
author = 'ls1088'
print(Fore.GREEN + Style.BRIGHT + "Project101, \nVersion", version, "\nAuthor:", author, infoStr + Fore.RESET + Style.RESET_ALL, greetingStr)
time.sleep(0.1)
################################################################################
#DEBUGGING SETTINGS
options = {'explore': 1, 'rest': 2, 'inventory': 8, 'check stats': 9, 'help': 0}
expMultiplier = 1
speedMultiplier = 1
combatSpeedMultiplier = 0.5
lootChance = 1
inventory = {'giant hammer':1, 'potion':1, 'strong potion':1}
if expMultiplier != 1 or speedMultiplier !=1 or combatSpeedMultiplier != 0.5 or lootChance != 1 or len(inventory) != 0:
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nWARNING: CUSTOM SETTINGS DETECTED.")
    if expMultiplier != 1:
        print ("Exp multiplier:", expMultiplier)
    if speedMultiplier != 1:
        print ("Speed multiplier:", speedMultiplier)
    if combatSpeedMultiplier != 0.5:
        print ("Combat speed multiplier:", combatSpeedMultiplier)
    if lootChance != 1:
        print ("Loot chance:", lootChance)
    if len(inventory) != 0:
        print ("Starting inventory:", inventory) 
    print (Fore.RESET + Back.RESET + Style.RESET_ALL)
################################################################################


'''
FUNCTIONS
'''
#Main interface
def askAdventure(question, *args):  
    print (question)
    optionGiven = {}
    while True:
        if args:
            print ('%s\n%s' % (line, 'What is your next action?'))
            for arg in args:
                optionGiven[arg] = options.get(arg)
                print( '%s. %s' % (optionGiven[arg], arg) )
            print(line)
        ans = input()
        beepSound()
        print(line)
        if args:
            if ans.isdigit():
                ans = int(ans)
            if 'explore' in args and (ans == optionGiven['explore'] or ans == 'explore'):
                explore()
                break
            elif 'rest' in args and (ans == optionGiven['rest'] or ans == 'rest'):
                rest()
                break
            elif 'shop' in args and (ans == optionGiven['shop'] or ans == 'shop'):
                shop()
                break
            elif 'inventory' in args and (ans == optionGiven['inventory'] or ans == 'inventory'):
                checkInventory()
            elif 'check stats' in args and (ans == optionGiven['check stats'] or ans == 'check stats'):
                checkStats()
            elif 'help' in args and (ans == optionGiven['help'] or ans == 'help'):
                gameHelp()
            else:
                print('Please enter a valid input.')
        else:
            break
    return ans

def checkStats():
    print('Name:', hero.name, 
          ' Level', hero.level, 'exp:', '%s/%s' % (hero.exp, hero.maxExp), 
          '\nHP:', math.ceil(hero.currentHP), '/', math.ceil(hero.maxHP),
          '\nAttack', '%s(+%s)' % (hero.attack - hero.weapon.attack, hero.weapon.attack), 
          'Defence', '%s(+%s)' % (hero.defence - hero.weapon.defence, hero.weapon.defence), 
          'Speed', hero.speed, 
          '\nCurrent weapon:', Fore.YELLOW + Style.BRIGHT + hero.weapon.name + Fore.RESET + Style.RESET_ALL, 
          '\nWeapon attack:', hero.weapon.attack, 
          'Weapon defence:', hero.weapon.defence, 
          'Special Effect:', hero.weapon.specialEffect)
    print(continueStr)
    input()
    
def gameHelp():
    print(helpStr)
    print(continueStr)
    input()
    
def explore():
    randomNumber = random.random()
    if randomNumber < 0.6:
        combat('random')
    elif randomNumber < 0.7:
        encounter()
    elif randomNumber < 0.8:
        event()
    elif randomNumber < 0.9:
        story()
    else:
        loot(hero.level, 'exploreLoot')
    
def rest():
    randomNumber = random.random()
    if randomNumber < 0.6:
        combat('random')
    elif randomNumber < 0.7:
        encounter()
    else:
        restHeal()

def restHeal():
    healAmount = random.randrange(int(round(hero.maxHP - hero.currentHP) / 3 + 1)) + 10
    hero.currentHP += healAmount
    if hero.currentHP >= hero.maxHP:
        hero.currentHP = hero.maxHP
        print('You are at full health!', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))
    else:
        print('You healed for', healAmount, 'points, ', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))

#COMBAT MECHANICS
def combat(enemy):
    global enemyDeathCounter, heroDeathCounter, combatOn      
    enemyDeathCounter = 0
    heroDeathCounter = 0
    combatOn = 1    
    availEnemyList = []
    availEnemyAppearRate = []         
    if enemy == 'random':       #Weighted random choice
        for i in enemyAppearRateDict:
            if enemyNameDict[i].level <= hero.level + 1 and enemyNameDict[i].level >= hero.level - 3:
                availEnemyList.append(i)
                availEnemyAppearRate.append(enemyAppearRateDict[i])
        availEnemyAppearRate_Total = sum(availEnemyAppearRate)
        for i in enumerate(availEnemyAppearRate):
            availEnemyAppearRate[list(i)[0]] = availEnemyAppearRate[list(i)[0]] / availEnemyAppearRate_Total
        combat(enemyNameDict[numpy.random.choice(availEnemyList, p = availEnemyAppearRate)])
    else:       #Combat
        dummy.__dict__ = enemy.__dict__.copy()
        print('%s %s' % ('You are in combat with', Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + dummy.name + Fore.RESET + Back.RESET + Style.RESET_ALL))
        heroAttackInterval = speedMultiplier * combatSpeedMultiplier / hero.speed
        enemyAttackInterval = speedMultiplier * combatSpeedMultiplier / dummy.speed
        while heroDeathCounter == 0 and enemyDeathCounter == 0:
            if heroAttackInterval < enemyAttackInterval:        #Hero attacks
                time.sleep(heroAttackInterval)
                damageDone = math.floor((random.uniform(-0.15, 0.15) + 1) * (random.uniform(-1, 1) + hero.attack) * (1 - (dummy.defence * defenceReductionMultiplier) / (1 + defenceReductionMultiplier)))
                dummy.currentHP -= damageDone
                damageDone = (Fore.RED + Style.BRIGHT + str(damageDone) + Fore.RESET + Style.RESET_ALL)
                if dummy.currentHP <= 0:        #Victory
                    print (hero.name, 'hit', dummy.name, 'for', damageDone, 'points! HP:', '(%s/%s)' % (0, math.ceil(dummy.maxHP)))
                    enemyDeathCounter = 1
                    print(dummy.name, 'has been defeated. You are victorious!')
                    if random.random() <= lootChance:
                        loot(dummy.level, 'combatLoot')
                    hero.exp += (dummy.exp * expMultiplier)
                    lvlupCheck()
                    combatOn = 0
                    break                     
                else:
                    print(hero.name, 'hit', dummy.name, 'for', damageDone, 'points! HP:', '(%s/%s)' % (math.ceil(dummy.currentHP), math.ceil(dummy.maxHP)))
                    time.sleep(heroAttackInterval) 
                enemyAttackInterval -= heroAttackInterval
                heroAttackInterval = speedMultiplier * combatSpeedMultiplier / hero.speed
            elif heroAttackInterval > enemyAttackInterval:          #Enemy Attacks
                time.sleep(enemyAttackInterval)
                damageDone = math.floor((random.uniform(-0.15, 0.15) + 1) * (random.uniform(-1, 1) + dummy.attack) * (1 - (hero.defence * defenceReductionMultiplier) / (1 + defenceReductionMultiplier)))
                hero.currentHP -= damageDone
                damageDone = (Fore.RED + Style.BRIGHT + str(damageDone) + Fore.RESET + Style.RESET_ALL)
                if hero.currentHP <= 0:         #Defeat
                    print (dummy.name, 'hit you for', damageDone, 'points! HP:', '(%s/%s)' % (0, math.ceil(hero.maxHP)))
                    heroDeathCounter = 1
                    combatOn = 0
                    print(hero.name, 'has fallen')
                    print(restartStr)
                    input()
                    winsound.Beep(900, 200)
                    main()                    
                else:            
                    print(dummy.name, 'hit you for', damageDone, 'points! HP:', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))
                    time.sleep(enemyAttackInterval)               
                heroAttackInterval -= enemyAttackInterval
                enemyAttackInterval = speedMultiplier * combatSpeedMultiplier / dummy.speed
            else:
                if random.random() < 0.5:
                    heroAttackInterval += 0.01
                else:
                    enemyAttackInterval += 0.01 

def lvlupCheck():
    if hero.exp >= hero.maxExp:
        hero.exp -= hero.maxExp
        hero.maxExp = math.ceil ( math.lgamma ( hero.maxExp / 4.7 + 55) )
        hero.level += 1
        hero.currentHP += 10
        hero.maxHP += 10
        hero.attack += 1
        hero.defence += 1
        print('%s\n%s\n%s' % (line, Fore.GREEN + Back.GREEN + Style.BRIGHT + 'You have leveled up! ' + str(int(hero.level) - 1) + ' ---> ' + str(hero.level) + Fore.RESET + Back.RESET + Style.RESET_ALL, line))
        time.sleep(speedMultiplier)
        checkStats()

#EVENTS
def encounter():
    print(Fore.RED+"DebugLog - encounter function was called"+Fore.RESET)

def event():
    randomNumber = random.random()
    if randomNumber < 0.99:
        shop()
    else:
        print(Fore.RED+"DebugLog - event function was called"+Fore.RESET)

def story():
    print(Fore.RED+"DebugLog - story function was called"+Fore.RESET)

def shop():
    randomNumber = random.random()
    if randomNumber < 0.6:
        print(shopStr1)
    elif randomNumber < 0.9:
        print(shopStr2)
    else:
        print(shopStr3)

#ITEM MECHANICS
def loot(lootLevel, lootMessage):
    availDropList = []
    availDropRate = []    
    global gold
    #weighted random choice
    if random.random() < 0.33 and lootMessage == 'exploreLoot':
        goldGained = random.randrange(10 + 2*lootLevel, 20 + 3*lootLevel)
        print("You found a treasure chest containing" + Fore.YELLOW + Style.BRIGHT, goldGained, Fore.RESET + Style.RESET_ALL + "gold.")
        gold += goldGained    
        return
    elif random.random() < 0.66 and lootMessage == 'combatLoot':
        goldGained = random.randrange(1 + lootLevel, 10 + 2*lootLevel)
        print("Your enemy dropped" + Fore.YELLOW + Style.BRIGHT, goldGained, Fore.RESET + Style.RESET_ALL + "gold.")
        gold += goldGained         
        time.sleep(speedMultiplier)
    if random.random() < 0.5:
        for i in hpPotionDropDict:
            if hpPotionNameDict[i].level <= lootLevel:
                availDropList.append(i)
                availDropRate.append(hpPotionDropDict[i])
        availDropRateTotal = sum(availDropRate)
        for i in enumerate(availDropRate):
            availDropRate[list(i)[0]] = availDropRate[list(i)[0]] / availDropRateTotal
        droppedItem = numpy.random.choice(availDropList, p = availDropRate)   
    else:
        for i in weaponDropDict:
            if weaponNameDict[i].level <= lootLevel:
                availDropList.append(i)
                availDropRate.append(weaponDropDict[i])
        availDropRateTotal = sum(availDropRate)
        for i in enumerate(availDropRate):
            availDropRate[list(i)[0]] = availDropRate[list(i)[0]] / availDropRateTotal
        droppedItem = numpy.random.choice(availDropList, p = availDropRate)   
    if droppedItem == 'none':
        if lootMessage == 'exploreLoot':
            randomNumber = random.random()
            if randomNumber < 0.3333:
                print ('You stumbled upon a treasure chest... but it is empty.')
            elif randomNumber < 0.6666:
                print ('You wasted your time by walking around aimlessly.')
            else:
                print ('You dig in a pile of debris only finding unusable items.')
    else:
        if lootMessage == 'combatLoot':
            print ('%s %s%s' % ('Your enemy dropped' + Fore.YELLOW + Style.BRIGHT, droppedItem, Fore.RESET + Style.RESET_ALL + '.'))
        elif lootMessage == 'exploreLoot':
            print ('You stumbled upon a dead body and found', Fore.YELLOW + Style.BRIGHT + droppedItem + Fore.RESET + Style.RESET_ALL)       
        if droppedItem in inventory.keys():
            inventory[droppedItem] += 1
        else:
            inventory[droppedItem] = 1
        time.sleep(speedMultiplier)

def checkInventory():
    useItem = 'placeholdertext'
    itemCheckTrigger = 0
    print("Inventory")
    print(line)
    print("Gold:", gold)
    if len(inventory) == 0:
        print("You don't have any items.")
    else:
        for key, value in inventory.items():
            if itemNameDict[key].__class__ == hpPotion:
                print(value, "X", Fore.YELLOW + Style.BRIGHT + itemNameDict[key].name + Fore.RESET + Style.RESET_ALL, end = " | ")
                print('HP recovery', itemNameDict[key].hpHeal)
            elif itemNameDict[key].__class__ == weapons:
                print(value, "X", Fore.YELLOW + Style.BRIGHT + itemNameDict[key].name + Fore.RESET + Style.RESET_ALL, end = " | ")
                print('Attack', itemNameDict[key].attack, 'Defence:', itemNameDict[key].defence, 'Special Effect:', itemNameDict[key].specialEffect)
        print(line)
        print("Enter the name of the item you wish to use. Input nothing to go back.")
        while useItem != '':
            useItem = input()
            for key, value in inventory.items():
                itemCheckTrigger = 0
                if useItem == key:
                    if key in hpPotionNameDict:
                        hero.currentHP += itemNameDict[key].hpHeal
                        if hero.currentHP >= hero.maxHP:
                            hero.currentHP = hero.maxHP
                            print("You recovered", itemNameDict[key].hpHeal, "points of hp to full health!", '(%s/%s)' % (hero.maxHP, hero.maxHP) )
                        else:
                            print("You recovered", itemNameDict[key].hpHeal, "points of hp.", '(%s/%s)' % (hero.currentHP, hero.maxHP) )
                    elif key in weaponNameDict:
                        hero.attack -= hero.weapon.attack
                        hero.defence -= hero.weapon.defence
                        if hero.weapon.name != 'none':
                            if hero.weapon.name in inventory.keys():
                                inventory[hero.weapon.name] += 1
                            else:
                                inventory[hero.weapon.name] = 1
                            print(Fore.YELLOW + Style.BRIGHT + hero.weapon.name + Fore.RESET + Style.RESET_ALL, "was unequiped.", end = " ")
                        hero.weapon = itemNameDict[key]
                        hero.attack += itemNameDict[key].attack
                        hero.defence += itemNameDict[key].defence
                        print(Fore.YELLOW + Style.BRIGHT + key + Fore.RESET + Style.RESET_ALL, "was equipped.")
                    inventory[key] -= 1
                    if inventory[key] == 0:
                        del inventory[key]
                    itemCheckTrigger = 1
                    break
            if useItem != '' and itemCheckTrigger == 0:
                print("No such item exists in your inventory.")
                        
#SOUND
def bgm():
    winsound.PlaySound('BGM.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    return

def beepSound():
    winsound.Beep(900, 125)
    return


'''
RUNTIME
'''
def main():
    bgm() #Testing sound
    hero.name = askAdventure('%s\n%s' % (line, question1))
    askAdventure(storyStr1, 'explore', 'rest', 'inventory', 'check stats', 'help')
    time.sleep(speedMultiplier)
    while True:
        while combatOn == 0 and heroDeathCounter == 0: 
            askAdventure(str1, 'explore', 'rest', 'inventory', 'check stats', 'help')
            time.sleep(speedMultiplier * 0.5)
            
if __name__ == '__main__':
    main()