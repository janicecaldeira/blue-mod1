# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        return self.idade
    
    def engordar(self):
        self.peso += 3
        return self.peso
    
    def emagrecer(self):
        self.peso -= 1
        return self.peso
    
    def crescer(self):
        self.altura = self.altura + 0.05
        return self.altura

while True:

    parar = input("Deseja incluir um novo usuário? [SIM/NÃO] ").upper()
    if parar != "SIM":
        break

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: ").replace(",","."))
    altura = float(input("Digite sua altura: ").replace(",","."))

    individuo = Pessoa(nome, idade, peso, altura)

    acao = int(input("Menu: \n1-Envelhecer\n2-Crescer\n3-Engordar\n4-Emagrecer\nDigite a opção desejada: "))

    if acao == 1:
        print(f"Você envelheceu e agora tem {individuo.envelhecer()} anos")
        if idade < 21:
            print(f"Por isso cresceu! E tem {individuo.crescer():.2f}m de altura")
    
    elif acao == 2:
        print(f"Você cresceu e agora tem {individuo.crescer():.2f}m de altura")
    
    elif acao == 3:
        print(f"Você engordou e agora pesa {individuo.engordar()} kg")

    elif acao == 4:
        print(f"Você emagreceu e agora pesa {individuo.emagrecer()} kg")
    
    else:
        print("Opção inválida")
        acao = int(input("Digite apenas números de 1 a 4: "))