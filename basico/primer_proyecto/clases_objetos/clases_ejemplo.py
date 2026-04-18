class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años. Mi promedio es {self.promedio}")
        
    def es_aprobado(self):
        if self.promedio >= 60:
            return "aprobado"
        else:
            return "reprobado"
        
carlos = Estudiante("Carlos", 20, 75)
maria = Estudiante("Maria", 22, 55)

carlos.presentarse()
print(carlos.es_aprobado())

maria.presentarse()
print(maria.es_aprobado())
