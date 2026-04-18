import json

productos = [
    {"articulo": "nevera", "precio": 1800000, "stock": 10},
    {"articulo": "lavadora", "precio": 2500000, "stock": 25},
    {"articulo": "monitor", "precio": 950000, "stock": 3},
]


with open("inventario.json", "w") as archivo:
    json.dump(productos, archivo, indent=4)

with open("inventario.json", "r") as archivo:
    informacion = json.load(archivo)
    total = 0
    for producto in informacion:
        if producto["stock"] > 5:
            print(producto["articulo"])
        total += producto["precio"] * producto["stock"]
    
    

    print(f"Total inventario: ${total:,}")
        
    