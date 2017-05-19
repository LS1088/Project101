from colorama import init, Fore, Back, Style
init(convert=True, autoreset=False)

'''
STRINGS
'''
infoStr = "\nBGM: Hatsune Miku - (UNICODEPLACEHOLDER).\nCombat system is fully automatic."

greetingStr = "\n\nTHIS IS A GREETING MESSAGE"

line = "--------------------------------------------------------------------------------"

question1 = "Choose a name for your character"

str1 = '%s\n%s' % (line, "You continue your adventure.")

storyStr1 = "You are awaken by the stench of rotten corpses. You can't remember anything. \nThe unfamiliar surroundings confuses you, but you must get out of here."

shopStr1 = "You find a general store."
shopStr2 = "You meet a travelling trader who has a selection of uncommon items."
shopStr3 = "You find a dodgy merchent selling rare items."

helpStr = "Defeat enemies in combat in order to gain exp and items. Items only start dropping when you reach a certain level.\nCurrent RNG: Explore - 6"\
    "0% combat, 10% encounter, 10% story, 10% event, 10% loot;\nRest - 7.5% combat, 5% encounter, 87.5% heal."

continueStr = Fore.GREEN + Style.BRIGHT + "Press enter to continue..." + Fore.RESET + Style.RESET_ALL

restartStr = '%s\n%s\n%s\n' % (line, Fore.GREEN + Style.BRIGHT + "Press enter to restart the game." + Fore.RESET + Style.RESET_ALL, line)