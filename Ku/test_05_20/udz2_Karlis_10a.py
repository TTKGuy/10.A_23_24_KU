
tries = 4
question = ""
#temperatures from https://www.meteoprog.com/lv/weather/Sigulda/month/december/
tempertures = {
    "1.dec" : -1,
    "2.dec" : -1,
    "3.dec" : -1,
    "4.dec" : +1,
    "5.dec" : +1,
    "6.dec" : +1,
    "7.dec" : +1
    }

#the function that repeats untill the question is answered in a correct way or they run out of attempts
def askdate():
    global question
    global tries
    global tempdate
    
    #checks for tries
    if tries > 0:
        question = input("please input a date (example : 1.dec): ")
        #if the key is in temperatures it goes on but if it isnt it asks again
        if question in tempertures:
            tempdate = tempertures[question]
        else:
            print("the date has been input in an incorrect format, please try again")
            tries -= 1
            askdate()
    else:
        #shuts down programm if no attempts left
        print("you have run out of attempts, programm shutting down")
        exit()

tempdate = ""
askdate()
print(question, "temperature in C =",tempdate,"\n*****\n" + question, "temperature in F =",tempdate*(9/5)+32)