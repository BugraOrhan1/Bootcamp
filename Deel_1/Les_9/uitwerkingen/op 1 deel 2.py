print('inschrijven vrachtwagenchaufers')
rijbewijs = input('rijbewijs? (ja/nee)')
paspoort = input('heb je een paspoort? (ja/nee)')
rus = input('beheerst u russisch? (ja/nee) ')
geo = input('beheerst u georgisch? (ja/nee) ')

if rijbewijs == 'ja' and paspoort == 'ja' and (rus == 'ja' or geo == 'ja') :
          print('we nemen graag aan')
else:
    ('sorry rijbewijs en paspoort en russish en georgischverplicht!!')
     

