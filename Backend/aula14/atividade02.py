import os
os.system('cls')

def imprime(numero):

    for e in range(numero+1):        
        print(f'{e} ' * e) 
        e + 1
  

numero = int(input('informe um numero: '))
imprime(numero)
