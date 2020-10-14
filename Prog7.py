numPalabras = int(input("Introduzca el número de palabras que va a contener la lista: "))
listaPalabras = []

for i in range(0, numPalabras):
    palabra = input("Introduzca palabra: ")
    listaPalabras.append(palabra)

print("Lista de palabras: ")
for palabra in listaPalabras:
    print(palabra)
