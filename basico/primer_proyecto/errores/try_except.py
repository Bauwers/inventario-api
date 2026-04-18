try:
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    print(f"La suma es: {suma}, la resta es: {resta}, la multiplicación es: {multiplicacion}, la división es: {division}")
except ValueError:
    print("Uno de los valores ingresados no es un número válido")
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero")
finally:
    print("Operación finalizada")