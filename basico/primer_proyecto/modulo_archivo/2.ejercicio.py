# with open("empleados.txt", "w") as archivo:
#     archivo.write("=== NOMBRE y SALARIO ===\n\n")
#     for i in range(3):
#         nombre = input("Ingresa un nombre: ")
#         salario = input("Ingresa un salario: ")
#         archivo.write(f"{nombre} - {salario} \n")

# with open("empleados.txt", "r") as archivo:
#     contenido1 = archivo.read()
#     contenido = archivo.readlines()

# precios = []
# for linea in contenido:
#     partes = linea.split("-")
#     precio = int(partes[1])
#     precios.append(precios)
# print(contenido1, contenido)

linea = "carlos - 3500000"
partes = linea.split("-")
salario = int(partes[1])
print(salario)
print(type(salario))


with open("empleados.txt", "w") as archivo:
    for i in range(3):
        nombre = input("Ingrese nombre: ")
        salario = int(input("Ingrese el salario: "))
        archivo.write(f"{nombre} - {salario}\n")
        
with open("empleados.txt", "r") as archivo:
    print(archivo.read())

with open("empleados.txt", "r") as archivo:
    
    lineas = archivo.readlines()
    salarios = []
    for linea in lineas:
        partes = linea.split("-")
        salarios.append(int(partes[1]))
    promedio = sum(salarios) / len(salarios)

    print(promedio)
