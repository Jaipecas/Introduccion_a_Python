num = int(input("Introduzca un número mayor que 0: "))
mitadNum = int(num / 2)
divisores = []

while num <= 0:
    num = int(input("El número tiene que ser mayor que 0, vuelva a introducir un número: "))

for i in range(1, mitadNum + 1):
    if num % i == 0:
        divisores.append(i)

divisores.append(num)

print(f"Los divisores del número {num} son :  {divisores}")
