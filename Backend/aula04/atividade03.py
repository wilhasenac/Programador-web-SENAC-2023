import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input('informe seu nome: ')
telefonte = input('informe um telefone para contato: ')
opcao = input('você deseja um produto - ( P ) ou servico - ( S ): ').lower()

if( opcao in ['produto', 'p'] ):
    produtos_descricao = input('informe a nome do produto: ')
    print('*'*10)
    print(f'nome: {nome}\nTelefonte: {telefonte}\nProdutos descricao: {produtos_descricao}')
    print('*'*10)

elif( opcao in ['servico', 's'] ):
    descricao_servico = input('informe a descrição do produto: ')
    print('*'*10)
    print(f'Nome:{nome}\nTelefonte: {telefonte}\nDescrição do servico: {descricao_servico}')
    print('*'*10)
else:
    print('Opção invalida')