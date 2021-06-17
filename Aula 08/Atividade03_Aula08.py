# Faça um jogo da forca.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.

import random

palavras = ["AMARELO", "PEIXE", "LARANJA", "MACACO", "PIADA", "GELADO", "AMARGO", "QUERIDA", "UNIVERSO"]

sorteio = random.randint(0,len(palavras)-1)

forca = palavras[sorteio]

erros = 0
chances = 6
tentativa = ""
print(forca)
while chances != 0:
    tentativa = input("Tente acertar a palavra: ").upper()
    if tentativa == forca:
        print("Parabéns! Você ganhou!")
        chances = 0
    else:
        erros += 1
        chances -= 1
        if chances > 1:
            print("Você ainda tem", chances, "tentativas")
        elif chances == 1:
            print("Cuidado! É a sua última tentativa!")
        else:
            pass

if erros >= 6:
    print("Você perdeu! A palavra era:", forca)