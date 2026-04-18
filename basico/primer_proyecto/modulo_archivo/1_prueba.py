# with open("prueba.txt", "w") as archivo:
#     archivo.write("Hola mundo\n")
with open("prueba.txt", "a") as archivo:
    archivo.write("segunda linea\n")

with open("prueba.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)