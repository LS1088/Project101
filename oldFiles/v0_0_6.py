import random, time, threading, sys, math, winsound, numpy
from colorama import init, Fore, Back, Style
init(convert=True, autoreset=False)

version = '0.0.6'
author = 'ls1088'
print(Fore.GREEN + Style.BRIGHT + "Project101, \nVersion", version, "\nAuthor:", author, "\nBGM: Hatsune Miku - (UNICODEPLACEHOLDER).\nCurrent combat system is fully automatic." + Fore.RESET + Style.RESET_ALL + "\n\nWelcome to (unnamed game)")
time.sleep(0.1)

'''
TRIGGERS, VARIABLES AND SETTINGS
'''
###################################
expMultiplier = 1
#Amount of exp gained. 1 = Base amount.
defenceReductionMultiplier = 0.06   
#Every point of defence is equal to 6% effective HP increase. (Same with wc3 and dota) Due to change in the future.
speedModifier = 1
#Changes combat speed, higher = slower. Value being set too low could result in garbled text output.
lootChance = 1
#Chance of calling loot function after combat victory. 1 = Always, 0 = Never.
enemyDeathCounter = 0
heroDeathCounter = 0
combatOn = 0
options = {'explore': 1, 'rest': 2, 'inventory': 8, 'check stats': 9, 'help': 0}
weaponDropDic = {}
weaponNameDic = {}
hpPotionDropDic = {}
hpPotionNameDic = {}
itemNameDic = {}
inventory = {}
###########################################
#Debugging/testing settings
options = {'explore': 1, 'rest': 2, 'inventory': 8, 'check stats': 9, 'help': 0}
expMultiplier = 100
inventory = {'stick': 100, 'minor potion':3}
speedModifier = 0.1
lootChance = 1

if expMultiplier != 1 or speedModifier !=1 or lootChance != 1 or len(inventory) != 0:
    print(Fore.RED, Style.BRIGHT, "\nWARNING: CUSTOM SETTINGS DETECTED. Exp multiplier:", expMultiplier, "Combat speed:", speedModifier, "Loot chance:", lootChance, "Starting inventory:", inventory, Fore.RESET, Style.RESET_ALL)


'''
CLASSES
'''
class hpPotion():
    def __init__(self, name, hpHeal, dropRate, level):
        self.name = name
        self.hpHeal = hpHeal
        self.dropRate = dropRate
        self.level = level
        hpPotionDropDic[self.name] = self.dropRate
        hpPotionNameDic[name] = self
        itemNameDic[name] = self
        
none = hpPotion('none', 0, 10000, 1)
minorPotion = hpPotion('minor potion', 15, 5000, 1)
lesserPotion = hpPotion('lesser potion', 20, 3500, 2)
smallPotion = hpPotion('small potion', 25, 2750, 4)
potion = hpPotion('potion', 30, 2250, 5)
strongPotion = hpPotion('strong potion', 40, 1625, 7)
largePotion = hpPotion('large potion', 50, 1250, 8)
elixirOfLife = hpPotion('elixir of life', 1000000, 100, 1)

class weapons():
    def __init__(self, name, attack, defence, specialEffect, dropRate, level):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.specialEffect = specialEffect
        self.dropRate = dropRate
        self.level = level
        weaponDropDic[self.name] = self.dropRate
        weaponNameDic[name] = self
        itemNameDic[name] = self
    
none = weapons('none', 0, 0, 'none', 10000, 0)

stick = weapons('stick', 1, 0, 'none', 4000, 1)
wand = weapons('wand', 1, 0, 'magic1', 1800, 3)
oakWand = weapons('oak wand', 1, 0, 'magic2', 400, 6)

rustySword = weapons('rusty sword', 2, 1, 'block', 3000, 2)
ironSword = weapons('iron sword', 5, 1, 'block', 1000, 4)
steelSword = weapons('steel sword', 6, 2, 'block', 400, 6)

rustyDagger = weapons('rusty dagger', 2, 0, 'assassination', 2000, 3)
ironDagger = weapons('iron dagger', 3, 0, 'assassination', 1000, 4)
steelDagger = weapons('steel dagger', 4, 0, 'assassination', 450, 6)

