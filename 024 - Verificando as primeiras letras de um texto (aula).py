#caso o nome seja 'santos', 'santosss', 'santomera' ... vai da true
cid = str(input('Em que cidade voce mora? ')).strip()
print(cid[:5].upper() == 'SANTO')