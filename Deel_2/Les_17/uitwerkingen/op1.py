import random
getal_random = (random.randint(1, 5))
A=0
while A< 3:
    I = int(input('getal?'))
    if getal_random == I :
        print('je hebt het goed!')
        A+=1
    if A == 3 :
        break
    else :
        print('je hebt het niet goed!')


    
