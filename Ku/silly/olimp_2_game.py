Ntemp, M1, M2, G = input().split()
N = []
Ntemp, M1, M2, G = int(Ntemp), int(M1), int(M2), int(G)
while Ntemp > 0:
    if Ntemp%M1 == 0 or Ntemp%M2 == 0:
        N.append(Ntemp)
    Ntemp -= 1


def thing(x):
    if x == "N":
        return False
    else:
        return True

def removenums(a : list):
    global N 
    for i in N:
        if int(a[0]) <= i <= int(a[1]):
            N[N.index(i)] = 'N'
            
    N = [i for i in N if i !='N']
temp = []
while G > 0:
    temp = input().split()
    removenums(temp)
    G -=1 
    

print(len(N))
    