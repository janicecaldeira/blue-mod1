# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já esteja lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

cont = 0
lista = []

while cont == 0:
    valor = int(input("Digite um valor: "))
    continuar = input("Deseja adicionar outro valor? [SIM/NÃO]").upper()
    if continuar != "SIM":
        cont += 1
    if valor not in lista:
        lista.append(valor)        

lista.sort()

print(lista)