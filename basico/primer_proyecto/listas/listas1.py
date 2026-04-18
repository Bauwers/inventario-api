list_precios = [12000, 45000, 8000, 67000, 23000]

mayor = max(list_precios)
menor = min(list_precios)
promedio = sum(list_precios) / len(list_precios)

print("El precio mayor es:", mayor)
print("El precio menor es:", menor)
print("El precio promedio es:", promedio)

print("Los precios mayores a 20000 son:")
for precio in list_precios:
    if precio > 20000:
        print(precio)
