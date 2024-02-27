P,Q,R,S = input("izutsumi reference").split()
P,Q,R,S = int(P),int(Q),int(R),int(S)

def checkshorten(x,y):
    x,y = int(x),int(y)
    a = 1
    while a == 1:
        if x%2 == 0 and y%2 == 0:
            x,y = x/2,y/2
            print(x,y,2)
        elif x%3 == 0 and y%3 == 0:
            x,y = x/3,y/3
            print(x,y,3)
        elif x%5 == 0 and y%5 == 0:
            x,y = x/5,y/5
            print(x,y,5)
        elif (x != 1 and y != 1) and (x%y == 0 or y%x == 0):
            print(x,y, "even")
            x,y = int(x),int(y)
            if x%y == 0:
                x,y = x/y, y/y
            elif y%x == 0:
                y,x = y/x, x/x
        else:
            print(x,y, 'done')
            return(x,y)

print(checkshorten(P,Q), checkshorten(R,S))