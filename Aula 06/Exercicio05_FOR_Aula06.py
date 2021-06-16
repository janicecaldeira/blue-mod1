# 05 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

contagem = [10,9,8,7,6,5,4,3,2,1,0]
cont = 0

print("Vamos iniciar a contagem regressiva para a linda queima dos fogos de artifício!\n")

for n in contagem:
    sleep(1)
    print(n)

while True:
    print("\U0001F387    \U0001F386", end=" ")
    cont += 1

    if cont > 10:
        break