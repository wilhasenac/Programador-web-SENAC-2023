lista = []
lista_par = []
lista_impar = []

contador = 0

while contador < 5 :
    elemento = int(input('Informe um valor inteiro para adicionar a lista: '))
    lista.append(elemento)

    if elemento % 2 == 0:
        lista_par.append(elemento)
    else:
        lista_impar.append(elemento)
        
    contador += 1

print(f'Lista geral: {lista}')
print(f'Lista de elemento pares: {lista_par}')
print(f'Lista de elemento impares: {lista_impar}')