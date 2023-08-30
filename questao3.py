# Classe Retângulo: Crie uma classe que modele um retângulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias 
# para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        
    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b
        
    def retornarLados(self):
        return self.lado_a, self.lado_b
    
    def calcularArea(self):
        return self.lado_a * self.lado_b
    
    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

comprimento = float(input("Informe o comprimento do local: "))
largura = float(input("Informe a largura do local: "))

local = Retangulo(comprimento, largura)

area = local.calcularArea()
perimetro = local.calcularPerimetro()

print(f"Área do local: {area} metros quadrados")
print(f"Perímetro do local: {perimetro} metros")

area_piso = 1 
qtd_pisos = area / area_piso

comprimento_rodape = 0.1 
qtd_rodapes = perimetro / comprimento_rodape

print(f"Quantidade de pisos necessários: {qtd_pisos:.2f}")
print(f"Quantidade de rodapés necessários: {qtd_rodapes:.2f}")