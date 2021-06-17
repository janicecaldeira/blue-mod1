# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000

for i in range(5):
    peso = float(input("Digite o seu peso: ").replace(",","."))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f"O maior peso informado foi: {maior} kg")
print(f"O menor peso informado foi: {menor} kg")