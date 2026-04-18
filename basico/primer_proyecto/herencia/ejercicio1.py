class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} esta trabajando")

    def mostrar(self):
        print(f"{self.nombre} Tiene una salario de {self.salario}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        self.equipo = equipo

    def dirigir(self):
        print(f"{self.nombre} dirige un equipo de {self.equipo} de personas")


class Vendedor(Empleado):
    def __init__(self, nombre, salario, comision):
        super().__init__(nombre, salario)
        self.comision = comision

    def vender(self, monto):
        ganancia = monto * self.comision / 100
        print(f"{self.nombre} gana {ganancia} de comision")


empleado = Empleado("sloower", 2000000)
empleado.trabajar()
empleado.mostrar()

gerente = Gerente("Bauwers", 3500000, 5)
gerente.trabajar()
gerente.mostrar()
gerente.dirigir()

vendedor = Vendedor("hugo", 2800000, 15)
vendedor.trabajar()
vendedor.mostrar()
vendedor.vender(5000000)
