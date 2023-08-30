# Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa 
# envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)
        
    def engordar(self, peso_ganho):
        self.peso += peso_ganho
        
    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido
        
    def crescer(self, altura_ganha):
        self.altura += altura_ganha
        
    def mostrarDados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura:.2f} cm")

pessoa = Pessoa(nome="Alice", idade=10, peso=23, altura=120)

print("Dados iniciais da pessoa:")
pessoa.mostrarDados()

pessoa.envelhecer(2)
pessoa.engordar(3)

print("\nDados após envelhecimento e ganho de peso:")
pessoa.mostrarDados()

pessoa.emagrecer(2)
pessoa.crescer(1)

print("\nDados finais da pessoa:")
pessoa.mostrarDados()