# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

soma = 0
cont = 0

for n in range(6):
    numero = int(input("Digite um número inteiro: "))
    cont += 1
    if (numero%2) == 0:
        soma = numero + soma
    else:
        pass

print(f"\nForam digitados {cont} números\nA soma dos números pares é = {soma}")