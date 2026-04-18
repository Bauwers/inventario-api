try:
    numero = int(input("Ingresa un número: "))
    print ("ingresaste el número:", numero)
except ValueError:
    print("Eso no es un número válido")
finally:
    print("Esto siempre se ejecuta")