hatchet = weapons('hatchet', 4, 0, 'none', 1800, 3)
ironAxe = weapons('iron axe', 6, 0, 'none', 700, 5)
steelAxe = weapons('steel axe', 8, 0, 'none', 300, 7)

ironGreatsword = weapons('iron greatsword', 6, 2, 'block', 800, 5)
steelGreatsword = weapons('steel greatsword', 8, 3, 'block', 200, 8)

shortBow = weapons('short bow', 3, 0, 'ranged attack', 3000, 2)
huntingBow = weapons('hunting bow', 5, 0, 'ranged attack', 800, 5)
compositeBow = weapons('composite bow', 7, 0, 'ranged attack', 250, 8)
longBow = weapons('long bow', 10, 0, 'ranged attack', 150, 9)
recurveBow = weapons('recurve bow', 13, 0, 'ranged attack', 100, 10)

hammer = weapons('hammer', 6, 0, 'stagger', 1000, 4)
sledgeHammer = weapons('sledge hammer', 10, 0, 'stagger', 350, 7)
giantHammer = weapons('giant hammer', 15, 0, 'stunning attack', 100, 10)

pitchfork = weapons('pitchfork', 1, 1, 'none', 3333, 1)
ironSpear = weapons ('iron spear', 4, 1, 'none', 2000, 3)
staff = weapons('staff', 3, 2, 'magic1', 1600, 4)
    
class armor ():
    pass

class stats():
    def __init__(self, name, currentHP, maxHP, attack, defence, speed, exp, maxExp, level, weapon):
        self.name = name
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.exp = exp
        self.maxExp = maxExp
        self.level = level
        self.weapon = weapon

hero = stats('placeholder', 100, 100, 10, 0, 1, 0, 100, 1, none)
dummy = stats('COMBAT PlACEHOLDER TARGET', 'CURRENT HP', 'MAX HP', 'ATTACK', 'DEFENCE', 'SPEED', 'EXP', 'MAXEXP', 'LEVEL', 'PLACEHOLDERWEAPON')
greenSlime = stats('green slime', 20, 20, 5, 0, 0.66, 20, 2**31-1, 1, 'none')
bat = stats('bat', 25, 25, 7, 1, 1.19, 40, 2**31-1, 1, 'none')
yellowSlime = stats('yellow slime', 35, 35, 10, 1, 0.69, 40, 2**31-1, 2, 'none')
giantCrab = stats('giant crab', 60, 60, 15, 4, 0.49, 75, 2**31-1, 4, 'none')
wolf = stats('wolf', 50, 50, 12, 1, 1.6, 100, 2**31-1, 5, 'none')
redSlime = stats('red slime', 80, 80, 22, 2, 0.76, 150, 2**31-1, 6, 'none')
direWolf = stats('dire wolf', 75, 75, 14, 1, 1.7, 220, 2**31-1, 7, 'none')
vampire = stats('vampire', 130, 130, 21, 3, 1.3, 300, 2**31-1, 8, 'none')
greenDragon = stats('green dragon', 110, 100, 30, 6, 0.901, 440, 2**31-1, 9, 'none')
kingSlime = stats('king slime', 300, 300, 40, 2, 0.81, 600, 2**31-1, 9, 'none')
redDragon = stats('red dragon', 200, 200, 60, 12, 0.921, 1200, 2**31-1, 10, 'none')


'''
STRINGS
'''
line = "--------------------------------------------------------------------------------"
q1 = "Choose a name for your character"
str1 = "You are awaken by the stench of rotten corpses. You can't remember anything. \nThe unfamiliar surroundings confuses you, but you must get out of here."
str2 = '%s\n%s' % (line, "You continue your adventure.")


'''
FUNCTIONS
'''
#Main interface
def askAdventure(question, *args):  #
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
                if 'explore' in args and ans == optionGiven['explore']:
                    explore()
                    break
                elif 'rest' in args and ans == optionGiven['rest']:
                    rest()
                    break
                elif 'inventory' in args and ans == optionGiven['inventory']:
                    checkInventory()
                elif 'check stats' in args and ans == optionGiven['check stats']:
                    checkStats()
                elif 'help' in args and ans == optionGiven['help']:
                    gameHelp()
                else:
                    print('Please enter a valid input.')
            elif ans == 'explore' and 'explore' in args:
                explore()
                break
            elif ans == 'rest' and 'rest' in args:
                rest()
                break
            elif ans == 'inventory' and 'inventory' in args:
                checkInventory()
            elif ans == 'check stats' and 'check stats' in args:
                checkStats()
            elif ans == 'help' and 'help' in args:
                gameHelp()
            else:
                print('Please enter a valid input.')
        else:
            break
    return ans

