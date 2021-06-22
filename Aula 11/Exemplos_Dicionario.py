
# lista_contatos = [("Maria","9999-5220"), ("João","3595-3595"), ("Pedro","98888-8888"), ("Ana","3454-3454")]

# contatos = dict(lista_contatos)
# print(contatos)

# nome = input("Digite o nome do contato: ").title()
# print(contatos.get(nome, "Não encontrado"))

marvel = {'Chris Evans':'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemworth':'Thor', 'Robert Downey Jr':'Homem de Ferro', 'Scarlett Johansson':'Viúva Negra'}
if 'Hulk' in marvel.values():
    print("Hulk está na lista")
if 'Chris Evans' in marvel.keys():
    print("Bonito demais, senhor amado")

marvel["Robert Deniro"] = "Batman"
print(marvel)

del marvel["Robert Deniro"]
print(marvel)

excluidos = marvel.pop('Mark Ruffalo')
print(excluidos)