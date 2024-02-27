import random

def drawStars(starCount):
    
    #the function creates an empty variable, and for every star required by the starcount variable it adds an additional star to the value before printing it
    stars = ''
    for i in range(starCount):
        stars += '*'
    print(stars)

while 1 == 1:
    drawStars(random.randrange(1, 100))
    a = 0
    while a < 4:
        print(random.randint(0,1), end='')
        a += 1
    else:
        temp = random.randrange(1, 15)
        if temp <=11:
            print(" ", end='')
        elif temp <= 13:
            pass
        else:
            print('')
        a = 0