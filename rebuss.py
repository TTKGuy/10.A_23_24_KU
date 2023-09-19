import random
import math

unum = [2, 7]

def defrandom(lt):
    while lt == None:
        print("1")
        i = random.randint(0, 9)
        if i in unum:
            print("2")
            defrandom(lt)
        else:
            print("3")
            return(i)
            unum + i

B= 2
A= 7
U= defrandom(U)
S= math.nan
K= math.nan
R= math.nan
Ī= math.nan
G= math.nan
O= math.nan
I= math.nan

U, S, K, R, Ī, G, O, I = defrandom(U), defrandom(S), defrandom(K), defrandom(R), defrandom(Ī), defrandom(G), defrandom(O), defrandom(I)

print(U, S, K, R, Ī, G, O, I)

RĪGA = str(R) + str(Ī) + str(G) + str(A)

BAUSKA = str(B) + str(A) + str(U) + str(S) + str(K) + str(A)
print (BAUSKA)
letters = ['B', 'A', 'U', 'S', 'K', 'R', 'Ī', 'G', 'O', 'I']
lvalues = [2, 7, random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]

i = 1
b=1

def reiz():
#    print("      ", B, A, U, S, K, A)
#    print("         ", R, Ī, G, A)
    skaitlis1 =  A * int(BAUSKA)
    skaitlis2 = G * int(BAUSKA + str(0))
    skaitlis3  = Ī * int(BAUSKA + str(0) + str(0))
    skaitlis4 = R * int(BAUSKA + str(0) + str(0) + str(0))
    print(skaitlis1)
    print(skaitlis2)
    print(skaitlis3)
    print(skaitlis4)       
    
    print(rezultats = skaitlis1[5:6])
    
    
    
    
    
print()
reiz()