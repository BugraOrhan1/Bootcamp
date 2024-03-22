print('inschrijven vrachtwagenchaufers')
rijbewijs = input('rijbewijs? (ja/nee)')

if rijbewijs == 'ja':
    paspoort = input('heb je een paspoort? (ja/nee)')
    if paspoort == 'ja': 
        print('we nemen je graag aan')
    else:
            print('sorry paspoort verplicht')
else:
    print('sorry rijbewijs verplicht')