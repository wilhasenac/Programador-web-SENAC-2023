import os
os.system('cls')

class Monitor:

    def __init__(self, polegadas, marca, modelo):
        self.polegadas = polegadas
        self.marca = marca
        self.modelo = modelo
    
    def ligar_monitor(self):
        print(f'limgando monitor  de modelo {self.modelo}')
    
    def desligar_monitor(self):
        print(f'desligando monitor de modelo {self.modelo}')


monitor1 = Monitor(19, 'aoc', 'modelo1')

print(monitor1.modelo)

monitor1.desligar_monitor()
