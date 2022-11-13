""" 
is_male = False
is_tall = False


if is_male and is_tall:
    print("C'est un grand mâle")

elif is_male and not(is_tall):
    print("C'est un petit mâle")

elif not(is_male) and is_tall:
    print("C'est une grande femelle")

else:
    print("C'est une petite femmelle")
 """


# Comparaisons >, <, <=, >=, ==, !=
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2
    
    else:
        return num3


print(max_num(46,42,6))
