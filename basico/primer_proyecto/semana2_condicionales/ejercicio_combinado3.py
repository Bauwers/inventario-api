limite = int(input("Ingrese la cantudad de numeros: "))
numeros = []
for i in range(limite):
    numero = int(input("Ingrese los numeros: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)
promedio = sum(numeros) / len(numeros)

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)
print("El promedio es:", promedio)
