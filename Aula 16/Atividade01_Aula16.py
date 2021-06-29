# 1.a) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.

class Pessoa():
    def __init__ (self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

# 1.b) Acrescente a classe criada um método para mostrar os dados de uma pessoa.

    def mostrar(self):
        print(f"Nome: {self.nome}\nSobrenome: {self.sobrenome}\nIdade: {self.idade}")

# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e métodos

usuario = Pessoa("Maria", "Alves", 27)
usuario.mostrar()