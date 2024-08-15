# Construtor:
# Desconstrutor:

# __init__

class galo:
    def __init__(self, nome, raça, cor, peso, altura, altura_do_canto, acordado=True):
        print("Inicializando a Classe...")
        self.nome=nome
        self.raça=raça
        self.cor=cor
        self.peso=peso
        self.altura=altura
        self.altura_do_canto=altura_do_canto
        self.acordado=acordado
       
       # __del__         
    def __del__(self):
        print("Removendo a Instância da Classe")
        
    def som_do_animal(self):
        print("cocoricó, cocorocó")    
 

g = galo("Dudu", "Serama", "vermelho, laranja e preto", "300 gramas", "20 cm", "médio")  
g.som_do_animal()           

# Removendo com "del"
print("Ola mundo")

del g

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")





















