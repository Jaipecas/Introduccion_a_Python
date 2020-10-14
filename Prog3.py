numPar = int(input("Introduzca un número par: "))
numImpar = int(input("Introduzca un número impar: "))

if numPar % 2 != 0 and numImpar % 2 == 0:
    print(f"El número {numPar} no es par y el número {numImpar} no es impar")
elif numPar % 2 != 0:
    print(f"El número {numPar} no es par")
elif numImpar % 2 == 0:
    print(f"El número {numImpar} no es impar")
else:
    print("Ambos números son correctos")
