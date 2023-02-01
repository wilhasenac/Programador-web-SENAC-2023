import os
os.system('cls')

lista = [ 5, 6, 2, 9]

soma = 0
contador = 0
quantidade_notas = len(lista)

while contador < quantidade_notas:
    soma += lista[contador]
    contador += 1

print(f'Média das nota é {soma / quantidade_notas}')
