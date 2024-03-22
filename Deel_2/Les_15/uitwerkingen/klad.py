# N = input('wat is je naam?')
# L = int(input('hoe oud ben je?'))
# H = input('welke kleur haar')
# if L == '16' :
#     if N == 'Bugra' or H == 'rood' :
#         print ('lekker bezig')
# else :
#     print('niks')

def bereken_hoog_btw_bedrag_incl(bedrag_ex):
    BTW = 1.21
    bedrag_incl = round(bedrag_ex * BTW, 2)
    return bedrag_incl

bedragen=(3.15, 2.45, 7.2)

for bedrag in bedragen:
    bedrag_in = bereken_hoog_btw_bedrag_incl(bedrag)
    print(F'excl,: € {bedrag} incl,: € {bedrag_in}')
