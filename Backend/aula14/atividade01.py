import os
os.system('cls')

def numero_invertido(numero):
    numero = str(numero)
    inversao = int(numero[::-1])

    print(f' {numero} -> {inversao}')


numero_invertido(374)
numero_invertido(5431)
numero_invertido(100)