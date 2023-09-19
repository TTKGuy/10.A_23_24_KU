import random
import os

num = int(input("Enter a number, any number (if you get the wrong number you die)"))
if num == random.randint(0, 5):
    print("correct!")
else:
    print("moron")
