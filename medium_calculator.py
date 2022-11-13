# Calculatrice avec Function
def calcul(num1, op, num2):
    if op == "+":
        return(num1 + num2)

    elif op == "-":
        return(num1 - num2)

    elif op == "*":
        return(num1 * num2)

    else:
        return(num1 / num2)


num1 = float(input("Enter first number: "))
op = input("Enter operator(+ - * /): ")
num2 = float(input("Enter second number: "))

result = calcul(num1, op, num2)

print(result)

#Calculatrice sans function
""" 
num1 = float(input("Enter first number: "))
op = input("Enter operator(+ - * /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

else:
    print(num1 / num2)
    
"""
