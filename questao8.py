# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo 
# menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando 
# pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
# o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível
# criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
        
    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")
        
    def verBucho(self):
        if len(self.bucho) > 0:
            print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está com o estômago vazio.")
            
    def digerir(self):
        if len(self.bucho) > 0:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada no estômago para digerir.")

macaco1 = Macaco(nome="Macaco 1")
macaco2 = Macaco(nome="Macaco 2")

macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("uva")
macaco2.comer("laranja")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer(macaco2.nome)
macaco1.verBucho()