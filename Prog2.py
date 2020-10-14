print("Este programa calcula su índice de masa corporal")
peso = float(input("Introduzca su peso: "))
altura = float(input("Introduzca su altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Su IMC es de: %.2f . Usted tiene un peso insuficiente" % imc)
elif 18.5 <= imc <= 24.9:
    print(f"Su IMC es de: %.2f . Usted tiene un peso adecuado" % imc)
elif 25 <= imc <= 26.9:
    print(f"Su IMC es de: %.2f . Usted tiene sobrepeso grado I" % imc)
elif 27 <= imc <= 29.9:
    print(f"Su IMC es de: %.2f . Usted tiene sobrepeso grado II (preobesidad)" % imc)
elif 30 <= imc <= 34.9:
    print(f"Su IMC es de: %.2f . Usted tiene obesidad de tipo I" % imc)
elif 35 <= imc <= 39.9:
    print(f"Su IMC es de: %.2f . Usted tiene obesidad de tipo II" % imc)
elif 40 <= imc <= 49.9:
    print(f"Su IMC es de: %.2f . Usted tiene obesidad de tipo III (mórbida)" % imc)
elif imc > 50:
    print(f"Su IMC es de: %.2f . Usted tiene obesidad de tipo IV (extrema)" % imc)
