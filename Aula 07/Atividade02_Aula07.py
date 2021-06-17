# Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

cont = 0

numero = int(input("Eba, vamos aprender a tabuada! Digite um número de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Digite um número de 1 a 10: "))

print(f"\U0001F4D2 Tabuada do {numero}")
for n in range(10):
    cont += 1
    total = numero * cont
    print(f"{numero} x {cont} = {total}")