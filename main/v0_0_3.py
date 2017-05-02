import random, time, threading, sys, math, winsound

def main():
    print ("hello world")

if __name__ == '__main__':
    None

##version 0.0.3
version = '0.0.3'
author = 'Pedololicon'
print("Project101, \nVersion", version, "\nAuthor:", author, "\n\nWelcome to (unnamed game). Help is accessed with number 0 as input.")
time.sleep(0.1)
##Trying to make a simple text-based adventure game

#Global triggers
enemyDeathCounter = 0
heroDeathCounter = 0
combatOn = 0

#Variables
defenseReductionMultiplier = 0.06  #Every point of defense is equal to 6% effective HP increase. Shamelessly copied from wc3 and dota. Due to change in the future.
speedModifier = 0.01  #Changes combat speed, higher = slower

#Base stats
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
        
hero = stats('placeholder', 100, 100, 10, 0, 1, 0, 100, 1, 'none')
dummy = stats('COMBAT PlACEHOLDER TARGET', 'CURRENT HP', 'MAX HP', 'ATTACK', 'DEFENCE', 'SPEED', 'EXP', 'MAXEXP', 'LEVEL', 'PLACEHOLDERWEAPON')

#Items
class weapons(object):
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

none = weapons('none', 0)
stick = weapons('stick', 1)
pitchfork = weapons('pitchfork', 2)
rustySword = weapons('rusty sword', 4)

#Strings
line = "---------------------------------------------"
q1 = "\nChoose a name for your character"
str1 = "You are awaken by the stench of rotten corpses. You can't remember anything. \nThe unfamiliar surroundings confuses you, but you must get out of here."
str2 = "You continue your adventure."

#Functions
def gameHelp():
    print('\nCurrent RNG: Explore - 60% combat, 10% encounter, 10% story, 10% event, 10% loot;\nRest - 7.5% combat, 5% encounter, 87.5% heal.')
    return

#Main interface
options = {'explore':1, 'rest':2, 'check stats':9, 'help':0}

def askAdventure(question, *args):  #
    print (question)
    optionGiven = {}
    while True:
        if args:
            print ("---------------------------------------------\nWhat is your next action?")
            for num, arg in enumerate(args):
                optionGiven[arg] = options.get(arg)
                print( '%s. %s' % (optionGiven[arg], arg) )
            print('---------------------------------------------')
        ans = input()
        print('---------------------------------------------')
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
    print ('Name:', hero.name, ' Level', hero.level, 'exp:', '%s/%s' % (hero.exp, hero.maxExp), '\nHP:', math.ceil(hero.currentHP), '/', math.ceil(hero.maxHP), '\nAttack', hero.attack, 'Defence', hero.defence, 'Speed', hero.speed, '\nCurrent weapon: ', hero.weapon,)
    
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
        loot()
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
            elif hero.level < 6:
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
    print('You are in combat with', dummy.name, '\n---------------------------------------------')
    threading.Thread(target = heroAttack).start()
    threading.Thread(target = enemyAttack).start()
    return

def heroAttack():
    global enemyDeathCounter
    global heroDeathCounter
    global combatOn
    while heroDeathCounter == 0:
        if dummy.currentHP <= 0:
            enemyDeathCounter = 1
            print(dummy.name, 'has been defeated. You are victorious!')
            hero.exp += dummy.exp
            lvlupCheck()
            time.sleep(1)
            combatOn = 0
            break
        else:
            damageDone = math.floor(hero.attack * (1 - (dummy.defence * defenseReductionMultiplier) / (1 + defenseReductionMultiplier)))
            dummy.currentHP -= damageDone
            if dummy.currentHP <= 0:
                print (hero.name, 'hit', dummy.name, 'for', round(damageDone, 1), 'points! HP:', '(%s/%s)' % (0, math.ceil(dummy.maxHP)))
            else:
                print(hero.name, 'hit', dummy.name, 'for', round(damageDone, 1), 'points! HP:', '(%s/%s)' % (math.ceil(dummy.currentHP), math.ceil(dummy.maxHP)))
                time.sleep(speedModifier / hero.speed)
    return

def enemyAttack():
    global enemyDeathCounter
    global heroDeathCounter
    global combatOn
    while enemyDeathCounter == 0:
        if hero.currentHP <= 0:
            heroDeathCounter = 1
            combatOn = 0
            print(hero.name, 'has fallen')
            break
        else:
            damageDone = math.floor(dummy.attack * (1 - (hero.defence * defenseReductionMultiplier) / (1 + defenseReductionMultiplier)))
            hero.currentHP -= damageDone
            if hero.currentHP <= 0:
                print (dummy.name, 'hit you for', round(damageDone, 1), 'points! HP:', '(%s/%s)' % (0, math.ceil(hero.maxHP)))
            else:            
                print(dummy.name, 'hit you for', round(damageDone, 1), 'points! HP:', '(%s/%s)' % (math.ceil(hero.currentHP), math.ceil(hero.maxHP)))
                time.sleep(speedModifier / dummy.speed)
    return    
    
def lvlupCheck():
    if hero.exp >= hero.maxExp:
        hero.exp -= hero.maxExp
        hero.maxExp = math.ceil(hero.maxExp ** 1.14)
        hero.level += 1
        hero.currentHP += 10
        hero.maxHP += 10
        hero.attack += 1
        hero.defence += 1
        print('---------------------------------------------\nYou have leveled up!\n---------------------------------------------')
        time.sleep(1)
        checkStats()
    return
    
def encounter():
    print('encounter function was called')
    return

def event():
    print('event function was called')
    return

def story():
    print('story function was called')
    return

def loot():
    print('loot function was called')
    return

def bgm():
    winsound.PlaySound('2.wav', winsound.SND_LOOP)
    return


#Start of I/O
threading.Thread(target = bgm).start()  #Testing sound

hero.name = askAdventure(q1)
askAdventure(str1, 'explore', 'rest', 'check stats', 'help')
time.sleep(1)
while True:
    while combatOn == 0 and heroDeathCounter == 0: 
        askAdventure(str2, 'explore', 'rest', 'check stats', 'help')
        time.sleep(1)