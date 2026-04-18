productos = {
    1: {"nombre": "laptop", "precio": 2500000, "cantidad": 3},
    2: {"nombre": "celular", "precio": 1500000, "cantidad": 20},
    3: {"nombre": "tablet", "precio": 1000000, "cantidad": 15},
}


def calculo_total(productos):
    total = 0
    for producto in productos.values():
        total += producto["precio"] * producto["cantidad"]
    return total


def stock_mayor(productos):
    for producto in productos.values():
        if producto["cantidad"] > 5:
            print(producto["nombre"])


for producto in productos.values():
    print(producto["nombre"], "-", producto["precio"], "-", producto["cantidad"])

calculo = calculo_total(productos)
print("El valor total de todos los producto es: ", calculo)
stock_mayor(productos)
