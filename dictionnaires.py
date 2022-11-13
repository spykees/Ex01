
# Dictionnaires chaque clés DOIT etre unique
month_converstion = {
    
    "Jan" : "Janvier",
    "Fev" : "Février",
    "Mar" : "Mars",

}

print(month_converstion.get("Mar"))

#Si la valeur n'exite pas dans le dico on affiche une valeur par defaut
print(month_converstion.get("Ali", "Valeur par defaut"))