# 1 – Classe Bomba de Combustível
# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel, # ii. valorLitro, # iii. quantidadeCombustivel

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

# b. A classe deve possuir no mínimo esses métodos:

# i. abastecerPorValor( )
# método onde é informado o valor a ser abastecido e mostra
# a quantidade de litros que foi colocada no veículo.

    def abastecerPorValor(self, valor):
        self.quantidadeCombustivel = valor/self.valorLitro
        print(f"Foram abastecidos {self.quantidadeCombustivel:.2f} litros")
        return self.quantidadeCombustivel

# ii. abastecerPorLitro( )
# método onde é informado a quantidade em litros de combustível e mostra o valora ser pago pelo cliente

    def abastecerPorLitro(self, litros):
        valor = self.valorLitro*litros
        print(f"Foram abastecidos {litros} litros e custou R$ {valor:.2f}")
        return self.quantidadeCombustivel

# iii. alterarValor( )
# altera o valor do litro do combustível

    def alterarValor(self,novoValor):
        self.valorLitro = novoValor
        print(f"{self.tipoCombustivel} agora custa R$ {self.valorLitro}")
        return self.valorLitro

# iv. alterarCombustivel( )
# altera o tipo do combustível

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        print(f"Essa bomba agora abastece {self.tipoCombustivel}")
        return self.tipoCombustivel


# v.  alterarQuantidadeCombustivel( )
# altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba

    def alterarQuantidadeCombustivel(self):
        pass

bomba1 = BombaCombustivel("Etanol",4.50,40)

bomba1.abastecerPorValor(50)
bomba1.abastecerPorLitro(25)
bomba1.alterarValor(5.35)
bomba1.alterarCombustivel("Gasolina")
bomba1.abastecerPorValor(50)
bomba1.abastecerPorLitro(25)
bomba1.alterarValor(3.83)
bomba1.alterarCombustivel("Diesel")