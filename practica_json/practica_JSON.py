import json
empleados = [
    {"nombre": "Carlos", "Salario": 3500000},
    {"nombre": "Maria", "Salario": 2800000},
]

#guardar info
with open("empleados.json", "w") as archivo:
    json.dump(empleados, archivo, indent=4)
    
#leer info
with open("empleados.json", "r") as archivo:
    datos = json.load(archivo)
    
for empleados in datos:
    print(empleados["nombre"], "-", empleados["Salario"])