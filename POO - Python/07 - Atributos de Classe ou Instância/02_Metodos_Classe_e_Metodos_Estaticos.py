# Método de Classe: @classmethod
# Método "Self" = Aponta para a instância de classe
# Ao se usar o Método de Classe o "self" é trocado pelo "cls"

# Método Estatico: @staticmethod

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def Criar_de_Data_Nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18 
    
    

p = Pessoa.Criar_de_Data_Nascimento(1994, 10, 26, "Santos")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(25))
print(Pessoa.e_maior_idade(15))




















