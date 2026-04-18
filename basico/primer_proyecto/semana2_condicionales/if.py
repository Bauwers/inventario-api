salario = float(input("Digite su salario:"))
print("Tu salario es de:", salario)
if salario < 1000000:
    print("no debe pagar impuestos")
    print("El valor a recibir es de:", salario)
elif salario >= 1000000 and salario <= 3000000:
    valor_impuesto = salario * 0.10
    print(valor_impuesto, "es el valor del impuesto a pagar (10%)")
    valor_neto = salario - valor_impuesto
    print(valor_neto, "es el valor a recibir con el impuesto incluido")
else:
    valor_impuesto = salario * 0.20
    print(valor_impuesto, "es el valor del impuesto a pagar (20%)")
    valor_neto = salario - valor_impuesto
    print(valor_neto, "Es el valor a recibir con el impuesto incluido")

