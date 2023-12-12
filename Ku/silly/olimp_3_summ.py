t = input().split()
c = list(range(int(t[0]), int(t[1])))
print(c)
rez = []


def getfull(ints):
    rez.append(0)
    temp = len(rez) - 1
    while len(ints) >= 1:
        rez[temp] += int(ints)
        ints = ints.rstrip(ints[-1])
        print(ints)
    
for i in t:
    getfull(i)
    
print(rez)