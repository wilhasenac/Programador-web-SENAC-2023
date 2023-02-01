'''
escreva um programa que leia dois numeros.Imprima a divisão inteira do primeiro pela segundo,
assim como o resto da divisão. ultilize apenas os operadores de soma e subtração para calcular o resultado.
lembre-se de qee podemos entender o quociente da divisão de dois numero como a quantidade de vezes que podemos
retiraro divisor do dividendo. logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
'''

numero1 = int(input('Informe o divisor: '))
numero2 = int(input('Informe o dividendo: '))
contador = 0
resultado = numero1 - numero2


while resultado >= 0 :
    contador = contador + 1
    resultado = resultado - numero2
else:
    print(contador)
    









