# return
# orientação a objeto

# for

# frutas = ["abacaxi","laranja","melancia","morango","pera"]

# quantidade_elementos = len(frutas)

# print(quantidade_elementos)

# elemento = frutas[3]

# print(elemento)

# for indice, elemento in enumerate(frutas):
#     print(indice, elemento)


# função

# def educado(nome_da_pessoa):
#     print(f"Olá {nome_da_pessoa}, seja muito bem vindo à Blue!")

# nome = input("Qual seu nome? ")


def autoriza(ano):
    idade = 2021-ano

    if idade < 16:
        print("NEGADO")

autorizado = autoriza(1990)

if autorizado == 'NEGADO':
    print("Você não pode votar")

else:
    print("Você está velho")


