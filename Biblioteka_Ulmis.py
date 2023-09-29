import time

person = 0
#1 for  student, 2 for not student

if(input("Do you currently have a non returned library book in your possesion?\n 1 if yes       2 if no\n") == '1'):
    print("Cant give you it sorry blud maybe return it next time idk")
    time.sleep(3)
    quit()
person = input("You are a\n 1 if student       2 if not student\n")

takeout = int(input("What do you wish to take out?\n1 if a book not in the popular section\n2 if anything in the popular section\n3 if a magazine not in the popular section\n"))
if takeout == 1:
    print("you are going to have to return the book in", 15*int(person), "days")
    time.sleep(3)
    
if takeout == 2:
    print("You are going to have to return the book in 3 days")
    time.sleep(3)
    
if takeout == 3:
    print("you are going to have to return the magazine in 10")
    time.sleep(3)