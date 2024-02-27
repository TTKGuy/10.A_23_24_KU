#write program that structures data fro one file, refreshes them and writes them in a new file
import random

lines = []
wordc = 0
try:
    f = open("Why, I can't see.txt",'r+',encoding="utf8")
    for i in f:
        lines.append(i)
    random.shuffle(lines)
    print(lines)
    f = open("rd5names.txt", 'w+', encoding="utf8")
    f.writelines(lines)
    f.close()
except FileNotFoundError:
    print("you fucked something up idiot")
except Exception as e:
    print(e)