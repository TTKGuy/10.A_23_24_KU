import random
import math
import sys

sys.setrecursionlimit(100000000)


unum = [2, 7]

def defallrandom():
    U, S, K, R, Ī, G, O, I = defrandom(), defrandom(), defrandom(), defrandom(), defrandom(), defrandom(), defrandom(), defrandom()
    

def defrandom():
    global unum
    i = random.randint(0, 9)
    while str(i) in unum:
        i = random.randint(0, 9)
    else:
        unum += str(i)
        return(i)
        

B= 2
A= 7
U= None
S= math.nan
K= math.nan
R= math.nan
Ī= math.nan
G= math.nan
O= math.nan
I= math.nan

U, S, K, R, Ī, G, O, I = defrandom(), defrandom(), defrandom(), defrandom(), defrandom(), defrandom(), defrandom(), defrandom()

print(U, S, K, R, Ī, G, O, I)

RĪGA = str(R) + str(Ī) + str(G) + str(A)

BAUSKA = str(B) + str(A) + str(U) + str(S) + str(K) + str(A)
print (BAUSKA)
letters = ['B', 'A', 'U', 'S', 'K', 'R', 'Ī', 'G', 'O', 'I']
lvalues = [2, 7, random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]

i = 1
b=1

print(unum)

skaitlis1 =  A * int(BAUSKA)
skaitlis2 = G * int(BAUSKA + str(0))
skaitlis3  = Ī * int(BAUSKA + str(0) + str(0))
skaitlis4 = R * int(BAUSKA + str(0) + str(0) + str(0))
    
def reiz():
#    print("      ", B, A, U, S, K, A)
#    print("         ", R, Ī, G, A)
    
    #print(skaitlis1)
    #print(skaitlis2)
    #print(skaitlis3)
    #print(skaitlis4)  
    if 1 == 1:
        manvissbesii()
    else:
        print('23')    
    
    
    
    
    
print()
strings = str(skaitlis1 + skaitlis2 + skaitlis3 + skaitlis4)
def manvissbesii():
    if(strings[4] == str(2) and strings[5] == str(0) and strings[6] == str(2) and strings[7] == str(3)):
        print("Rēķināšana gatava rezultāts ir:", strings)
    else :
        print("false", BAUSKA, RĪGA) 
        unum = [2, 7]
        
        defallrandom()
        manvissbesii()

manvissbesii()