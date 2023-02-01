d = {
    'maça': 0.30,
    'pera': 0.90,
    'kiwi': 0.98
    }

produto = input('informe o produto: ')

compra = d.get(produto)

if compra != None:
    qte = float(input('informe a quantidade da compra: '))
    compra = compra * qte
    print(f'valor final da compra é de R$ {compra}')
    
else:
    print('Produto não encontrado')
