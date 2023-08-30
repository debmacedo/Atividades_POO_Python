# Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudarLado(self, novoLado):
        self.lado = novoLado
        
    def retornarLado(self):
        return self.lado
    
    def calcularArea(self):
        return self.lado*self.lado

quadrado = Quadrado(lado=5)
print("Tamanho do lado:", quadrado.retornarLado())
print("Área do quadrado:", quadrado.calcularArea())

quadrado.mudarLado(10)
print("Novo tamanho do lado:", quadrado.retornarLado())
print("Nova área do quadrado:", quadrado.calcularArea())