class Operacao:

    def __init__(self,valor, numero_conta, nome_cliente, tipo_operacao):
        self.valor = valor
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.tipo_operacao = tipo_operacao
        
    

class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:

    def __init__(self, cliente, saldo, numero):
        self.saldo = saldo
        self.cliente = cliente
        self.numero = numero
        self.__operacoes = []
    
    def resumo(self):
        print(f'Número: {self.numero}, saldo: {self.saldo}, cliente: {self.cliente.nome}')
    
    def sacar(self, valor_saque):       
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f'Novo saldo: {self.saldo}')

            operacao = Operacao(valor_saque, self.numero, self.cliente.nome, 'Saque')

            self.__operacoes.append(operacao)
        else:
            print('Saldo insuficiente')

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito

        operacao = Operacao(valor_deposito, self.numero, self.cliente.nome, 'Deposito')

        self.__operacoes.append(operacao)

        print(f'Novo saldo: {self.saldo}')
    
    def extrato(self):
        for operacao  in self.__operacoes:
            print('*********')
            print(f'Cliente da operacao {self.cliente.nome}')
            print(f'Tipo da operacao {operacao.tipo_operacao}')
            print(f'valor da operacao {operacao.valor}')
            print(f'numero da operacao {operacao.numero_conta}')
            
            print('*********')

def main():
    cliente = Cliente('Luiz', '8699999-9999')

    conta = Conta(cliente, 0, '85858585')

    conta.depositar(300)
    conta.sacar(100)


    
    
    conta.extrato()

    #conta.resumo()
    print('Executando código')

if __name__ == '__main__':
    main()