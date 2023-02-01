import os
os.system('cls')
soma = 0.0
produto1 = ['maca', 0.30]
produto2 = ['pera', 0.75]
produto3 = ['kiwi', 0.98]

produtos = []
while True:

    produto = input('informe o produto: ')

    if produto == 'fim':
        break
    else:
        if produto in produto1 or produto2 or produto3:
            quantidade = float(input('Informe aquantidade: '))
            if produto in produto1:
                valor = float(produto1[1] * quantidade)
                produtos.append(valor)
            elif produto in produto2:
                valor = float(produto2[1] * quantidade)
                produtos.append(valor)
            else:
                valor = floas(produto3[1] * quantidade)
                produtos.append(valor)
            

        else:
            print('produto não encontrado')

for e in produtos:
    soma = soma + e

print(f'o valor total da compra é de R$ {soma}')
   


