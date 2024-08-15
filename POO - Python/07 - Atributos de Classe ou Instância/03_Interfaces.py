#

explicacao = "Em Python, interfaces não são implementadas da mesma maneira que em linguagens como Java ou C#. Python não possui uma palavra-chave específica para definir uma interface. No entanto, o conceito de interfaces pode ser alcançado usando classes abstratas e métodos abstratos, através do módulo abc (Abstract Base Classes)."

from abc import ABC, abstractmethod

class forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
class Retangulo(forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
        
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
    
class Circulo(forma):
    def __init__(self, raio):
        self.raio = raio
        
        
    def area(self):
        return 3.14 * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * 3.14 * self.raio
    
explicacao = "Forma (class forma(ABC)) é uma classe abstrata porque herda de ABC (Abstract Base Class). Isso significa que você não pode criar uma instância diretamente de Forma."

explicacao = "@abstractmethod: Os métodos area() e perimetro() são métodos abstratos, ou seja, qualquer classe que herda de Forma deve implementá-los."
            
explicacao = "Retangulo e Circulo: Ambas são classes concretas que herdam de Forma e implementam os métodos abstratos area() e perimetro()."

# Usando Interfaces na Prática!
explicacao = "Com essas classes abstratas e métodos, você pode criar uma estrutura similar a uma interface. Qualquer classe que herde de Forma será obrigada a implementar os métodos area() e perimetro():"

# Chamada de Instancia:
retangulo = Retangulo(10, 20)
print(retangulo.area)
print(retangulo.perimetro())

circulo = Circulo(5)
print(circulo.area())


















