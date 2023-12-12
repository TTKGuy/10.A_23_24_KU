import random
import tkinter as tk

colors = ["cyan", "teal", "blue"]

window = tk.Tk()

canvas = tk.Canvas(window, width=400, height= 400, borderwidth= 100, highlightthickness=5, bg="teal")
canvas.grid()



while True:
    x0 = random.randint(-200, 800)
    y0 = random.randint(-200, 800)
    s = random.randint(0, 100)
    canvas.create_text(x0, y0, text="hii :3", fill= colors[random.randint(0, 2)])
#    canvas.create_oval(x0, y0, x0+s, y0+s, fill=colors[random.randint(0, 2)])
    window.update()
    

window.title('silly guy times')

window.mainloop()