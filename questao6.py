# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser 
# capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do 
# canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 18
        
    def trocarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido. Escolha um número entre 1 e 100.")
            
    def aumentarVolume(self):
        if self.volume < 20:
            self.volume += 1
            print("Volume aumentado para:", self.volume)
        else:
            print("Volume máximo alcançado.")
            
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuído para:", self.volume)
        else:
            print("Volume mínimo alcançado.")
            
    def mostrarTV(self):
        print(f"Canal: {self.canal}")
        print(f"Volume: {self.volume}")

