# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print("\n*** MENU ***\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")

escolha = int(input("\nDigite o número correspondente à opção desejada: "))

while escolha < 1 or escolha > 5:
    escolha = int(input("Digite uma opção válida: "))

if escolha == 1:
    soma = valor1 + valor2
    print(f"A soma dos números é = {soma}")

elif escolha == 2:
    multiplica = valor1 * valor2
    print(f"A multiplicação dos números é = {multiplica}")

elif escolha == 3:
    if valor1 > valor2:
        print(f"O maior número é = {valor1}")
    elif valor2 > valor1:
        print(f"O maior número é = {valor2}")
    else:
        print("Os números são iguais")

elif escolha == 4:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

else:
    print("Programa encerrado com sucesso")