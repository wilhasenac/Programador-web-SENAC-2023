lista = []
multiplicacao = 1
soma = 0 
contador = 0

while contador < 5:
    elemento = int(input('Informe um elemento para compor a lista: '))
    soma += elemento
    multiplicacao = multiplicacao * elemento
    lista.append(elemento)
    contador += 1

print(f'Todos os elementos: {lista}')
print(f'A soma dos elementos é: {soma}')
print(f'A multiplicação dos elementos é: {multiplicacao}')

