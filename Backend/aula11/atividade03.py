import os
os.system('cls')
d = {
    'maça': [10, 0.30],
    'pera': [10, 0.90],
    'kiwi': [10, 0.98]
    }

vendas = {
    'maça': [0, 0.30],
    'pera': [0, 0.90],
    'kiwi': [0, 0.98]
}


posicaoqte = 0
posicaopreco = 1
produto = 0

while produto != 'fim':
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
        else:
            
            print(f'Produto sem estoque suficiente ! estoque atual {d[produto][posicaoqte]}')   
    else:
        print('Produto não encontrado')
else:
    print('fim da compra')

