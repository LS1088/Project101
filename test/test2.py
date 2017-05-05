options = {'explore':1, 'rest':2, 'inventory':8, 'check stats':9, 'help':0}
inventory = []
line = "--------------------------------------------------------------------------------"

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
                elif int(ans) == optionGiven['inventory']:
                    CheckInventory()
                elif int(ans) == optionGiven['check stats']:
                    checkStats()
                elif int(ans) == optionGiven['help']:
                    gameHelp()
                else:
                    print('Please enter a valid input.')
            elif ans == 'explore':
                explore()
                break
            elif ans == 'rest':
                rest()
                break
            elif ans == 'inventory':
                checkInventory()
            elif ans == 'check stats':
                checkStats()
            elif ans == 'help':
                gameHelp()
            else:
                print('Please enter a valid input.')
        else:
            break
    return ans

def main():
    hero.name = askAdventure('%s\n%s' % (line, q1))
    askAdventure(str1, 'explore', 'rest', 'check stats', 'help')
    time.sleep(1)
    while True:
        while combatOn == 0 and heroDeathCounter == 0: 
            askAdventure(str2, 'explore', 'rest', 'inventory', 'check stats', 'help')
            time.sleep(1)
            
if __name__ == '__main__':
    main()