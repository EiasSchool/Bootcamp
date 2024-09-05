from random import randint

totale_score = 0

for ronde in range(3):

    print(f'Ronde {ronde + 1}')
    te_raden = randint(1,5)

    aantal_gokken = 0

    while True:
        gok = int(input('Kies een getal van 1 t/m 5: '))
        if gok == te_raden:
            print("Je hebt het getal goed geraden!")
            break
        else:
            print("Je hebt het getal niet goed geraden!")
            aantal_gokken += 1

    score = 20 - aantal_gokken
    totale_score += score

print(f'Jouw Score: {totale_score}')