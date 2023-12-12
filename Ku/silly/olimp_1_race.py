S, N = (input("")).split()
S,N = int(S), int(N)

a1 = {}

Stemp = S
Ntemp = N

def sumnums(person : int):
    temp = 0
    for i in a1[person]:
        i = int(i)
        match i:
            case 1:
                temp += 25
            case 2:
                temp += 18
            case 3:
                temp += 15
            case 4:
                temp += 12
            case 5:
                temp += 10
            case 6:
                temp += 8
            case 7:
                temp += 6
            case 8:
                temp += 4
            case 9:
                temp += 2
            case 10:
                temp += 1
    a1[person] = int(temp)


while Stemp > 0:
    a1[S - Stemp + 1] = (input())
    a1[S - Stemp + 1] = a1[S - Stemp + 1].split()
    sumnums(S - Stemp + 1)
    Stemp -= 1
    


print(a1[max(a1, key=a1.get)], len([k for k,v in a1.items() if float(v) == a1[max(a1, key=a1.get)]]))
print(' '.join(map(str, [k for k,v in a1.items() if float(v) == a1[max(a1, key=a1.get)]])))
