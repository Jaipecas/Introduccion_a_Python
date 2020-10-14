def obtenerPrimerNum():
    num1 = int(input("Introduce el primer número del rango: "))
    return num1


def obtenerSegundoNum():
    num2 = int(input("Introduce el segundo número del rango: "))
    return num2


num1 = obtenerPrimerNum()
num2 = obtenerSegundoNum()


def recorrerNumeros():
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(f"{i} es un número par")


recorrerNumeros()
