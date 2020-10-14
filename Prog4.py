numPar = int(input("Introduzca un número par: "))

if numPar % 2 != 0:
    print(f"{numPar} no es un número par")
else:
    print("El número introducido es par")
    numImpar = int(input("Introduzca un número impar: "))
    if numImpar % 2 == 0:
        print(f"{numImpar} no es un número impar")
    else:
        print("El número introducido es impar")
