
i = 1

#Loop (while) until i = 10
print("Starting Loop !")

while i <= 10 :
    print(i)
    i += 1

print("End of loop !")

# Loop (for) pour chaque

for letter in "Hello World":
    print(letter)

friends = ["Alain", "Marc", "Noémie", "Jean", "Bertrand"]

for name in friends:
    print(name)

for index in range(0, 11): #range n'inclus pas le dernier chiffre (ex: 0,10 affiche 1 à 9)
    print(index)

for index in range(len(friends)):
    print(friends[index])


# Logic inside loop
for index in range(5):
    if index == 0:
        print("First index")
    else:
        print("Not first")