# Print + variables

prenom = "John Mavick"
nom = "Doe"

print(f"Prénom : {prenom} \nNom : {nom}")

# Simple fonctions

print(prenom.upper(), nom.lower()) # Transformer en Majuscule ou en Minuscule
print(len(prenom), len(nom)) # Nombre de caractères
print(len(prenom) + len(nom)) # Nombre de caractère Prenom + Nom
print(nom.upper().isupper()) # Bolean est il en Majuscule

print(prenom[0]) # Print la première lettre
print(prenom[1]) # Print la deuxième lettre
print(prenom[2]) # Print la troisième lettre
print(prenom[3]) # Print la quatième lettre
# print(prenom[9]) # Donne une erreur OUT OF RANGE

print(nom.index("o")) # Donne l'index du premier caractère trouvé
print(prenom.replace("Mavick", "Montain")) # Remplace le premier argument par le deuxième

