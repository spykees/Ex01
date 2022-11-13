
""" friends = ["Alain", "Marc", "Noémie", "Jean", "Bertrand"]

print(friends)
print(friends[2]) #access index
print(friends[-1]) #access index reverse
print(friends[2:]) #access specific index
print(friends[2:4]) #access specific index 2 3 but not 4

#Modify a list
print(friends)
friends[1] = "Jean"
friends[3] = False
print(friends) """

# List Fonctions
numbers = [1, 3, 5 ,7, 12, 15]
friends = ["Alain", "Marc", "Noémie", "Jean", "Bertrand"]
print(friends)

friends.append("Mike") # Ajouter à la fin
friends.insert(1, "Kelly") # Ajouter après un index
friends.remove("Jean") # Effacer un élément par nom ou par index ou tout effacer friends.clear()
friends.extend(numbers) # Fusionner

print(friends)
friends.pop() #Pop of the last element

print(friends)

friends = ["Alain", "Marc", "Kevin", "Noémie", "Noémie", "Jean", "Bertrand"]
print(friends.index("Noémie")) # Donne l'index de l'element
print(friends.count("Noémie")) # Compte le nombre d'éléments

friends.sort() # organise descendant
print(friends)
friends.reverse() # Inverse la liste
print(friends)

friends2 = friends.copy() # Cpy a list
print(friends2)