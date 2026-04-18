numero = int(input("Ingrese un numero del 1 al 10:"))
while numero < 1 or numero > 10:
    print("El numero ingresado no es valido")
    numero = int(input("Ingrese un numero del 1 al 10:"))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)




