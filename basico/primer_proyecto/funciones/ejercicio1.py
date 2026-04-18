lista_notas = []


def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)


def es_aprobado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


def mostrar_resultados(nombre, promedio, aprovo):

    print("El promedio de las notas es: ", promedio)
    print("El estudiante ", nombre, " esta: ", aprovo)


nombre = input("Ingrese el nombre del estudiante: ")
for i in range(4):
    notas = float(input("Ingrese la nota: "))
    lista_notas.append(notas)

print("las notas son: ", lista_notas)


promedio = calcular_promedio(lista_notas)

aprobado = es_aprobado(promedio)

mostrar_resultados(nombre, promedio, aprobado)
