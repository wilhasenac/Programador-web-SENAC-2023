import os

def limpa_terminal():
    os.system('cls')

class Operacao:

    def __init__(self,valor, numero_conta, nome_cliente, tipo_operacao):
        self.valor = valor
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.tipo_operacao = tipo_operacao
        
    

class Cliente:

    def __init__(self, nome):
        self.nome = nome
        

class Conta:

    def __init__(self, cliente, saldo, numero):
        self.saldo = saldo
        self.cliente = cliente
        self.numero = numero
        self.__operacoes = []
    
    def resumo(self):
        print(f'Número: {self.numero}, saldo: {self.saldo}, cliente: {self.cliente.nome}')
    
    def sacar(self, valor_saque):
        limpa_terminal()      
        if valor_saque <= self.saldo:
            print('-'*47)
            print(f'Saldo anterior: {self.saldo}')
            print(f'Valor do saque: {valor_saque}')
            self.saldo -= valor_saque
            print('-'*47)
            print(f'Novo saldo: {self.saldo}')
            print('-'*47)

            operacao = Operacao(valor_saque, self.numero, self.cliente.nome, 'Saque')

            self.__operacoes.append(operacao)
        else:
            print('-'*47)
            print('Saldo insuficiente')
            print('-'*47)

    def depositar(self, valor_deposito):
        limpa_terminal()
        print(f'')
        print(f'saldo anterior: {self.saldo}')
        print(f'Valor do deposito: {valor_deposito}')
        self.saldo += valor_deposito

        operacao = Operacao(valor_deposito, self.numero, self.cliente.nome, 'Deposito')

        self.__operacoes.append(operacao)
        print('-' * 47)
        
        print(f'Saldo final: {self.saldo}')
        print('-' * 47)
    
    def extrato(self):
        limpa_terminal()
        for operacao  in self.__operacoes:
            print('-'*47)
            print(f'Cliente da operacao : {self.cliente.nome}')
            print(f'Tipo da operacao : {operacao.tipo_operacao}')
            print(f'valor da operacao : {operacao.valor}')
            print(f'numero da operacao : {operacao.numero_conta}')            
            print('-'*47)
        print(f'----------Saldo final {self.saldo}----------')
    
    def transferir(self):
        
        



limpa_terminal()
nome_cliente = str(input('Informe o nome do cliente: '))
numero_da_conta = str(input('Informe o numero da conta: '))
saldo_inicial = float(input('Informe o valor do saldo inicial: '))
limpa_terminal()

cliente = Cliente(nome_cliente)
conta = Conta(cliente, saldo_inicial, numero_da_conta)

cliente2 = Cliente('joãozinho')
conta2 = Conta(cliente2, 100, '456')

cliente3 = Cliente('kleyslane')
conta3 = Conta(cliente3, 100, '789')

while True:

    print('***********************************************')
    print('   Operações (Daque - Deposito - Extrato - Transferência)')
    
    print('  Para sair do sistema basta digitar "fim" ')
    print('***********************************************')

    movimentacao = str(input('Qual a operação deseja fazer: ').lower())

    if movimentacao in ['sacar', 's', 'saque'] :
        
        valor_saque = float(input('Informe o valor do saque: '))
        conta.sacar(valor_saque)
        
    elif movimentacao in ['deposito', 'depositar', 'd']:
        
        valor_deposito = float(input('Informe o valor do deposito: '))
        conta.depositar(valor_deposito)
    elif movimentacao in ['extrato', 'Extrato', 'e']:
        
        conta.extrato()
    elif movimentacao in ['f', 'fim']:
        break

    elif movimentacao in ['T', 't', 'transferencia', 'transfêrencia']:
        pass
    else:
        limpa_terminal()
        print('Informe uma opção valida')
