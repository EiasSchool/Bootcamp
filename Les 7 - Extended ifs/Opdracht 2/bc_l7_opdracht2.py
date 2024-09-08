leeftijd = int(input('Wat is je leeftijd?\n'))
snor = input('Heb je een snor? (j/n)\n').lower()
diploma = input('Heb je een diploma? (j/n)\n')

if (leeftijd >= 18 and snor == 'j') or (leeftijd < 18 and diploma == 'j'):
    print('je bent aangenomen')
else:
    print('jij bent niet aangenomen')