import random
import time
import os
import sys

NameObjects = str(input('Please input the name of the object: \n'))
Dcard = str(input('Do you have a discount card?\n(y/n)\n'))

RawPrice = 0.0
while RawPrice <= 0.0: #defines the price as above 0 or 0
    RawPrice = float(input('Please input the price of the object:\n'))

DiscountOption = 0
DiscountVariable = 0

def _RandDiscount(object): #finds and defines the correct discount for the object
    global DiscountOption
    global DiscountVariable
    random.seed(object)
    drand = random.randint(1, 6)
    if drand == 1:
        DiscountOption = 1
        DiscountVariable = 0.30
        print('This object has a 30% discount!')
        print('Discount has been applied')
    if drand == 2:
        print('This object has a 40% discount if you have a discount card!')
        if Dcard == 'y':
            DiscountOption = 1
            DiscountVariable = 0.40
            print('Discount has been applied!')
        if Dcard == 'n':
            DiscountOption = 0
            DiscountVariable = 0
            print('No discount')
    if drand == 3:
        print('This object has a 20% discount with no card, 50% if you have a discount card!')
        if Dcard == 'y':
            DiscountOption = 1
            DiscountVariable = 0.50
            print('50% Discount has been applied!')
        if Dcard == 'n':
            DiscountOption = 1
            DiscountVariable = 0.20
            print('20% discount has been applied')
    if drand == 4:
        DiscountOption = 2
        DiscountVariable = 0.30
        print("This object has a 30% discount if you buy more than 3 objects")
    if drand == 5:
        DiscountOption = 3
        DiscountVariable = 1
        print('Every seccond object is free!')
    if drand == 6:
        DiscountOption = 0
        DiscountVariable = 0
        print('This object has no discount.')
        
_RandDiscount(NameObjects) #Defines said discount

NumbObjects = 0.0
while NumbObjects <= 0: # makes sure there are more than 0 objects
    NumbObjects = int(input('Please input the amount of Objects: \n'))

price = 0.0

if DiscountOption == 0: # finds the correct price based off the discount
    price = RawPrice * NumbObjects
if DiscountOption == 1:
    price = (RawPrice*NumbObjects) - ((RawPrice*NumbObjects) * DiscountVariable)
if DiscountOption == 2:
    if NumbObjects >= 3:
        price = (RawPrice*NumbObjects) - (RawPrice*NumbObjects) * DiscountVariable
    else:
        price = RawPrice * NumbObjects
if DiscountOption == 3:
    for i in range(NumbObjects):
        if (i % 2) == 0:
            pass
        else:
            price += RawPrice
price = round(price, 2)
print(price)


#the are you done purchasing question
if str(input("Are you done with purchasing\n(y/n)\n")) == 'n':
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    #chreates the thing
    print("Congratulations on your purchase!\n")
    print('Price: ' + str(price)+ '\n\nObject: ' + str(NameObjects) + "    " + str(RawPrice) + "\nDiscount = ", end="")
    if DiscountOption == 1:
        print(DiscountVariable)
    elif DiscountOption == 0:
        print("None")
    elif DiscountOption == 2:
        print("30% For 3 or more objects")
    elif DiscountOption == 3:
        print("Every other object free")
    
input()#keeps the programm up so you can read what it says