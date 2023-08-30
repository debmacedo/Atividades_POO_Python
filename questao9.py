# 9. Classe Ponto e Retângulo: Faça um programa completo utilizando funções e classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y.
# b. Possua uma classe chamada Retângulo, com os atributos largura e altura.
# c. Possua uma função para imprimir os valores da classe Ponto
# d. Possua uma função para encontrar o centro de um Retângulo.
# e. Você deve criar alguns objetos da classe Retângulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, 
# que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto 
# que indique os valores de x e y para o centro do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def imprimir(self):
        print("x:", self.x, "| y:", self.y)

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura
        
    def encontrarCentro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

def criarPonto():
    x = float(input("Digite o x do ponto: "))
    y = float(input("Digite o y do ponto: "))
    return Ponto(x, y)

def criarRetangulo():
    print("Digite as coordenadas do vértice inferior esquerdo:")
    ponto_inicial = criarPonto()
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    return Retangulo(ponto_inicial, largura, altura)

def menu():
    while True:
        print("\n1. Criar Retângulo")
        print("2. Encontrar Centro")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            retangulo = criarRetangulo()
            retangulos.append(retangulo)
            print("Retângulo criado com sucesso!")
        elif opcao == 2:
            if len(retangulos) > 0:
                print("Escolha um retângulo:")
                for i, ret in enumerate(retangulos):
                    print(f"{i + 1}. Retângulo com vértice inferior esquerdo em", end=" ")
                    ret.ponto_inicial.imprimir()
                escolha = int(input()) - 1
                if 0 <= escolha < len(retangulos):
                    centro = retangulos[escolha].encontrarCentro()
                    print("Centro do retângulo:", end=" ")
                    centro.imprimir()
                else:
                    print("Opção inválida.")
            else:
                print("Nenhum retângulo criado.")
        elif opcao == 3:
            break
        else:
            print("Opção inválida.")

retangulos = []

menu()