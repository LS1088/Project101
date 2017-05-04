import random, time, threading, sys, math, winsound, numpy
from colorama import init, Fore, Back, Style
init(convert=True, autoreset=False)

version = '0.0.5'
author = 'ls1088'
print(Fore.GREEN + Style.BRIGHT + "Project101, \nVersion", version, "\nAuthor:", author, "\nBGM: Hatsune Miku - (UNICODEPLACEHOLDER).\nCurrent combat system is fully automatic." + Fore.RESET + Style.RESET_ALL + "\n\nWelcome to (unnamed game). Input either the full text or shortcut number.")
time.sleep(0.1)

'''
TRIGGERS, VARIABLES AND CLASSES
'''
enemyDeathCounter = 0
heroDeathCounter = 0
combatOn = 0
defenseReductionMultiplier = 0.06   
#Every point of defense is equal to 6% effective HP increase. (Same with wc3 and dota) Due to change in the future.
speedModifier = 1.5  
#Changes combat speed, higher = slower
weaponDropDic = {}
weaponObjectNameDic = {}
options = {'explore':1, 'rest':2, 'check stats':9, 'help':0}
inventory = []

class stats(object):
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

class items():
    pass

class weapons(object):
    def __init__(self, name, attack, defense, specialEffect, dropRate, level):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.specialEffect = specialEffect
        self.dropRate = dropRate
        self.level = level
        weaponDropDic[self.name] = self.dropRate
        weaponObjectNameDic[name] = self

none = weapons('none', 0, 0, 'none', 10000, 0)

#one handed
stick = weapons('stick', 1, 0, 'none', 5000, 1)
wand = weapons('wand', 1, 0, 'magic1', 1000, 3)
oakWand = weapons('oak wand', 1, 0, 'magic2', 800, 6)

rustySword = weapons('rusty sword', 2, 1, 'block', 4000, 2)
ironSword = weapons('iron sword', 5, 1, 'block', 1000, 4)
steelSword = weapons('steel sword', 6, 2, 'block', 1000, 6)

rustyDagger = weapons('rusty dagger', 2, 0, 'assassination', 1000, 3)
ironDagger = weapons('iron dagger', 3, 0, 'assassination', 1000, 4)
steelDagger = weapons('steel dagger', 4, 0, 'assassination', 1000, 6)

hatchet = weapons('hatchet', 4, 0, 'none', 1000, 3)
ironAxe = weapons('iron axe', 6, 0, 'none', 1000, 5)
steelAxe = weapons('steel axe', 8, 0, 'none', 1000, 7)

#two handed
ironGreatsword = weapons('iron greatsword', 6, 2, 'block', 1000, 5)
steelGreatsword = weapons('steel greatsword', 8, 3, 'block', 1000, 8)

shortBow = weapons('short bow', 3, 0, 'ranged attack', 1000, 2)
huntingBow = weapons('hunting bow', 5, 0, 'ranged attack', 1000, 5)
compositeBow = weapons('composite bow', 7, 0, 'ranged attack', 1000, 8)
longBow = weapons('long bow', 10, 0, 'ranged attack', 1000, 9)
recurveBow = weapons('recurve bow', 13, 0, 'ranged attack', 1000, 10)

hammer = weapons('hammer', 6, 0, 'stagger', 1000, 4)
sledgeHammer = weapons('sledge hammer', 10, 0, 'stagger', 1000, 7)
giantHammer = weapons('giant hammer', 15, 0, 'stunning attack', 1000, 10)

pitchfork = weapons('pitchfork', 1, 1, 'none', 1000, 1)
ironSpear = weapons ('iron spear', 4, 1, 'none', 1000, 3)
staff = weapons('staff', 3, 2, 'magic1', 1000, 4)

class armor (object):
    pass

