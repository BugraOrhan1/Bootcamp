print('inschrijven vrachtwagenchaufers')
rijbewijs = input('rijbewijs? (ja/nee)')
paspoort = input('heb je een paspoort? (ja/nee)')
rus = input('beheerst u russisch? (ja/nee) ')
geo = input('beheerst u georgisch? (ja/nee) ')

if rijbewijs == 'ja' and paspoort == 'ja': 
     if rus == 'ja' or geo == 'ja' :
          print('we nemen graag aan')
     else:
        print('sorry, russish en georgisch verplicht!!')
else:
    ('sorry rijbewijs en paspoort verplicht!!')
     





