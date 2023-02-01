import os
os.system('cls')

#'nome produto'  (qte estoque, valor)
d = {
    
}

vendas = {

}


qte_em_estoque = 0
valor_do_produto = 0.0

posicaoqte = 1
posicaopreco = 0
produto = 0

cont = 0


def cadastrar_produto():
      
    novo_produto = 'produto'
    while novo_produto != 'sair':
        print('Cadastro de produtos para sair do cadastro informe o nome do produto como sair : ')
        novo_produto = str(input('Informe o nome do produto: '))
        if novo_produto != 'sair':
            print('***********************')
            qte_em_estoque = float(input('Informe a quantidade em estoque: '))
            print('***********************')
            valor_do_produto = float(input('Informe o valor do produto: '))
            d[novo_produto] = [valor_do_produto, qte_em_estoque]
            
        else:
            print('fim do cadastro')
            cont = 1 

    else:
        print(d)
        print('Iniciando compra')




while produto != 'fim': 
    if cont == 0:          
        cadastrar_produto()
    

    os.system('cls')    
    produto = input('informe o produto: ')
    print('**********')
    compra = d.get(produto)
    

    if compra != None:
       
            
        qte = int(input('informe a quantidade da compra: '))
        if d[produto][posicaoqte] >= qte: 

            #definindo o valor da compra
            valorcompra = qte * d[produto][posicaopreco]

            #calculando o valor final do estoque
            valor_qte_final = d[produto][posicaoqte] - qte
            d[produto][posicaoqte] = valor_qte_final

            #printando o valor do estoque final
            print(f'valor de estoque final : {d[produto][posicaoqte]}')
                

            #printnado o valor da compra
            print(f'valor final da compra é de R$ {valorcompra}')
            break
        else:
                
            print(f'Produto sem estoque suficiente ! estoque atual {d[produto][posicaoqte]}') 
              
    else:
        print('Produto não encontrado')
else:
    print('fim da compra')

