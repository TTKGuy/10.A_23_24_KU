a = 1

if a == 0:
    #ask for inputs untill the input is an empty line and save the data in a file
    f = open('temp.txt', 'w+', encoding='utf8')
    while True:
        t = input()
        if t != '':
            t += '\n'
            f.write(t)
        else:
            break
    f.close()

if a == 1:
    #gain text inpu tand write it into a file, gain number input and write it in, every line starts with an extra line num
    f = open('temp.txt', 'w+', encoding='utf8')
    i = 1
    while True:
        t = input('input a text ')
        if t != '':
            t = str(i) + " " + t +'\n'
            f.write(t)
            i += 1
        else:
            break
        t = int(input('input a number '))
        if t != '':
            t = str(i) + " " + str(t) +'\n'
            f.write(t)
            i += 1
        else:
            break
    f.close()
    
    
    
    