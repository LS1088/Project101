# Test

def main():
    print ("hello world")

if __name__ == '__main__':
    None

##version 0.0.1
version = "0.0.1"
print("Project101, Version ", version)
##Trying to make a simple text-based adventure

#Variables
heroCurrentHp = 100
heroMaxHp = 100
heroWeapon = 'Fists'

#Strings
str1 = "Welcome to this simple text-based adventure"
q1 = "Choose a name for your character"
q2 = "You are awaken by the stench of rotten corpses. You don't remember anything. \nYou try to access the situation around you, and you find yourself in a dark cave."

#Functions
def ask(question, *args, **kwargs):
    print (question)
    if args:
        print ("What is your next action?")
    for num, ar in enumerate(args):
        print (num+1, ar)
    ans = input()
    if ans == 'Check stats':
        checkStats()
    return ans

def checkStats():
    print (heroName, '\nHP: ', heroCurrentHp, '/', heroMaxHp, '\nCurrent weapon: ', heroWeapon)

#Start of I/O

print (str1)
heroName = ask(q1)
ask(q2, 'Explore', 'Rest', 'Check stats')