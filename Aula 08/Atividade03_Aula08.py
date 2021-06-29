# Faça um jogo da forca.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.

import random

palavras = ["AMARELO", "PEIXE", "LARANJA", "MACACO", "PIADA", "GELADO", "AMARGO", "QUERIDA", "UNIVERSO"]

palavra_sorteada = random.choice(palavras)
palavra_sorteada = list('_' * len(palavra_sorteada))

print(' '.join(palavra_sorteada))