def absolute(nr):
    if nr < 0:
        return nr * -1
    else:
        return nr

getal = int(input('getal?'))
result = absolute(getal)
print(result)


def getal_maal_5(getal):

    uitkomst = getal * 5
    return uitkomst

result = getal_maal_5(-12)
print(result)


def telop(getal1,getal2):
    pipo = getal1 + getal2
    return pipo 

resulaat = telop(34,5)
print(resulaat)
