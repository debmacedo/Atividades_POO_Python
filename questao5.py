# 5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir 
# os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: 
# alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais
# atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
        
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para o saque.")

minha_conta = ContaCorrente(numero_conta=12345, nome_correntista="Mário")

print("Número da conta:", minha_conta.numero_conta)
print("Nome do correntista:", minha_conta.nome_correntista)
print("Saldo:", minha_conta.saldo)

minha_conta.alterarNome("Jhonny")
print("Novo nome do correntista:", minha_conta.nome_correntista)
