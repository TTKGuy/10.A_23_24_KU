num1 = None
num2 = None

def getnum():
    global num1
    global num2
    num1 = int(input())
    num2 = int(input())
    checknum()

def checknum():
    if(num1*num2<0):
        print("Wrong!")
        getnum()
    else:
        print(num1+num2)
        
getnum()