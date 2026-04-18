class Productos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        total = self.precio * self.cantidad
        return total

    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)

    def mostrar(self):
        print(f"Nombre {self.nombre} precio {self.precio} cantidad {self.cantidad}")


pc = Productos("accer", 5000000, 5)
teclado = Productos("Redragon", 2540000, 15)
deadema = Productos("ryzer", 18000, 7)

pc.aplicar_descuento(10)
pc.mostrar()
print(pc.valor_total())
teclado.mostrar()
print(teclado.valor_total())
deadema.mostrar()
print(deadema.valor_total())
