# 03 - Faça um script que o usuário escolha um número de início,
# um número de fim, e um número depasso. O programa deve printar todos
# os números do intervalo entre início e fim, "pulando" de acordo com o intervalo passado

inicio = int(input("Escolha um número inicial: "))
fim = int(input("Escolha um número final: "))
intervalo = int(input("Escolha um número de intervalo: "))

texto = " "

for n in range(inicio, fim, intervalo):
    print(n, end=' ')