
def ask(floats, question):
    answ = input(question + "\n")
    if floats == True:
        if float(answ) >= 0:
            return answ
    if floats == False:
        if int(answ) >= 0:
            return answ


applereq = 3
sugarreq = 1
waterreq = 500
lemonreq = 1
almondextreq = 5
cinnamonreq = 10


customrec = input("Would you like to use our default recipe or input your own?\nDefault recipe:\n3 kg of apples\n1 kg of sugar\n500ml of water\n1 lemon\n5ml of almond extract\n10g of cinnamon\n(Y,N)\n")
if customrec == 'N':
    applereq = ask(True, "How many kg of apples are used per jam in the recipe")
    sugarreq = ask(True, "How many kg of sugar are used per jam in the recipe")
    waterreq = ask(True, "How many ml of water are used per jam in the recipe")  
    lemonreq = ask(True, "How many lemons are used per jam in the recipe")  
    almondextreq = ask(True, "How many ml of almond extract are used per jam in the recipe") 
    cinnamonreq = ask(True, "How many grams of cinnamon are required per jam in the recipe")
else:
    pass

customrec = input("Would you like to use our default average pricing or input your own?\nDefault pricing:\n1,26 eur per kg apples\n1 kg of sugar\n500ml of water\n1 lemon\n5ml of almond extract\n10g of cinnamon\n(Y,N)\n")
    
appleprc = ask(True, "What is the price of apples per KG")

applenum = int(input("How many apple kg"))

sugarprc = float()

apple, sugar, water, lemon, almondextract, cinnamon = 0
recipe = appleprc * applenum