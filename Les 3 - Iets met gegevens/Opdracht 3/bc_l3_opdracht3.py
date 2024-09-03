stad_1 = input("In welke stad gebeurt dit verhaal?")
naam_1 = input("Wat is de naam van de hoofdpersoon?")
woord_1 = input("Wat voor soort dag moet het zijn?")
woord_3 = input("Naar wat voor voorwerp of plek is de hoofdpersoon op zoek?")
woord_4 = input("Hoe zou je de persoon die de hoofdpersoon tegenkomt beschrijven (man/vrouw)?")
woord_5 = input("Wat verkoopt de persoon die de hoofdpersoon ontmoet?")
woord_6 = input("Waar komt de hoofdpersoon vervolgens aan (bij welke plek)?")
woord_zin_7 = input("Wat doen de mensen die de hoofdpersoon ziet (beschrijf hun activiteit)?")

verhaal = f'Het was een {woord_1} dag in {stad_1}.{naam_1} liep door de straten, op zoek naar een {woord_3}.Plotseling zag {naam_1} een {woord_4} man/vrouw die een {woord_5} verkocht.{naam_1} besloot om het te kopen en liep verder. Toen {naam_1} bij een {woord_6} kwam,zag hij/zij een groep mensen die {woord_zin_7}.{naam_1} besloot om mee te doen en had de tijd van zijn/haar leven.'

print(verhaal)