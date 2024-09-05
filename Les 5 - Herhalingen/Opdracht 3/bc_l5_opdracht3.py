from random import randint

te_raden = randint(1,5)

while True:
    gok = int(input('Kies een getal van 1 t/m 5: '))
    if gok == te_raden:
        print("Je hebt het getal goed geraden!")
        break
    else:
        print("Je hebt het getal niet goed geraden!")