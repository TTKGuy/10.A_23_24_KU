i = 0
if i == 0:
    fnames = open("demo.txt", "r", encoding="utf8")

    print(fnames.read())

    fnames.seek(0)

    print(fnames.readline())

    fnames.seek(0)

    print(fnames.read(10))

    fnames.seek(0)
    fnames.close()

if i == 1:
    dwrite =open('demo-write.txt', 'w+', encoding='utf8')
    dwrite.write("hiiii :3\n")
    dwrite.write("izu just like me fr fr\n")
    a = 0
    dwrite.seek(0)
    print(dwrite.read())
    dwrite.close()
    
if i == 2:
    #use w+ to create a file 'dati2.txt'
    f = open('dati2.py', 'w+', encoding='utf8')
    f.write("print('hello, world!')\nf = input()")
    a = open('dati2.py', 'r', encoding='utf8')
    
if i == 3:
    file = open('characters.txt', 'a+', encoding="utf8")
    characters = {
        'izu':'cat',
        'lios':'tsm',
        'sen':'cook'
    }
    file.writelines(characters)
    print(file.read())

if i == 4:
    fx = open('~$woe!.xlsx', 'r+', encoding='utf8')
    