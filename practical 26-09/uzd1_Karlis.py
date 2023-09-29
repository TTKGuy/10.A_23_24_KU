from colorama import Fore, Back, Style
import time


def thing():
    num1 = int(input())
    num2 = int(input())

    if(8 <= num1 <= 25 and 8 <= num2 <= 25):
        for letter in "Thank you for inputing the correct numbers!":
            print(Fore.GREEN + letter, end = '')
            time.sleep(0.05)
            
    elif(8 <= num1 <= 25 or 8 <= num2 <= 25):
        for letter in "One of the numbers is incorrect!":
            print(Fore.YELLOW + letter, end = '')
            time.sleep(0.05)
        
    else:
        for letter in "read the rules again!":
            print(Fore.RED + letter, end = '')
            time.sleep(0.05)
    print()
    Fore.RESET
    thing()
    
thing()