# 10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel. ii. valorLitro iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de 
# litros que foi colocada no veículo ii. abastecerPorLitro( ) – método onde é informado a quantidade em
# litros de combustível e mostra o valor a ser pago pelo cliente. iii. alterarValor( ) – altera o valor
# do litro do combustível. iv. alterarCombustivel( ) – altera o tipo do combustível. 
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total 
# na bomba

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")
        else:
            print("Não há combustível suficiente na bomba.")
            
    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"O valor a pagar é R${valor_a_pagar:.2f}.")
        else:
            print("Não há combustível suficiente na bomba.")
            
    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor
        
    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
        
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

bomba = BombaCombustivel(tipoCombustivel="Gasolina", valorLitro=5.0, quantidadeCombustivel=1000.0)

bomba.abastecerPorValor(100)
bomba.abastecerPorLitro(20)
bomba.alterarValor(6.5)
bomba.alterarCombustivel("Álcool")
bomba.alterarQuantidadeCombustivel(1000)

print("\nInformações da bomba de combustível:")
print("Tipo de Combustível:", bomba.tipoCombustivel)
print("Valor por Litro:", bomba.valorLitro)
print("Quantidade de Combustível:", bomba.quantidadeCombustivel)