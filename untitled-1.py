# Test
import random

def main():
    print ("hello world")

if __name__ == '__main__':
    None

##version 0.0.1
version = '0.0.1'
author = 'pedololicon'
print("Project101, \nVersion", version, "\nAuthor:", author)
##Trying to make a simple text-based adventure

#Variables
heroCurrentHp = 100
heroMaxHp = 100
heroWeapon = 'Worn out sword'

#Strings
str1 = "\nWelcome to this simple text-based adventure"
q1 = "\nChoose a name for your character"
str2 = "\nYou are awaken by the stench of rotten corpses. You don't remember anything. \nYou try to access the situation around you, and you find yourself in a dark cave."

#Functions
def ask(question, *args, **kwargs):
    print (question)
    while True:
        if args:
            print ("What is your next action?")
            for num, ar in enumerate(args):
                print (num+1, ar)
        ans = input()
        if args:
            if ans == 'explore' or '1':
                explore()
                break
            elif ans == 'rest' or '2':
                rest()
                break
            elif ans == 'check stats' or '3':
                checkStats()
        else:
            break
    return ans

def checkStats():
    print ('\nName: ', heroName, '\nHP: ', heroCurrentHp, '/', heroMaxHp, '\nCurrent weapon: ', heroWeapon, '\n')
    
def explore():
    randomNumber = random.randrange(10000)
    print('\ndice toss,', randomNumber)
    if randomNumber < 5000:
        combat()
    elif randomNumber < 6000:
        encounter()
    elif randomNumber < 7000:
        event()
    elif randomNumber < 8000:
        story()
    else:
        loot()
    return
    
def rest():
    randomNumber = random.randrange(10000)
    print('\ndice toss,', randomNumber)
    if randomNumber < 750:
        combat()
    elif randomNumber < 1250:
        encounter()
    else:
        restHeal()
    return

def restHeal():
    print('\nrestHeal function was called')
    return

def combat():
    print('\ncombat function was called')
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

print (str1)
heroName = ask(q1)
ask(str2, 'explore', 'rest', 'check stats')
