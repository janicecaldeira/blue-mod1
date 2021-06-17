# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

cont = 0
cont_18 = 0
cont_M = 0
cont_20 = 0

print("Informe os dados abaixo")

while cont == 0:
    idade = int(input("Idade: "))

    sexo = input("Sexo (F/M): ").upper()
    while sexo != "F" and sexo != "M":
        sexo = input("Sexo (F/M): ").upper()
    
    continuar = input("Você deseja informar novos dados (SIM/NAO): ").upper()
    while continuar != "SIM" and continuar != "NAO":
        continuar = input("Você deseja informar novos dados (SIM/NAO): ").upper()
    
    if continuar != "SIM":
        cont = 1
    else:
        cont = 0
    
    if idade > 18:
        cont_18 += 1
    
    if sexo == "M":
        cont_M += 1
    
    if sexo == "F":
        if idade < 20:
            cont_20 += 1

if cont_18 > 0:
    print(f"{cont_18} pessoas +18 anos")
else:
    print("Ninguém tem +18 anos")

if cont_M > 0:
    print(f"{cont_M} homem cadastrado")
else:
    print("Nenhum homem cadastrado")

if cont_20 > 0:
    print(f"{cont_20} mulher menor de 20 anos")
else:
    print("Nenhuma mulher menos de 20 anos")