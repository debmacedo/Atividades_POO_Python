# 7. Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome,
#  Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este 
# humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos
# criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.idade = 1
        
    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        
    def alterarFome(self, nova_fome):
        self.fome = nova_fome
        
    def alterarSaude(self, nova_saude):
        self.saude = nova_saude
        
    def alterarIdade(self, nova_idade):
        self.idade = nova_idade
        
    def retornarNome(self):
        return self.nome
    
    def retornarFome(self):
        return self.fome
    
    def retornarSaude(self):
        return self.saude
    
    def retornarIdade(self):
        return self.idade
    
    def calcularHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor

meu_bichinho = BichinhoVirtual(nome="Tamagoshi")

meu_bichinho.alterarFome(30)
meu_bichinho.alterarSaude(70)
meu_bichinho.alterarIdade(2)

print("Nome:", meu_bichinho.retornarNome())
print("Fome:", meu_bichinho.retornarFome())
print("Saúde:", meu_bichinho.retornarSaude())
print("Idade:", meu_bichinho.retornarIdade())

humor = meu_bichinho.calcularHumor()
print("Humor:", humor)