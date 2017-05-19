# Test
import random

def main():
    print ("hello world")

if __name__ == '__main__':
    None

##version 0.0.1
version = '0.0.1'
author = 'Pedololicon'
print("Project101, \nVersion", version, "\nAuthor:", author, "\n\nWelcome to this simple text-based adventure(unnamed game). Help is accessed with number 0 as input.")
##Trying to make a simple text-based adventure

#Variables
class stats(object):
    def __init__(self, currentHP, maxHP, attack, defence, speed, exp, maxExp, level, weapon):
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.exp = exp
        self.maxExp = maxExp
        self.level = level
        self.weapon = weapon

hero = stats(100, 100, 10, 0, 1, 0, 100, 1, 'Worn out sword')

greenSlime = stats(20, 20, 5, 0, 1, 10, 2**31-1, 1, 'none')

#Strings
q1 = "\nChoose a name for your character"
str1 = "\nYou are awaken by the stench of rotten corpses. You can't remember anything. \nThe unfamiliar surroundings confuses you, but you must get out of here."
str2 = "\nYou continue your adventure."

#Functions
def gameHelp():
    print('\nShortcuts: 1 - explore, 2 - rest, 3 - check stats, 0 - help')
    print('\nCurrent RNG: Explore - 60% combat, 10% encounter, 10% story, 10% event, 10% loot;\nRest - 7.5% combat, 5% encounter, 87.5% heal.')
    return

def askAdventure(question, *args, **kwargs):
    print (question)
    while True:
        if args:
            print ("\nWhat is your next action?")
            for num, ar in enumerate(args):
                print (num+1, ar)
            print('0 help')
        ans = input()
        if args:
            if ans == 'explore' or ans == '1':
                explore()
                break
            elif ans == 'rest' or ans == '2':
                rest()
                break
            elif ans == 'check stats' or ans == '3':
                checkStats()
            elif ans == 'help' or ans == '0':
                gameHelp()            
        else:
            break
    return ans

def checkStats():
    print ('\nName: ', heroName, '\nHP: ', hero.currentHP, '/', hero.maxHP, '\nCurrent weapon: ', hero.weapon, '\nAttack', hero.attack, 'Defence', hero.defence, 'Speed', hero.speed)
    
def explore():
    print('\nexplore function')
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
    print('\nrest function')
    randomNumber = random.randrange(10000)
    if randomNumber < 750:
        combatSelect('random')
    elif randomNumber < 1250:
        encounter()
    else:
        restHeal()
    return

def restHeal():
    healAmount = random.randrange((hero.maxHP - hero.currentHP)/2 + 10)
    if hero.currentHP >= hero.maxHP:
        hero.currentHP = hero.maxHP
        print('\nYou are at full health!', '(%s/%s)' % (hero.currentHP, hero.maxHP))
    else:
        print('\nYou healed for', healAmount, 'points, ', '(%s/%s)' % (hero.currentHP, hero.maxHP))
    return

def combatSelect(enemy):
    print('\ncombat function was called')
    if enemy == 'random':
        randomNumber = random.randrange(10000)
        if randomNumber < 2000:
            combatSelect('bat')
        elif randomNumber < 3000 and hero.level > 1:
            combatSelect('wildDog')
        elif randomNumber < 4000 and hero.level > 3:
            combatSelect('giantCrab')
        elif randomNumber < 5000 and hero.level > 5:
            combatSelect('wolf')
        elif randomNumber < 6000 and hero.level > 6:
            combatSelect('redSlime')
        elif randomNumber < 7000 and hero.level > 7:
            combatSelect('hyena')
        elif randomNumber < 8000 and hero.level > 7:
            combatSelect('lion')
        elif randomNumber < 9000 and hero.level > 8:
            combatSelect('manticore')
        elif randomNumber < 9500 and hero.level > 8:
            combatSelect('kingSlime')
        elif randomNumber < 9000 and hero.level > 10:
            combatSelect('dragon')        
        else:
            combatSelect('greenSlime')
    else:
        combat(enemy)
    return

def combat(enemy):
    enemy.attack
    return

def encounter():
    print('\nencounter function was called')
    return

def event():
    print('\nevent function was called')
    return

def story():
    print('\nstory function was called')
    return

def loot():
    print('\nloot function was called')
    return

#Start of I/O

while hero.currentHP > 0:
    heroName = askAdventure(q1)
    askAdventure(str1, 'explore', 'rest', 'check stats')
    while True:
        askAdventure(str2, 'explore', 'rest', 'check stats')

print(heroName, 'has fallen')
