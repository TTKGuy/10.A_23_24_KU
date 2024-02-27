import keyboard
import time
import mouse
import math
import random

a = 10000
b = 0

time.sleep(3)

while a >= 1:
    a -= 1
    #mouse.double_click()
    
    keyboard.press_and_release('1,enter')


while b >= 0:
    
    #mouse.move(1920/3, 1080/3)
    mouse.move(1920/3-math.sin(b)*400,1080/3-math.sin(b*2)*150)
    time.sleep(0.001)
    b -= 0.01
    

