# Métodos Especiais ou Métodos Mágicos são usados para definir e manipular objetos.

# __init__ 
class Pessoa:
    def __init__(self, nome, idade): # Inicializador
        self.nome = nome
        self.idade = idade


# __str__
class mulher:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self): # String representado um Objeto.
        return f'{self.nome}, {self.idade} anos'

ela = mulher('Alice', 30)
print(mulher)  


# __repr__
class Homem:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):  # Função "repr"
        return f'Homem({self.nome!r}, {self.idade})' # Valor da função

ele = Homem("Eduardo", "30 anos")
print(repr(Homem))  # Retorna o valor da função "def __repr__" ligado a classe



# __len__
class Paradigmas_de_Programacao:
    def __init__(self, imperativo, declarativo):
      imperativo.self
      declarativo.self
      
    def imperativo(self):
        print("É uma forma de programar que se concentra em dar instruções claras sobre como realizar uma tarefa. Neste estilo de programação, podemos mudar o valor das coisas conforme precisarmos. Usamos comandos simples, como atribuir um valor a uma variável ou fazer uma conta matemática. Também podemos tomar decisões (como se isso acontecer, faça aquilo) e repetir ações várias vezes (como em um loop), podemos organizar nossos comandos em funçõe ou usarmos objetos para representar coisas do mundo real.")
        # alt + z (formata grandes strings para melhor vizualização na tela)
        
    def declarativo(self):
        print("Foca em descrever o que deve ser alcançado, em vez de como alcançá-lo. Em vez de fornecer uma sequência de instruções detalhadas, o programador declara as propriedades e relações que o resultado final deve ter.")
      
      
class paradigma_estruturado(Paradigmas_de_Programacao):
    def __init__(self, imperativo, estruturado):
        super().__init__(imperativo, estruturado)
        self.estruturado = estruturado
        
    def estruturado(self):
        print("É um estilo dentro do paradigma imperativo que se concentra em organizar o código fonte em uma sequência de procedimentos ou funções.")
        
class paradigma_orientado_a_objetos(Paradigmas_de_Programacao):
    def __init__(self, imperativo, Poo):
        super().__init__(imperativo, Poo)
        self.Poo = Poo
        
    def Programacao_Orientado_a_Objetos(self):
        print("É centrado na ideia de (objetos) instância de uma classe, encapsula dados (atributos) e comportamentos (métodos), permitindo interações entre eles para executar tarefas")       
        
    
        
    
        
    










# EXPLICAÇÃO:
# __init__ [É o método inicializador de uma classe, também conhecido como construtor.Ele é chamado quando uma nova instância da classe é criada.]

# __str__ [É usado para retornar uma string representativa de um objeto / ...
# Define o comportamento do objeto quando ele é passado para a função str() ou quando é impresso.]

# __repr__ [Define o comportamento do objeto quando é passado para a função "repr()"...  
# O objetivo é fornecer uma string que poderia ser usada para recriar o objeto.]

# __len__ [Define o comportamento do objeto quando é passado para a função len()...
# Deve retornar o comprimento do objeto.]

# __add__ 


# __getitem__


# __bool__



# Se um método mágico/especial for usado durante a chamada da função, o Python irá buscar na classe correspondente... o método usado (ex: __add__)
# Os "underlines" usados nos métodos especiais são chamados de "Underscore"



nome = "João"
sobrenome = " da Silva Cabral"
print(nome + sobrenome)