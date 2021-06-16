# 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

numero = int(input("Digite um número: "))

print(f"Os divisores de {numero} são:")

for n in range(1, numero):
    if numero % n ==0:
        print(n)