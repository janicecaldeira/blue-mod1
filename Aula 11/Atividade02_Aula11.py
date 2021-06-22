# Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado.
# Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

estoque = {'Batata': 10, 'Guaraná': 5, 'Pipoca': 15, 'Arroz': 0, 'Chocolate': 100}

compra = input("O que deseja comprar? ").title()

print(estoque.get(compra, "Produto Inválido"))