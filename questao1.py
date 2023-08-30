# Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        
    def mostraCor(self):
        return self.cor

bola = Bola(cor="verde", circunferencia=20, material="borracha")

print("Cor da bola:", bola.mostraCor())

bola.trocaCor("vermelho")

print("Nova cor da bola:", bola.mostraCor())