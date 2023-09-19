import math
import random

num = 43.7

print(math.floor(num)) #rounded down
print(math.ceil(num)) #rounded up

print(math.pow(num, 3), 'or easier', num**3) #powers wowie

print(math.sqrt(num)) #square root

x = 80085/101.32

print(x)
print('%.3f'%x,"or also bad", '{:.3f}'.format(x) ,"or easier", round(x, 3)) # rounding to digits

rnum = random.random() #0.0000001, 1.0
print(rnum)

rnum2 = random.randint(1, 12) # take a wild guess
print(rnum2)