#find price of tshirt ordering and delivering, ordering is based off the type of print, shirt count
#delivering is based off the amount of shirts

def order_shirt(count : int, print : str, delivery : bool):
    price = 0
    if print.lower() == 'text':
        price += 5
    elif print.lower() == 'symbol':
        price += 7
    elif print.lower() == 'photo':
        price += 20
    else:
        return("BAD_INPUT - NONDEFINED SHRIT PRINT")
    if count <= 0:
        return("BAD_INPUT - NEGATIVE SHIRT AMOUNT")  
    else:
        price *= count
    if delivery and price < 50 or price < 50 and delivery == "Yes":
        price +=15
    if price > 100:
        price *= 0.95
    return price
try:
    print('This will cost',order_shirt(int(input("Please input the amount of shirts you will purchase\n")),input("Please input the print of the shirt\npptions:\nTEXT\nSYMBOL\nPHOTO\n"),bool(input("Do you want delivery?\nYes : True\nNo : False\n"))),"✧")
except :
    print("something went wrong!")
input()

