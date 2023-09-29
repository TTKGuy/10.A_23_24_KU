from termcolor import colored
from colorama import Fore, Back, Style
import colorama
import time
numbers = [0, 1, 2, 3, 4, 5]
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
spaces = ['', '  ', '    ', '  ▓▓  ', '    ', '  ']
spaces2 = ['   ', '  ', ' ', '', ' ', '  ']


def thing():
    for number in numbers:
        print(colored(spaces2[number] +'▓' +spaces[number] + '▓',  colors[number]))
        time.sleep(0.05)
    Fore.RESET
#   print("    ",end = '')
    thing()
    
thing()