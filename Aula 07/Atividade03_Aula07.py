# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

cont = 0

for i in range(7):
    idade = int(input("Qual a sua idade? "))

    if idade > 18:
        cont += 1

if cont > 0:    
    print(f"{cont} pessoas são maiores de idade")
else:
    print("Ninguém é maior de idade")