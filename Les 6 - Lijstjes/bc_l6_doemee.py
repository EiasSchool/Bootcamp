# we gaan aan de lijst met getallen 
# het getal 6 tevoegen en dan alles optellen
# getallen = [1, 2, 3, 4, 5]
# getallen.append(6)
# print(getallen)

# #bereken alle waarden
# print(getallen, sum(getallen))

# we gaan checken of in deze lijst met sporten
# een bepaalde sport zit en welke indec die heeft
# sporten = ["voetbal", "basketbal", "tennis", "zwemmen", "honkbal", "volleybal", "atletiek"]
# print(sporten)
# sport = input('welke sport?').lower()
# if 'zwemmen' in sporten:
#     print('OK', sporten.index(sport))
# else:
#     print('Not OK', sporten.index(sport))

# we gaan uit de volgende lijst met autos 1 halen en tonen
# en dan de rest sorteren
autos = ['BMW', 'Audi', 'Ford', 'Volvo', 'Porche']

auto = autos.pop(3)
print(auto)

autos.sort()
print(autos)

aantal = autos.count('BMW')
print(aantal)