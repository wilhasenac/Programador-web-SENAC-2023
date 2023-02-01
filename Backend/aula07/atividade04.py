import os
os.system('cls')
contador = 0
soma = 0
media = 0

while True:
    codigo = int(input('Informe o codigo do produto:'))

    if codigo != 0:
        qte = int(input('Informe a quantidade :'))

        if codigo == 1:
            soma = soma + (qte * 0.5)
        elif codigo == 2:
            soma = soma + (qte * 1)
        elif codigo == 3:
            soma = soma + (qte * 4)
        elif codigo == 5:
            soma = soma + (qte * 7)
        elif codigo == 9:
            soma = soma + (qte * 8)
        else:
            print('Codigo invalido')
            
    else:        
        print('informe uma opção valida')
        break

print(soma)

