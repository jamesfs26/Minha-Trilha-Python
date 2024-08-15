# Váriaveis de Instância: Possui uma Cópia
# Variáveis de Classe: São Únicas


class Estudante:
    escola = "EBAC - Escola Britanica de Artes criativas e tecnologia" # Variável de Classe - Sua criação é semelhante a uma Variável comum (atribuição)
    escola = "DIO - Digital Inovation One"
    
    def __init__(self, nome, matricula): # Variável de Instância - É criada por funções especiais (ex: __init__)
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.escola}"
    
def mostrar_valores(*objs):
        for obj in objs:
            print(obj)
        
# Chamada de Instância  
aluno_1 = Estudante("Rafael Souza", 45)
aluno_2 = Estudante("João Batista", 46)
aluno_3 = Estudante("Cesar Batista", 50)

# Antes da alteração
mostrar_valores(aluno_1, aluno_2, aluno_3) 

# Com a alteração
aluno_1.matricula = 40 
mostrar_valores(aluno_1, aluno_2, aluno_3)

# A alteração da variável de classe afeta todos os estudantes
# A alteração de uma variável de instancia afeta apenas aquele a quem ela pertence








