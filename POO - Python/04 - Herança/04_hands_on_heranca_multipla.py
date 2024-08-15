# Objeto Animal - Classes de Animais - Animais

class Animal:
    def __init__(self, cabeca, dorso, patas):
        self.cabeca = cabeca
        self.dorso = dorso
        self.patas = patas
      #função numero de patas usando uma entrada de dados (input)                
    def numero_patas(self):
        self.n_patas = input("O animal tem: ")
         
        
descricao = Animal("Cabeça e Pescoço", "Peito, ombros e costas", "Pernas, pés e Patas")
descricao.numero_patas()
print("Descrição do Animal:")
print("Cabeça: Rosto, olhos, nariz, ")
print(" ")

class Ave(Animal):
    def __init__(self, cabeca, dorso, patas, Tem_Penas, Possui_Bico, Coloca_Ovos, Sabe_Voar, Cor_Penas):
        super().__init__(cabeca, dorso, patas)  # Chama o construtor da classe pai primeiro
        self.Tem_Penas = Tem_Penas
        self.Possui_Bico = Possui_Bico
        self.Coloca_Ovos = Coloca_Ovos
        self.Sabe_Voar = Sabe_Voar
        self.Cor_Penas = Cor_Penas

    def info(self):
        print(f"Cabeça: {self.cabeca} Dorso: {self.dorso} Patas: {self.patas} Possui Bico: {self.Possui_Bico} Coloca Ovos: {self.Coloca_Ovos} Sabe Voar: {self.Sabe_Voar} Cor das penas: {self.Cor_Penas}")

    def info1(self):
        print("Aves possuem Bicos")
    
    def info2(self):
        print("Aves colocam Ovos")
        
    def info3(self):
        print("Aves possuem Penas")
        
    def info4(self):
        print("Aves voam")
    
    def info5(self):
        print("Algumas Aves não conseguem voar, pois suas asas são muito curtas!")
        
        
bird = Ave(cabeca="cabeça, crista, olhos, bico e pescoço /", dorso="peito, assas, ombros e costas /", patas="pernas, patas e garras  /", Tem_Penas="Sim, pelo corpo todo, exceção do rosto e das patas /", Possui_Bico="Sim /", Coloca_Ovos="Sim /", Sabe_Voar="A maioria das especies consegue voar", Cor_Penas="Vermelhas, pretas com brilho azulado")
print("Informações da Classe Ave")
bird.info()
bird.info1()
bird.info2()
bird.info3()
bird.info4()
bird.info5()
print(" ")
        
        
class mamifero(Animal):
    def __init__(self, cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo):
        super().__init__(cabeca, dorso, patas)
        self.Possui_Tetas = Possui_Tetas
        self.Possui_Pelos = Possui_Pelos
        self.Possui_Bolsa = Possui_Bolsa
        self.Cor_Pelo = Cor_Pelo

    def info(self):
        print(f"Cabeça: {self.cabeca} Dorso: {self.dorso} Patas: {self.patas} Possui Tetas: {self.Possui_Tetas} Possui Pelos: {self.Possui_Pelos} Possui Bolsa: {self.Possui_Bolsa} Cor do Pelo: {self.Cor_Pelo}")
        
        
        
mamario = mamifero(cabeca="Cabeça e Pescoço / ", dorso="Peito, ombros e costas / ", patas="Pernas, pés e Patas /", Possui_Tetas="Sim /", Possui_Pelos="Sim /", Possui_Bolsa="Sim /", Cor_Pelo="Várias Cores")
print("Informações da Classe Mamifero:")
mamario.info()
print(" ")

class cachorro(mamifero):
    def __init__(self, cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo):
        super().__init__(cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo)
        self.Cor_Pelo = Cor_Pelo
        
    def esta_limpo(self):
        print("O Cachorro  não possui Pulgas")
        print("O Cachorro possui Carrapatos!")
           
    def latido(self):
        print("Au Au Au...")

print("Informação do Cachorro:")
cao = cachorro(cabeca="Cabeça, orelhas, olhos, fucinho, boca e pescoço", dorso="Peito, ombros e costas", patas="2 Patas", Possui_Tetas="Sim /", Possui_Pelos="Sim /", Possui_Bolsa="Não /", Cor_Pelo="Amarelo")
cao.esta_limpo()
cao.latido()
print(" ")

class gato(mamifero):
    def __init__(self, cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo):
        super().__init__(cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo)
        self.Cor_Pelo = Cor_Pelo

    def miado(self):
        print("Miau Miau...")
        
    def castrado(self):
        print("O Gato é castrado!")
          
cat = gato(cabeca="Cabeça, orelhas, olhos, fucinho, boca e pescoço /", dorso="Peito, ombros e costas /", patas="2 Patas /", Possui_Tetas="Sim /", Possui_Pelos="Sim /", Possui_Bolsa="Não /", Cor_Pelo="Branco e Preto")
print("Informação do Gato:")
cat.info()
cat.miado()
cat.castrado()
print(" ")

class leao(mamifero):
    def __init__(self, cabeca, juba, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo):
        super().__init__(cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa, Cor_Pelo)
        self.juba = juba
        self.Cor_Pelo = Cor_Pelo
        
    def rei(self):
        print("O Leão é o rei da selva!")
        
Leao = leao(cabeca="Cabeça, orelhas, olhos, fucinho, boca e pescoço", juba="Pelo", dorso="Peito, ombros e costas", patas="2 Patas", Possui_Tetas="Sim /", Possui_Pelos="Sim /", Possui_Bolsa="Não /", Cor_Pelo="Amarelo avermelhado")  
print("Informações do Leão:")
Leao.info()
Leao.rei()
print(" ")

class ornitorrinco(mamifero, Ave):
    def __init__(self, cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa):
        super().__init__(cabeca, dorso, patas, Possui_Tetas, Possui_Pelos, Possui_Bolsa)

    def e_mamifero(self):
        print("Este animal é um mamifero")
        
    def e_ave(self):
        print("Este animal não é uma ave")
        
    def coloca_ovos(self):
        print("Este animal coloca ovos")
        
    def animal_mamario(self):
        print("É um animal mamario!")
        
    def bolsa(self):
        print("Não possui bolsa")




class galinha(Ave):
    def __init__(self, Tem_Penas, Possui_Bico, Coloca_Ovos, Sabe_Voar):
        super().__init__(Tem_Penas, Possui_Bico, Coloca_Ovos, Sabe_Voar)
        
    def e_mamifero(self):
        print("Este animal não é um mamifero")
        
    def e_ave(self):
        print("Este animal é uma ave")
        
    def coloca_ovos(self):
        print("Este animal coloca ovos")
        
    def animal_mamario(self):
        print("Não é um animal mamario!")
        
    def bolsa(self):
        print("Não possui bolsa")






