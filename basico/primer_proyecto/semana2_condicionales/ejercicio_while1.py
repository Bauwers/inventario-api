num_secret = 42
respuesta = int(input("Adivina el numero secreto: "))
contador = 1
while respuesta != num_secret:
    contador += 1
    print("Respuesta incorrecta, intenta de nuevo.")
    if respuesta < num_secret:
        print("El numero secreto es mayor que", respuesta)
    elif respuesta > num_secret:
        print("El numero secreto es menor que", respuesta)
    respuesta = int(input("Adivina el numero secreto: "))

    print("¡Felicidades! Has adivinado el numero secreto.")

print("El numero de intentos fue:", contador)
