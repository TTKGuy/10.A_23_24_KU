import math

people = input()
disturbers = input().split()
peopletemp = int(people)
disturbed = []
peoplel = []

while peopletemp > 0: peopletemp-=1; disturbed.append(0)
peopletemp = int(people)
while peopletemp > 0: peopletemp-=1; peoplel.append(len(peoplel)+1)

def getdisturbed(person):
    temp1 = 0
    temp2 = 0
    opt = 0
    for i in peoplel:
        if i != 'N':
            if int(i) < int(person):
                temp1 += 1
            if int(i) > int(person):
                temp2 += 1

    if temp1 == temp2:
        opt = 1
    elif temp1 < temp2:
        opt = 1
    elif temp1 > temp2:
        opt = 2

    if opt == 1:
        for i in peoplel:
            if i != 'N':

                if int(i) <= person:
                    disturbed[i-1] += 1
    if opt == 2:
        for i in peoplel:
            if i != 'N':
                if int(i) >= person:
                    disturbed[i-1] += 1

    peoplel[person-1] = 'N'

for i in disturbers:
    getdisturbed(int(i))
    
print(' '.join(map(str, disturbed)))