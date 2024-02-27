import tkinter as tk
import time
import random
import os


class pet():
    def __init__(self):
        # create a window
        self.window = tk.Tk()

        #0 == still 1 == right 2 == left 3 is down 4 is up
        self.state = random.randrange(0,5)
        
        # placeholder image
        self.walking_right = [tk.PhotoImage(file='walking_right.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        # timestamp to check whether to advance frame
        self.timestamp = time.time()
        self.twtimestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='black')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)
        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'black')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='black')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = random.randrange(0, 1000)
        self.y = random.randrange(0, 700)
        self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        
        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        # move right by one pixel
        if self.state == 1:
          self.x += 1
        elif self.state == 2:
          self.x -= 1
        if self.state == 3:
          self.y += 1
        elif self.state == 4:
          self.y -= 1
        if self.state == 5:
          #os.system('functest.py')
          self.x += random.randrange(-100,100)
          self.y += random.randrange(-100,100)
          self.x += random.randrange(-100,100)
          self.y += random.randrange(-100,100)
          self.frame_index = (3)

        elif self.state == 0:
          pass

        # advance frame if 50ms have passed
        
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.walking_right[self.frame_index]
        if time.time() > self.twtimestamp +2:
            self.twtimestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.state = random.randrange(0,6)
            print(self.state)
        # create the window
        self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        if self.y >= 720:
            self.twtimestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.state = 4
            print(self.state)
        if self.x >= 1200:
            self.twtimestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.state = 2
            print(self.state)
        if self.y <= -40:
            self.twtimestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.state = 3
            print(self.state)
        if self.x <= -40:
            self.twtimestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.state = 1
            print(self.state)

        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 10ms
        self.window.after(10, self.update)

pet()