a=5
b=3
c=2

# if statement 1
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")    

# if statement 2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar")


print("UITLEG: omdat in de eerste if-statement `and` eerst wordt gelezen maar in de tweede zorgen de haakjes ervoor dat `or` eerst gelezen wordt wat de uitkomst verandert.")