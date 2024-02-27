import time

f = open("Why, I can't see.txt",encoding="utf8")
i = open('download.jpg',"rb")
i2 = open('edited.jpg',"xb")

short = []
med = []
long = []

ditat = ''

for dat in i:
    if ditat == '':
        ditat = dat
    i2.write(ditat)

    for dat2 in dat:
        
        print(dat2, 'aaaa', type(dat2))
#    print(dat, 'a')



if 1 != 1:
    for i in f:
        if len(i) <= 20:
            if i not in short:
                short.append(i)
        elif len(i) <= 35:
            if i not in med:
                med.append(i)
        else:
            if i not in long:
                long.append(i)

        for b in i:
            
            if b not in 'אֶהְיֶהאֲשֶׁראֶהְיֶה':
                time.sleep(0.001)
                print(b, end="")
            else:
                for c in b:
                    print(c, end="")
                time.sleep(0.05)
        time.sleep(0.02)
#print(f.read())

f.close()
i.close()
i2.close()
print(short)
print(med)
print(long)