kleuren = ["rood", "blauw", "groen", "geel", "paars"]

naam = input('Wat is je naam:\n')
fav_kleur = input('Wat is je favoriete kleur?\n')

if fav_kleur in kleuren:
    print(f'{naam}, jouw lievelingskleur {fav_kleur} is net zo vrolijk en vrolijk als jij!')
else:
    print(f'Psst {naam}, deze kleur is niet zo geweldig! Kies liever uit: {', '.join(kleuren)}')