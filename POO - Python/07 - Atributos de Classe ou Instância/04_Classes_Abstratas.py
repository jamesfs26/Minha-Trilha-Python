# O @abstractproperty foi substituido pelo @abstractmethod apartir do Python 3.3

from abc import ABC, abstractmethod

class Controle_Remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Controle_TV(Controle_Remoto):
    @property
    def marca(self):
        return "Samsung"

    def ligar(self):
        print("Ligando a TV...")
        print("TV ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")

class Controle_Ar_Condicionado(Controle_Remoto):
    @property
    def marca(self):
        return "LG"

    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ar Condicionado ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Ar Condicionado desligado!")

# Usando as classes concretas
controle_tv = Controle_TV()
controle_tv.ligar()
controle_tv.desligar()
print(controle_tv.marca)

controle_ar = Controle_Ar_Condicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)
