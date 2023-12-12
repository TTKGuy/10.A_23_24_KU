import random
A,B,C = 1,1,1
answers = []

tries = 1000000

while tries > 0:
    tries-=1
    if A**(1./3.) + B**(1./3.) == C**(1./3.):
        if 0 not in [A,B,C]:
            if [A,B,C] not in answers:
                answers.append([A,B,C])
        A,B,C = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100) 
    else:
        A,B,C = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100) 
        
answers.sort()
print(answers)