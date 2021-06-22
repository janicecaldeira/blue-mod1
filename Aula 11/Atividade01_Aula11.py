# Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9
# (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.

lista = [1, 4, 5, 6, 7, 9]
quadrados = {}

for i in lista:
    quadrados[i] = i**2

print(quadrados)

# Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10]
# e cada valor associado é o número ao quadrado.​

quadrados = {}

for i in range(1,11):
    quadrados[i] = i**2

print(quadrados)