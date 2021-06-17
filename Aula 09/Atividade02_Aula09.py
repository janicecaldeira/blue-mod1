# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

cont = 0
lista = []
par = []
impar = []

while cont == 0:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    continuar = input("Deseja adicionar outro número? [SIM/NÃO]").upper()
    if continuar != "SIM":
        cont += 1
    if numero%2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(lista)
print(par)
print(impar)