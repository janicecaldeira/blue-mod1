# 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
# conte quantas vezes aparece as vogais a,e,i,o,u

cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

frase = input("Digite uma frase: ").lower()

for n in frase:
    if n == "a":
        cont_a += 1

    if n == "e":
        cont_e += 1
    
    if n == "i":
        cont_i += 1
    
    if n == "o":
        cont_o += 1

    if n == "u":
        cont_u += 1

print("\nA frase tem:")

if cont_a > 0:
    print(f'{cont_a} letras(s) "A"')
else:
    print("Não tem letras A")

if cont_e > 0:
    print(f'{cont_e} letras(s) "E"')
else:
    print("Não tem letras E")

if cont_i > 0:
    print(f'{cont_i} letras(s) "I"')
else:
    print("Não tem letras I")

if cont_o > 0:
    print(f'{cont_o} letras(s) "O"')
else:
    print("Não tem letras O")

if cont_u > 0:
    print(f'{cont_u} letras(s) "U"')
else:
    print("Não tem letras U")
