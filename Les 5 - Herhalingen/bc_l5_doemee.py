# we gaan hier een loop voor maken

# for getal in range(5, 26):
#     print(getal)

# We maken een programma die herhaaldelijk (met een input()) ‘?’ zegt 
# totdat het resultaat daarvan gelijk is aan ‘quit’.
# Daarna printen we het aantal iteraties (Het aantal keren dat de vraag is gesteld).

# getal = int(input('Geef getal: '))

# for x in range(1, 11):
#     print(f'{x} x {getal} = {x*getal}')

teller = 0

while True:
    antwoord = input('? ')
    if antwoord == 'quit':
        print(f'aantal pogingen: {teller}')
        break
    else:
        print(f'pogingen {teller}')
        teller = teller + 1