from tkinter import *
import random
import os
num = 10000

window = Tk()
width = 700
height = 700
window.title("hiii :3")
canvas = Canvas(window, width=width, height=height, background="#CDF5FD")
canvas.pack()

ship = canvas.create_oval(0, 0, 80, 40, outline="black", width=10, fill="gray")


window.update()
while 1==1:
    canvas.moveto(ship, window.winfo_pointerx() - window.winfo_rootx(), window.winfo_pointery() - window.winfo_rooty())
    print(window.winfo_pointerx() - window.winfo_rootx(), window.winfo_pointery() - window.winfo_rooty())
    
    window.update()
mainloop()