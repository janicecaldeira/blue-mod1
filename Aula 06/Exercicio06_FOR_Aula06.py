# 06 - Escreva um programa onde o usuário digita
# uma frase e essa frase retorna sem nenhuma vogal

frase = input("Digite uma frase: ").upper()

for n in frase:
    if n == "A":
        frase = frase.replace("A","")

    if n == "E":
        frase = frase.replace("E","")
    
    if n == "I":
        frase = frase.replace("I","")
    
    if n == "O":
        frase = frase.replace("O","")

    if n == "U":
        frase = frase.replace("U","")

print(frase)