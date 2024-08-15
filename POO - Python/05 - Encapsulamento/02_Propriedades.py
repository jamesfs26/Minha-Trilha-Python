# Palavras reservadas com o "@" são chamadas de "decorators". Elas são uma maneira poderosa e prática de modificar o comportamento de funções ou métodos sem alterar diretamente seu código.
# Os 3 Principais Decoratores: @staticmethod @classmethod @property



# Exemplo - Classe Foo
class Foo:
    def __init__(self, x=None):
        self._x = x # "_x" Atributo Privado

    @property  #Criando um Atributo Gerenciado
    def x(self):
        return self._x or 0
    
    @x.setter #Complemento do @property
    def x(self, value):
        _x = self._x or 0
        self._x = (self._x or 0) + value
    
        
    @x.deleter #Complemento do @property
    def x(self):
        self._x = -1
        
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)














