numero_de_convidados = int(input('Quantos convidados você deseja chamar? '))
lista_de_convidados = []

i = 1

while i <= numero_de_convidados:
    nome_do_convidado = input('Qual o nome do convidado? #' + str(i) +': ').title()
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print ('\nSerão convidadas' ,numero_de_convidados, 'pessoas:')

for convidado in lista_de_convidados:
    print(f'\U0001F31F {convidado}')