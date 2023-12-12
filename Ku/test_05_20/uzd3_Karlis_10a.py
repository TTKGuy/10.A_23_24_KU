numA = int(input("please input how many different numbers there are going to be (it has to be more than or 3): "))
numL = []
#Number Amount and Number List


#if the number amount is less than 3 it keeps asking till its more, then it appends the numbers
while numA < 3:
    numA = int(input("please input how many different numbers there are going to be (it has to be more than or 3): "))
while numA > 0:
    numL.append(int(input("Please input the " + str(len(numL)+1) +" number: ")))
    numA-=1
print('list  of numbers:',numL)
#just sorts it and picks the last number in the array
numL.sort()
print('the biggest number is:', numL[len(numL)-1])