def checkStats():
    print('Name:', hero.name, ' Level', hero.level, 'exp:', '%s/%s' % (hero.exp, hero.maxExp), '\nHP:', math.ceil(hero.currentHP), '/', math.ceil(hero.maxHP)) 
    print('\nAttack', '%s(+%s)' % (hero.attack - hero.weapon.attack, hero.weapon.attack), 'Defence', '%s(+%s)' % (hero.defence - hero.weapon.defence, hero.weapon.defence), 'Speed', hero.speed, '\nCurrent weapon:', Fore.YELLOW + Style.BRIGHT + hero.weapon.name + Fore.RESET + Style.RESET_ALL, '\nWeapon attack:', hero.weapon.attack, 'Weapon defence:', hero.weapon.defence, 'Special Effect:', hero.weapon.specialEffect)
    print(Fore.GREEN + Style.BRIGHT + "Press enter to continue..." + Fore.RESET + Style.RESET_ALL)
    input()
    
def gameHelp():
    print('Defeat enemies in combat in order to gain exp and items. Currently most weapons only start dropping when you reach a certain level.')
    print('\nCurrent RNG: Explore - 60% combat, 10% encounter, 10% story, 10% event, 10% loot;\nRest - 7.5% combat, 5% encounter, 87.5% heal.')
    print(Fore.GREEN + Style.BRIGHT + "Press enter to continue..." + Fore.RESET + Style.RESET_ALL)
    input()
    
def explore():
    randomNumber = random.randrange(10000)
    if randomNumber < 6000:
        combatSelect('random')
    elif randomNumber < 7000:
        encounter()
    elif randomNumber < 8000:
        event()
    elif randomNumber < 9000:
        story()
    else:
        loot(hero.level, 'exploreLoot')
    return
    
def rest():
    randomNumber = random.random()
    if randomNumber < 0.6:
        combatSelect('random')
    elif randomNumber < 0.7:
        encounter()
    else:
        restHeal()
    return

def restHeal():
    healAmount = random.randrange(int(round(hero.maxHP - hero.currentHP) / 3 + 1)) + 10
    hero.currentHP += healAmount
    if hero.currentHP >= hero.maxHP:
        hero.currentHP = hero.maxHP
        print('You are at full health!', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))
    else:
        print('You healed for', healAmount, 'points, ', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))
    return

#combat section
def combatSelect(enemy):
    if enemy == 'random':
        randomNumber = random.randrange(10000)
        if randomNumber < 2000:
            combatSelect(bat)
        elif randomNumber < 3000 and hero.level > 1:
            combatSelect(yellowSlime)
        elif randomNumber < 4000 and hero.level > 3:
            combatSelect(giantCrab)
        elif randomNumber < 5000 and hero.level > 5:
            combatSelect(wolf)
        elif randomNumber < 6000 and hero.level > 6:
            combatSelect(redSlime)
        elif randomNumber < 7000 and hero.level > 7:
            combatSelect(direWolf)
        elif randomNumber < 8000 and hero.level > 7:
            combatSelect(vampire)
        elif randomNumber < 9000 and hero.level > 8:
            combatSelect(greenDragon)
        elif randomNumber < 9500 and hero.level > 9:
            combatSelect(kingSlime)
        elif randomNumber < 10000 and hero.level > 10:
            combatSelect(redDragon)        
        else:
            if hero.level < 4:
                combatSelect(greenSlime)
            elif hero.level <= 5:
                combatSelect(bat)
            elif hero.level <= 6:
                combatSelect(giantCrab)
            else:
                combatSelect(wolf)
    else:
        combat(enemy)
    return

