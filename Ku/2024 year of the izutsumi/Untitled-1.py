from tkinter import *
import random
import os
import math
num = 10000
b = 0
colors = ["cyan", "teal", "blue"]
window = Tk()
width = 700
height = 700
window.title("hiii :3")
canvas = Canvas(window, width=width, height=height, background="#CDF5FD")
canvas.pack()

ship = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")
ship1 = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")
ship2 = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")
ship3 = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")
ship4 = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")
ship5 = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")


window.update()
while 1==1:
    canvas.moveto(ship, 700/2+math.sin(b)*200-40,700/2+math.sin(b*2)*150-20)
    canvas.moveto(ship1, 700/2+math.sin(b-1)*200-40,700/2+math.sin((b-1)*2)*150-20)
    canvas.moveto(ship2, 700/2+math.sin(b-2)*200-40,700/2+math.sin((b-2)*2)*150-20)
    canvas.moveto(ship3, 700/2+math.sin(b-3)*200-40,700/2+math.sin((b-3)*2)*150-20)
    canvas.moveto(ship4, 700/2+math.sin(b-4)*200-40,700/2+math.sin((b-4)*2)*150-20)
    canvas.moveto(ship5, 700/2+math.sin(b-5)*200-40,700/2+math.sin((b-5)*2)*150-20)
    canvas.create_text(700/2+math.sin(b)*200-40,700/2+math.sin((b)*2)*150-20,text=":3", fill= colors[random.randint(0, 2)])


    #canvas.moveto(ship, 0,0)
    print((1920/3-math.sin(b)*400,1080/3-math.sin(b*2)*150))
    b += 0.005
    window.update()
mainloop()