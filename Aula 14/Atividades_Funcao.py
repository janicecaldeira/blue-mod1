# 1. Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.

def somar(n1, n2, n3):
	soma = n1+n2+n3
	print(f"O resultado da soma é {soma}")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

somar(numero1, numero2, numero3)

# 2. Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def valide(n1):
    if n1 > 0:
        print("P")
    elif n1 < 0:
        print("N")
    else:
        print("0")

numero = int(input("Digite um número inteiro: "))

valide(numero)

# 3. Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e
# custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    
    valorSemImposto = custo
    valorDoImposto = taxaImposto*valorSemImposto
    valorComImposto = valorSemImposto + valorDoImposto

    print(f'O produto custa {valorSemImposto} e com impostos custa {valorComImposto}')

taxa = float(input("Digite a taxa de imposto: ").replace(",","."))
produto = float(input("Digite o valor do produto: ").replace(",","."))

somaImposto(taxa,produto)

# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ.
# O salário é pago conforme a quantidade de horas trabalhadas.
# Quando um funcionário trabalha mais de 40 horas ele recebe um
# adicional de 1.5 nas horas extras trabalhadas.

def salarioMes(horasTrabalhadas,valorHora):
    horasRegulares = 40
    adicional = 1.5

    if horasTrabalhadas <= horasRegulares:
        salario = horasTrabalhadas*valorHora
        print(f"Seu salário é {salario}")
    else:
        salario = horasRegulares*valorHora
        horaExtra = horasTrabalhadas - horasRegulares
        salarioExtra = salario + (horaExtra*valorHora*adicional)
        print(f"Seu salário com HE é {salarioExtra}")
    
valorHora = float(input("Digite o valor da sua hora de trabalho: "))
horasTrabalhadas = int(input("Digite quantas horas você trabalhou essa semana: "))

salarioMes(horasTrabalhadas, valorHora)

# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que
# tenha 1,68 e pese 75kg.

def IMC(peso, altura):
    calculo = peso/altura**2
    print(f"O seu IMC é {(calculo):.2f}")

IMC(75,1.68)

# 6. Escreva uma função que, dado um número nota representando
# a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def converte(nota):
    if nota >= 9:
        print("A")
    elif nota >= 8:
        print("B")
    elif nota >= 7:
        print("C")
    elif nota >= 6:
        print("D")
    elif nota <= 4:
        print("F")
    else:
        print("Sua nota é 5 e eu não sei converter")

suaNota = float(input("Qual é a sua nota? ").replace(",","."))

converte(suaNota)

# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.

def compara(num1, num2):
    if num1 > num2:
        print(f"O número {num2} é menor")
    elif num1 < num2:
        print(f"O número {num1} é menor")
    else:
        print("Os números são iguais")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

compara(numero1, numero2)