def combat(enemy):
    global enemyDeathCounter
    global heroDeathCounter
    global combatOn
    enemyDeathCounter = 0
    heroDeathCounter = 0
    combatOn = 1
    dummy.__dict__ = enemy.__dict__.copy()
    print('%s %s' % ('You are in combat with', dummy.name))
    time.sleep(speedModifier)
    #dummy.name = (Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + dummy.name + Fore.RESET + Back.RESET + Style.RESET_ALL)
    randomBoolean = random.randrange(2)
    if randomBoolean == 0:
        threading.Thread(target = heroAttack).start()
        time.sleep(0.05)
        threading.Thread(target = enemyAttack).start()
    else:
        threading.Thread(target = enemyAttack).start()
        time.sleep(0.05)
        threading.Thread(target = heroAttack).start()        
    return

def heroAttack():
    global enemyDeathCounter
    global heroDeathCounter
    global combatOn
    while heroDeathCounter == 0:
        if dummy.currentHP <= 0:  ##Victory
            enemyDeathCounter = 1
            print(dummy.name, 'has been defeated. You are victorious!')
            if random.random() <= lootChance:
                loot(dummy.level, 'combatLoot')
            hero.exp += (dummy.exp * expMultiplier)
            lvlupCheck()
            combatOn = 0
            break
        else:
            damageDone = math.floor(hero.attack * (1 - (dummy.defence * defenceReductionMultiplier) / (1 + defenceReductionMultiplier)))
            dummy.currentHP -= damageDone
            damageDone = (Fore.RED + Style.BRIGHT + str(damageDone) + Fore.RESET + Style.RESET_ALL)
            if dummy.currentHP <= 0:
                print (hero.name, 'hit', dummy.name, 'for', damageDone, 'points! HP:', '(%s/%s)' % (0, math.ceil(dummy.maxHP)))
            else:
                print(hero.name, 'hit', dummy.name, 'for', damageDone, 'points! HP:', '(%s/%s)' % (math.ceil(dummy.currentHP), math.ceil(dummy.maxHP)))
                time.sleep(speedModifier / hero.speed)
    return

def enemyAttack():
    global enemyDeathCounter
    global heroDeathCounter
    global combatOn
    while enemyDeathCounter == 0:
        if hero.currentHP <= 0:  ##Defeat
            heroDeathCounter = 1
            combatOn = 0
            print(hero.name, 'has fallen')
            print('%s\n%s\n%s\n' % (line, Fore.GREEN + Style.BRIGHT + "Press enter to restart the game." + Fore.RESET + Style.RESET_ALL, line))
            input()
            winsound.Beep(900, 200)
            main()
            break
        else:
            damageDone = math.floor(dummy.attack * (1 - (hero.defence * defenceReductionMultiplier) / (1 + defenceReductionMultiplier)))
            hero.currentHP -= damageDone
            damageDone = (Fore.RED + Style.BRIGHT + str(damageDone) + Fore.RESET + Style.RESET_ALL)
            if hero.currentHP <= 0:
                print (dummy.name, 'hit you for', damageDone, 'points! HP:', '(%s/%s)' % (0, math.ceil(hero.maxHP)))
            else:            
                print(dummy.name, 'hit you for', damageDone, 'points! HP:', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))
                time.sleep(speedModifier / dummy.speed)
    return    
    
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
        time.sleep(speedModifier)
        checkStats()
    return

#Events
def encounter():
    print('encounter function was called')
    return

def event():
    print('event function was called')
    return

def story():
    print('story function was called')
    return

#Item Drop
def loot(lootLevel, lootMessage):
    availDrop = []
    availDropRateUnmodified = []
    availDropRate = []    
    #weighted random choice
    if random.random() < 0.35:
        for i in hpPotionDropDic:
            if hpPotionNameDic[i].level <= lootLevel:
                availDrop.append(i)
                availDropRateUnmodified.append(hpPotionDropDic[i])
        availDropRateUnmodifiedTotal = sum(availDropRateUnmodified)
        for i in availDropRateUnmodified:
            i = i / availDropRateUnmodifiedTotal    
            availDropRate.append(i)
    else:
        for i in weaponDropDic:
            if weaponNameDic[i].level <= lootLevel:
                availDrop.append(i)
                availDropRateUnmodified.append(weaponDropDic[i])
        availDropRateUnmodifiedTotal = sum(availDropRateUnmodified)
        for i in availDropRateUnmodified:
            i = i / availDropRateUnmodifiedTotal
            availDropRate.append(i)
    droppedItem = numpy.random.choice( availDrop, p = availDropRate )
    if droppedItem == 'none':
        if lootMessage == 'exploreLoot':
            print ('You stumbled upon a treasure chest... but it is empty.')
    else:
        if lootMessage == 'combatLoot':
            print ('%s %s %s' % ('You find', Fore.YELLOW + Style.BRIGHT + droppedItem + Fore.RESET + Style.RESET_ALL, 'on the dead body of your enemy.'))
        elif lootMessage == 'exploreLoot':
            print ('You stumbled upon an ancient treasure... and found', Fore.YELLOW + Style.BRIGHT + droppedItem + Fore.RESET + Style.RESET_ALL)
        if droppedItem in inventory.keys():
            inventory[droppedItem] += 1
        else:
            inventory[droppedItem] = 1
    return

