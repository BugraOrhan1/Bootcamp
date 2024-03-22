naam = input ('wat is u naam?')
age = input  ('leeftijd =')
age_1 = 18


if (int(age) < age_1 ) :
    print(f'Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in :-( ')
if (int(age) > age_1 ) :
    print(f'Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans)')
if (int(age) == age_1 ) :
    print(f'Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans)')

