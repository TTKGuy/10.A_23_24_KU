#   word counter program
#
#

words = []
wordscounter = {}
wordc = 0
try:
    #f = open("Why, I can't see.txt",'r+',encoding="utf8")
    #f = open("blackboxwarrior.txt",'r+', encoding="utf8")
    f = open('dungeon.py', 'r+', encoding='utf8')
    for i in f:
        for b in i.split():
            if b not in words:
                words.append(b)
            elif b in words:
                if b in wordscounter:
                    wordscounter[b] += 1
                else: 
                    wordscounter.update({b: 2})
            wordc += 1
    sorted_wordscounter = sorted(wordscounter.items(), key=lambda x:x[1], reverse=True)
    print(*sorted_wordscounter,sep=", ")
    print(wordc)
    f.close()
except FileNotFoundError:
    print("you fucked something up idiot")
#except Exception as e:
#    print(e)