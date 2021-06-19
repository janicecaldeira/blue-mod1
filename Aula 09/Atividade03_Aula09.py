# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

cont = 0
jogos = []
palpites = []
cont_j = 1

quantidade = int(input("Informe quantos jogos desejar gerar: "))

for i in range(quantidade):
    while cont < 6:
        numero = random.randint(1,60)
        if numero not in palpites:
            palpites.append(numero)
            cont += 1
    cont = 0
    palpites.sort()
    jogos.append(palpites)
    palpites = []

print("\n\U0001F340 Aqui estão os jogos, BOA SORTE!")
for j in jogos:
    print(f"Jogo #{cont_j}: {j}")
    cont_j += 1