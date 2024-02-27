import math
import datetime
import time



print(datetime.datetime.utcnow().hour)

mealtimes = [9.00, 12.00, 5.00]

meals = {
    'mcdonald' : ['mcdonal', 'french fries and chicken nuggets', 20001]
}

def ViewPlan():
    MEAL = 'mcdonald'
    print(meals[MEAL][0],'\n' + meals[MEAL][1],'\n' + str(meals[MEAL][2]))

def ConfMeals():
    print(':3')

def ConfSettn():
    print(':3')


def Start():
    global temp
    print("Welccome to Meal Thing, What would you like to do?\n1 : View todays eating plan\n2 : Configure meals\n3 : Configure settings")
    temp = input()
    while not(temp == '1'or temp == '2' or temp == '3'):
        print("Wrong input, please input one of the options (1 2 or 3)")
        temp = input()
    
    if temp == '1':
        ViewPlan()
    if temp == '2':
        ConfMeals()
    if temp == '3': 
        ConfSettn()  
Start()



