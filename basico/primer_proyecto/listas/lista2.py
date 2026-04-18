lista_nombres = []
for i in range(5):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)

print("Los nombres ingresados son: ", lista_nombres)

lista_nombres.sort()
print("El Orden alfabético es: ", lista_nombres)


consulta_nombre = input("Ingrese un nombre para consultar: ")
if consulta_nombre in lista_nombres:
    print("El nombre", consulta_nombre, "se encuentra en la lista.")
else:
    print("El nombre", consulta_nombre, "no se encuentra en la lista.")
