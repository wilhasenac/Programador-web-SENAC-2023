import os
os.system('cls')

class Ave():
    def __init__(self, nome):
        self.possui_penas = True
        self.possui_penas = True
        self.possui_assas = True
        self.nome = nome


    def voa(self):
        if self.possui_assas:
            print(f'Sou {self.nome} e estou voando')


class Passeriformes(Ave):
    pass

class Galliformes(Ave):
    def voa(self):
        print(f'Sou um {self.nome} e eu não consigo voar')





   
bem_te_vi = Passeriformes('Bem-te-vi')
galinha = Galliformes('Galinha')
calopsita = Passeriformes('Calopsita')

calopsita.voa()

galinha.voa()

    
