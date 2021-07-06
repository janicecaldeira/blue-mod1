# 01 Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior,
# crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado.
# Não esqueça que os lançamentos são feitos de forma randômica.

from random import randint

class Lancador():

    def __init__ (self, dado, moeda):
        self.dado = dado
        self.moeda = moeda

    def moeda_joga(self):
        sorte = randint(0,1)
        if sorte == 0:
            print("Cara")
    
        else:
            print("Coroa")

    def dado_joga(self):
        sorte = randint(1,6)
        print(f"Você tirou o número {sorte}")

jogada = Lancador("dado","moeda")

while True:
    usuario = input("Você deseja lançar moeda ou dado?\nOu digite sair: ").lower()

    if usuario == "moeda":
        jogada.moeda_joga()

    elif usuario == "dado":
        jogada.dado_joga()

    elif usuario == "sair":
        break

    else:
        print("Opção inválida")