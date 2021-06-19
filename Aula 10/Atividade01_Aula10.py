# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes,
# utilizando o for e o if, verifique quais clientes são maiores de idade
# e quais são menores de idade e mostre na tela a seguinte frase para cada um deles:
# 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e  também quantos são maiores e quantos são menores de idade.

lista_completa = []
nomes = []
idades = []
cont_maior = 0
cont_menor = 0

for i in range(2):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade > 18:
        cont_maior += 1
    else:
        cont_menor += 1
    nomes.append(nome)
    idades.append(idade)
    lista_completa = nomes + idades
    
print(f"Nessa lista tem {cont_maior} maiores de idade e {cont_menor} menores de idade")

for n in lista_completa:
    if idade > 18:
        print(f"{nome} é maior de idade")
    
