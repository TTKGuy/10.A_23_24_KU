import random
NumL = []
temp = 10

if int(input("Do you want to\n1. input your own number list\nor\n2. use a randomly generated one? (1/2)\n")) == 1:
    while temp > 0:
        #if the person wanted to input their own numbers here it loops 10 times asking for the numbers
        NumL.append(int(input("Please input the "+str(len(NumL)+1) + " number")))
        temp -= 1
else:
    #random numbers 10 times if the person didnt want to input their own
    NumL = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

odds = 0
evens = 0

#checks all numbers in aray and if they are odd it adds one to the odd counter, if even it adds one to the even counter
for i in NumL:
    if i%2 == 0:
        evens += 1
    elif i%2 != 0:
        odds += 1
        
print("List:",NumL,"\nOdd number count:",odds,"\nEven number count:",evens)