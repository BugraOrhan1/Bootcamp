import random
fout = 0
goed = 0
while True :
    getal_random = (random.randint(1, 5))
    print(getal_random)
    while True :
        getal = int(input('getal?'))
        if getal == getal_random :
            print('goed')
            goed+=1
            print('wilt u door gaan?')
            Antwoord = input('j/n')
            break
        print('fout')
        fout+=1
    if Antwoord != 'j' :
        print(f'bedankt voor spelen u had fout:{fout} en goed:{goed} ')
        break 
