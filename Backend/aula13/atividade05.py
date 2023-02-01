import os
os.system('cls')

def areaTriangulo(base, altura):

     area = ( base * altura ) / 2
     return f'A area do triangulo é {area} m²'

base = int(input('informe a base to triângulo: '))
altura = int(input('Informe a altura do triângulo: '))

print(areaTriangulo(base, altura))

