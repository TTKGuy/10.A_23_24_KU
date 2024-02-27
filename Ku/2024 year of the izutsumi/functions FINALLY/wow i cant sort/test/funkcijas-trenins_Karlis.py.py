import math
import random

def drawBlanks():
    
    #Simply printing a single \n will print two blank lines, as this function should do
    print('\n')

def drawStars(starCount):
    
    #the function creates an empty variable, and for every star required by the starcount variable it adds an additional star to the value before printing it
    stars = ''
    for i in range(starCount):
        stars += '*'
    print(stars)

def getFact(number):
    
    #Factorial getting function not much to explain about this function
    return math.factorial(number)

def getInput(question, reqAnswers, type, errorMsg):
    
    #My input function, wasnt required for this project but i like its reliability
    #It requires the input of a question that will be asked trough the input, some sort of list of values that are allowed, a type so that it can be changed into the type for checking if it works for values, and a custom error message incase the value isnt one of the selected ones
    #It also returns 'Er' in this case if the answer doesnt match, so that it can be used further to identify that it didnt end up matching
    try:
        tempIn = input(question)
        
        #Here if the input isnt of the required type it attempts to hange it to the type, if it returns an error (changing 'b' into an int) it will return a message stating so
        if type(tempIn) != type:
            if type == int:
                tempIn = int(tempIn)
            if type == float:
                tempIn = float(tempIn)
            if type == str:
                tempIn = str(tempIn)
                
        #if the input isnt one of the possible answers, it returns the custom error
        if tempIn not in reqAnswers:
            
            print(errorMsg)
            return 'Er'
        else:
            
            #if all is well it returns the gained input
            return tempIn
    except ValueError:
        
        #if weird type then it returns a message stating so
        print('you have input a value that doesnt match the allowed values in type')
        return 'Er'

def main():
    print("Factorial Calculator")
    drawStars(55)
    
    while 1 == 1:
        #this keeps looping untill the programm is shut down with the exit() function
        
        temp = getInput('Input a whole positive number that is lesser than 13:\n',range(0, 13), int, "The number is too big or negative!")
        
        #if the user input all correctly, it prints the factorial
        if temp != 'Er':
            print("Factorial:",getFact(temp))
            
        temp = getInput('Do you wish to continue? (Y - yes | N - no)\n',['Y', 'N'], str, "Y to continue, N to stop")
        
        while temp == 'Er':
            #If the user input an answer that wasnt Y or N it asks again, feels more convinient this way
            temp = getInput('Do you wish to continue? (Y - yes | N - no)\n',['Y', 'N'], str, "Y to continue, N to stop")
            
        if temp == 'Y':
            #if user wants to continue, simply prints the double blank lines and goes back to the start of while 1 == 1
            drawBlanks()
        elif temp == 'N':
            
            #if user wishes to stop i draw the blanks, a random number of stars in the allowed star ammount, and thank them before exiting the programm
            drawBlanks()
            drawStars(random.randrange(10, 20))
            print("Thank you!")
            exit()
            
        

main()
