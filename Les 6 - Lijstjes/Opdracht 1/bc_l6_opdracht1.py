getallen = []

for getal in range(6):
    getal = int(input(f'{getal + 1} Geef een getal\n'))
    getallen.append(getal)

    getallen.sort()

print(getallen)