#Variables
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
greenDragon = stats('green dragon', 110, 100, 40, 6, 0.901, 440, 2**31-1, 9, 'none')
kingSlime = stats('king slime', 300, 300, 75, 2, 0.81, 600, 2**31-1, 9, 'none')
redDragon = stats('red dragon', 200, 200, 100, 12, 0.921, 1200, 2**31-1, 10, 'none')

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
options = {'explore':1, 'rest':2, 'check stats':9, 'help':0}

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
                if int(ans) == optionGiven['explore']:
                    explore()
                    break                
                elif int(ans) == optionGiven['rest']:
                    rest()
                    break
                elif int(ans) == optionGiven['check stats']:
                    checkStats()
                elif int(ans) == optionGiven['help']:
                    gameHelp()
                else:
                    print('Please enter a valid number.')
            elif ans == 'explore':
                explore()
                break
            elif ans == 'rest':
                rest()
                break
            elif ans == 'check stats':
                checkStats()
            elif ans == 'help':
                gameHelp()
            else:
                print('Please enter a valid input.')
        else:
            break
    return ans

def checkStats():
    print ('Name:', hero.name, ' Level', hero.level, 'exp:', '%s/%s' % (hero.exp, hero.maxExp), '\nHP:', math.ceil(hero.currentHP), '/', math.ceil(hero.maxHP), '\nAttack', hero.attack, 'Defence', hero.defence, 'Speed', hero.speed, '\nCurrent weapon: ', hero.weapon.name,)
    
def gameHelp():
    print('\nCurrent RNG: Explore - 60% combat, 10% encounter, 10% story, 10% event, 10% loot;\nRest - 7.5% combat, 5% encounter, 87.5% heal.')
    return
    
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
    randomNumber = random.randrange(10000)
    if randomNumber < 750:
        combatSelect('random')
    elif randomNumber < 1250:
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
    print('%s %s\n%s' % ('You are in combat with', dummy.name, line))
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
            loot(dummy.level, 'combatLoot')
            hero.exp += dummy.exp
            lvlupCheck()
            time.sleep(1)
            combatOn = 0
            break
        else:
            damageDone = math.floor(hero.attack * (1 - (dummy.defence * defenseReductionMultiplier) / (1 + defenseReductionMultiplier)))
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
            replay = input('%s\n%s\n%s\n' % (line, 'Input anything to restart.', line))
            winsound.Beep(900, 200)
            if replay:
                main()
            break
        else:
            damageDone = math.floor(dummy.attack * (1 - (hero.defence * defenseReductionMultiplier) / (1 + defenseReductionMultiplier)))
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
        print('%s\n%s\n%s' % (line, 'You have leveled up!', line))
        time.sleep(1)
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
    for i in weaponDropDic:
        if weaponObjectNameDic[i].level <= lootLevel:
            availDrop.append(i)
            availDropRateUnmodified.append(weaponDropDic[i])
        availDropRateUnmodifiedTotal = sum(availDropRateUnmodified)
    for i in availDropRateUnmodified:
        i = i / availDropRateUnmodifiedTotal
        availDropRate.append(i)
    droppedItem = numpy.random.choice( availDrop, p = availDropRate )
    if droppedItem == 'none' and lootMessage == 'exploreLoot':
        print ('You stumbled upon a treasure chest... but it is empty.')
    else:
        droppedItem = (Fore.YELLOW + Style.BRIGHT + droppedItem + Fore.RESET + Style.RESET_ALL)
        if lootMessage == 'combatLoot':
            print ('%s %s %s' % ('You find', droppedItem, 'on the dead body of your enemy.'))
        elif lootMessage == 'exploreLoot':
            print ('You stumbled upon an ancient treasure... and found', droppedItem)
        else:
            print ('ERROR: YOU SHOULD NOT SEE THIS MESSAGE')
    return

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
    askAdventure(str1, 'explore', 'rest', 'check stats', 'help')
    time.sleep(1)
    while True:
        while combatOn == 0 and heroDeathCounter == 0: 
            askAdventure(str2, 'explore', 'rest', 'check stats', 'help')
            time.sleep(1)
            
if __name__ == '__main__':
    main()