def checkInventory():
    useItem = 'placeholdertext'
    itemCheckTrigger = 0
    print("Inventory")
    print(line)
    if len(inventory) == 0:
        print("You don't have any items.")
    else:
        for key, value in inventory.items():
            if itemNameDic[key].__class__ == hpPotion:
                print(value, "X", Fore.YELLOW + Style.BRIGHT + itemNameDic[key].name + Fore.RESET + Style.RESET_ALL, end = " | ")
                print('HP recovery', itemNameDic[key].hpHeal)
            elif itemNameDic[key].__class__ == weapons:
                print(value, "X", Fore.YELLOW + Style.BRIGHT + itemNameDic[key].name + Fore.RESET + Style.RESET_ALL, end = " | ")
                print('Attack', itemNameDic[key].attack, 'Defence:', itemNameDic[key].defence, 'Special Effect:', itemNameDic[key].specialEffect)
        print(line)
        print("Enter the name of the item you wish to use. Input nothing to go back.\n")
        while useItem != '':
            useItem = input()
            for key, value in inventory.items():
                itemCheckTrigger = 0
                if useItem == key:
                    if key in hpPotionNameDic:
                        hero.currentHP += itemNameDic[key].hpHeal
                        if hero.currentHP >= hero.maxHP:
                            hero.currentHP = hero.maxHP
                            print("You recovered", itemNameDic[key].hpHeal, "points of hp to full health!", '(%s/%s)' % (hero.maxHP, hero.maxHP) )
                        else:
                            print("You recovered", itemNameDic[key].hpHeal, "points of hp.", '(%s/%s)' % (hero.currentHP, hero.maxHP) )
                    elif key in weaponNameDic:
                        hero.attack -= hero.weapon.attack
                        hero.defence -= hero.weapon.defence
                        if hero.weapon.name != 'none':
                            if hero.weapon.name in inventory.keys():
                                inventory[hero.weapon.name] += 1
                            else:
                                inventory[hero.weapon.name] = 1
                            print(Fore.YELLOW + Style.BRIGHT + hero.weapon.name + Fore.RESET + Style.RESET_ALL, "was unequiped.", end = " ")
                        hero.weapon = itemNameDic[key]
                        hero.attack += itemNameDic[key].attack
                        hero.defence += itemNameDic[key].defence
                        print(Fore.YELLOW + Style.BRIGHT + key + Fore.RESET + Style.RESET_ALL, "was equipped.")
                    inventory[key] -= 1
                    if inventory[key] == 0:
                        del inventory[key]
                    itemCheckTrigger = 1
                    break
            if useItem != '' and itemCheckTrigger == 0:
                print("No such item exists in your inventory.")
                        
#Sound
def bgm():
    winsound.PlaySound('BGM.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    return

def beepSound():
    winsound.Beep(900, 125)
    return

'''
MAIN I/O
'''
def main():
    bgm() #Testing sound
    hero.name = askAdventure('%s\n%s' % (line, q1))
    askAdventure(str1, 'explore', 'rest', 'inventory', 'check stats', 'help')
    time.sleep(speedModifier)
    while True:
        while combatOn == 0 and heroDeathCounter == 0: 
            askAdventure(str2, 'explore', 'rest', 'inventory', 'check stats', 'help')
            time.sleep(speedModifier)
            
if __name__ == '__main__':
    main()