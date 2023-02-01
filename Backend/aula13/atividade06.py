import os
os.system('cls')

def funcao(lista, palavra):
    if len(lista) > 1:
        print(f'{palavra}s')
    else:
        print(palavra)


funcao([1,2,3,4],"adicionado")
funcao([1],"adicionado")
funcao([1,2],"adicionado")