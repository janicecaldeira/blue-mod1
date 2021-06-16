# 04 - Desenvolva um código em que o usuário vai entrar vários
# números e no final vai apresentar a soma deles
# (o usuário vai dizer quantos números serão informados antes de começar)

soma = 0

quantidade = int(input("Quantos números você deseja somar? "))

for n in range(quantidade):
    numero = int(input("Digite o número a ser somado: "))
    soma = soma + numero

print(f"A soma dos números é = {soma}")