import os
os.system('cls')
contador = 0
soma = 0
media = 0

while True:
    numero = int(input('Informe o um numero :'))
    if numero != 0:
        soma = soma + numero
        contador = contador + 1
        media = soma / contador
    else: 
        break


print(f'foram exibidos {contador} numeros :')
print(f'A soma é {soma}')
print(f'media é {media}')