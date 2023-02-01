import os
os.system('cls')

def multiplo(numero1, numero2):
    if (numero1 % numero2) == 0:
        return True
    else:
        return False


numero1 = int(input('informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))

print(multiplo(numero1, numero2))