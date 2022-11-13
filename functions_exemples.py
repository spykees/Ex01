
#Creation de la fonction simple
def say_hi():
    print("Hello")

# Function avec plusieurs parametres
def say_hi_param(name, age):
    print(f"Hello {name} you are {age} years old")

# Function avec return. Return breack la function et rien ne sera executer après
def cube(num):
    return num * num * num
    


# Appel de la function simple
say_hi()

# Appel de la function avec plusieurs paramètres
say_hi_param("Mark", 24)
say_hi_param("Elise", 34)

# Appel de la function avec return
result = cube(4)
print(result)
