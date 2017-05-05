import random, time, threading, sys, math, winsound, numpy
from colorama import init, Fore, Back, Style
init(convert=True, autoreset=False)


line = "--------------------------------------------------------------------------------"

print('%s\n%s\n%s' % (line, Fore.RED + Back.WHITE + Style.BRIGHT + 'You have leveled up!' + str(int('2') - 1) + '>' + str(int('2')) + Fore.RESET + Back.RESET + Style.RESET_ALL, line))
print('%s\n%s\n%s' % (line, Fore.RED + Back.WHITE + Style.BRIGHT + 'You have leveled up!' + str(int(hero.level) - 1) + '>' + hero.level + Fore.RESET + Back.RESET + Style.RESET_ALL, line))