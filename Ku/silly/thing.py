import random
import tkinter as tk
from random_word import RandomWords 
import time

window = tk.Tk()
window.geometry('500x500')
canvas = tk.Canvas(window, width=400, height= 400, borderwidth= 100, highlightthickness=5, background='white')
canvas.create_text(300, 300, text='a', fill= 'black',font=("Purisa", 32), id="text_id")
timething = time.time()

while True:
    if time.time() >= timething + 3:
        canvas.delete("text_id")
        
        print("thing")
        timething = time.time()
        canvas.create_text(300, 300, text=RandomWords().get_random_word(), fill= 'black',font=("Purisa", 32))
        
        
    #canvas.pack()
    #canvas.delete('all')

            #    canvas.create_oval(x0, y0, x0+s, y0+s, fill=colors[random.randint(0, 2)])
    window.update()
    
    

window.mainloop()
window.title(RandomWords().get_random_word())

