vruchten = ["apple", "banana", "orange", "grape", "mango", "pineapple"]

print('huidige lijst van fruit: ', vruchten)

index = int(input('Voer een index (0-5) in om een fruit te verwijderen:\n'))

removed_fruit = vruchten.pop(index)

print(f'Je hebt verwijderd: {removed_fruit}')
print(f'Bijgewerkte lijst met fruit: {vruchten}')