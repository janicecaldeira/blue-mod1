# Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista
# b) maior valor da lista
# c) menor valor da lista
# d) soma de todos os elementos da lista
# e) lista em ordem crescente
# f) lista em ordem decrescente

Lista = [5, 7, 2, 9, 4, 1, 3]
print("A sua lista atual é:", Lista)
print("Tamanho da lista:", len(Lista))
print("Maior valor da lista:", max(Lista))
print("Menor valor da lista:", min(Lista))
print("Soma de todos os elementos da lista:", sum(Lista))
Lista.sort()
print("Lista em ordem crescente:", Lista)
Lista.reverse()
print("Lista em ordem descrescente:", Lista)