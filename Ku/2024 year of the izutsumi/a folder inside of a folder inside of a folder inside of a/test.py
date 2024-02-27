a = 2

if a == 1:


    a = list(map(int, input("First number array: \n").split()))
    b = list(map(int, input("Seccond number array: \n").split()))

    asum = sum(a)
    bsum = sum(b)

    if asum > bsum:
        print('first array is larger than the seccond by', asum - bsum)

if a == 2:
    f = open('numbers.txt', 'r+', encoding='utf8')
    b = list(map(int, f.read().split()))
    bave = sum(b) / len(b)
    for i in b: 
        if i > bave:
            print(i, end=' ')