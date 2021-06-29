# 2) Crie uma classe chamada Conta para simular as operações de uma conta corrente.
# Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar.
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.

class Conta():
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def Sacar(self, quantia):
        if self.saldo >= quantia:
            self.saldo = self.saldo - quantia
            print(f"Saque efetuado com sucesso. Saldo R$ {self.saldo}")
        else:
            print("Saque não autorizado. Saldo insuficiente")

    def Depositar(self, quantia):
        self.saldo = self.saldo + quantia
        print(f"Depósito efetuado com sucesso. Saldo R$ {self.saldo}")

cliente1 = Conta("Janice Caldeira", 500)

quantia = float(input("Quanto você deseja depositar R$: "))

cliente1.Depositar(quantia)
cliente1.Sacar(150)
cliente1.Depositar(50)
cliente1.Sacar(1000)