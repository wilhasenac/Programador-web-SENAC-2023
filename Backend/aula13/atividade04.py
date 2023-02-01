import os
os.system('cls')

def areaQuadrado(lado):
    lado = lado * lado
    print(f'A area do quadrado é {lado} m²')

lado = float(input('informe o primeiro numero: '))

areaQuadrado(lado)