import os
os.system('cls')

def maior(numero1, numero2):
    if numero1 > numero2:
        return f'numero {numero1} é maior que {numero2}'
    elif numero2 > numero1:
        return f'numero {numero2} é maior que {numero1}'
    else:
        return 'Os numeros são iguais'

numero1 = int(input('informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))

print(maior(numero1, numero2))