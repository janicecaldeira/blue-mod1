# Vamos aprimorar o código: cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula 14.
# Faça com que o seu código funcione para vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador. 

# jogador = []
# incluir = ""
# jogadores = {}

# while incluir != "SIM":

#     incluir = input("Deseja incluir um jogador? [SIM/NÃO]").upper()

#     nome = input("Digite o nome do jogador: ")
#     jogador.append(nome)
#     partidas = int(input("Quantas partidas esse jogador jogou: "))
#     jogador.append(partidas)
#     gols = int(input("Quantos gols esse jogador fez: "))
#     jogador.append(gols)
#     for i in jogador:
#         jogadores["Jogador"] = jogador

# print(jogadores)

class Jogador():
    def __init__ (self, nome, partidas, gols):
        self.nome = nome
        self.partidas = partidas
        self.gols = gols
    
    def Desempenho(self):
        aproveitamento = (self.gols/self.partidas)*100
        print(f"O jogador {self.nome} teve {aproveitamento}% de rendimento")

incluir = "SIM"

while incluir == "SIM":

    incluir = input("Deseja incluir um jogador? [SIM/NÃO] ").upper()

    if incluir != "SIM":
        break

    nome = input("Digite o nome do jogador: ")
    partidas = int(input("Quantas partidas esse jogador jogou: "))
    gols = int(input("Quantos gols esse jogador fez: "))

    jogador = Jogador(nome, partidas, gols)

    jogador.Desempenho()

print("Fim")