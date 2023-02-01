import os


def limparTela():
    os.system('cls')

class Vendedor():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Produto():
    def __init__(self, nome, descricao, preco, estoque, vendedor):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao
        self.vendedor = vendedor

class Venda():
    def __init__(self, vendedor, produto, quantidade):
        self.vendedor = vendedor
        self.produto = produto
        self.quantidade = quantidade


limparTela()
nome_vendendor = str(input('Informe o nome do vendendor: '))
telefonte_vendedor = str(input('Informe o numero de telefone: '))

vendedor = Vendedor(nome_vendendor, telefonte_vendedor)
produtos = []
vendas = []


while True:
    opcao = str(input('Voce deseja cadastrar ou comprar '))
    if opcao in ['compra','c']:
        for e in range(len(produtos)):
                      
            print("Nome: "+produtos[e].nome)
            print("Preço: R$ "+produtos[e].preco)
            print('********************************')

        produto_compra = str(input('qual produto deseja comprar? '))
       
        for e in range(len(produtos)):
            if produto_compra in produtos[0].nome:
                qte_compra = int(input('Informe a quantidade da compra'))

                if produtos[e].estoque >= qte_compra:
                    print('da certo')
                else:
                    print('Não tenho estoque suficiente!')
            else:
                print('produto não encontrado')
        


    elif opcao in ['cadastrar','cad']:
        
        nome_produto = str(input('Informe o nome do produto: '))
        descricao_produto = str(input('Informe a descrição: '))
        preco_produto = str(input('Informe o preço do produto: '))
        estoque_produto = int(input('Informe a quantdade em estoque: '))

        produto = Produto(nome_produto, descricao_produto, preco_produto, estoque_produto, vendedor)
        
        produtos.append(produto)

    elif opcao in ['s', 'sair']:
        break   
    
    elif opcao in ['l']:
        limparTela()
        for e in range(len(produtos)):
            
            
            print("Nome: "+produtos[e].nome)
            print("Descrição: "+produtos[e].descricao)
            print("Preço: R$ "+produtos[e].preco)
            print("Quantidade em estoque: "+produtos[e].estoque)
            print("Vendedor: "+produtos[e].vendedor.nome)
            print('********************************')
    else:
        print('opção inválida')
        
