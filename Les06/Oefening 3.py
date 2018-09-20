getallenrij = [2, 4, 6, 8, 10, 9, 7]

zoekgetal = eval(input('Geef een getal: '))

gevonden = False

for getal in getallenrij :
    if getal == zoekgetal :
        gevonden = True
if gevonden == True :
    print('Getal in de lijst')
else :
    print('Getal niet in de lijst')