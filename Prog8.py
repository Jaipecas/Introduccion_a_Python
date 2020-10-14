listaPalabras = []
terminaLista = True

while terminaLista:
    palabra = input("Introduzca palabra a insertar en la lista: ")
    listaPalabras.append(palabra)
    respuesta = input("¿Desea introducir más palabras? (si/no): ")
    if respuesta.lower() == "no":
        terminaLista = False

palabraBusqueda = input("Introduzca la palabra que desea buscar: ")
contador = 0

for palabra in listaPalabras:
    if palabraBusqueda == palabra:
        contador += 1

print(f"La palabra se encuentra {contador} veces en la lista")
