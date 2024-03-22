oppervlakte = (input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40
import time
aantal = 5
teller = 0
while teller < aantal :
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    time.sleep(1)
teller = teller + 1
totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))

