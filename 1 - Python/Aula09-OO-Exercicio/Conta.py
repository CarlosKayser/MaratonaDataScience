class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, qtd):
        if self.saldo - qtd > self.limite:
            self.saldo -= qtd
            print("Foi sacado:", qtd)
        else:
            print("Saldo insuficiente")

    def depositar(self, depositar):
        if depositar > 0:
            self.saldo += depositar
        else:
            print("Erro no deposito")

    def consultar_saldo(self):
        return self.saldo        