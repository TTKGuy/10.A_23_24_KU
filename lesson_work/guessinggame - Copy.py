import random
import os
import time

num = int(input("Enter a number, any number (if you get the wrong number you die)"))
if num == random.randint(0, 5):
    print("correct!")
    time.sleep(5)
else:
    print("moron")
    time.sleep(5)
