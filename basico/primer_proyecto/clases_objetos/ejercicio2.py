class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - cantidad

    def mostrar_saldo(self):
        print(f"Su saldo restante es {self.saldo}")


cliente1 = CuentaBancaria("Bauwes", 1000000)
cliente1.depositar(500000)
cliente1.retirar(200000)
cliente1.retirar(2000000)
cliente1.mostrar_saldo()
