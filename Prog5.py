num1 = int(input("Introduzca el primer número del rango: "))
num2 = int(input("Introduzca el segundo número del rango: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(f"{i} es un número par")