class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        
    def mostrar (self):
        print(f"{self.nombre},{self.edad} años, raza {self.raza}")
        
perro = Perro("rex", 3, "Labrador")
perro.mostrar()
        