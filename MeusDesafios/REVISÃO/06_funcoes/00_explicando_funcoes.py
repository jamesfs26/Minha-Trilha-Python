# BLOCO DE EXPLICAÇÃO! [Inicio]

# Em Python, funções são blocos de código reutilizáveis que executam uma tarefa específica.
# Elas podem receber entradas (argumentos) e retornar uma saída.
# Estrutura básica de uma função em Python:
# "Palavra-Chave" + "nome_da_funcao" + ("parametros"):
# "parametros" são os valores que a função recebe.
# "Código da Função" é o "bloco de código" que será executado quando a função for chamada.
# Funções possuem a mesma ideia de estrutura usadas nas estruturas de repetições e condicionadas.
# Estrutura de código que comporta apenas 4 linhas - Bloco iniciado após ":"(dois ponntos).
# valor_de_retorno é o valor que a função retorna ao chamar
# Parametros = Entradas | Retornos = Saídas


# BLOCO DE EXPLICAÇÃO! [Fim]



# Função com Argumentos:
def soma(a, b):
    return a + b
resultado = soma(50, 20)
print(resultado)

def saudacao(): # Chamar a Função "função()"
    print("Olá, Mundo!")
    
    
# Parametrôs Padrão:
def total(a, b=0): # "Defalt" = se você chamar a função sem fornecer um valor para b, o valor padrão será usado (0).
    return a + b


# Tipos Definidos:

def soma(a: int, b: int) -> int: # A Função aceita apenas parametrôs do tipo "Inteiros"
    return a + b


# Função Recursiva
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)





# BLOCO DE EXPLICAÇÃO! [Inicio]

# Funções em Python devem ser definidas antes de serem usadas.
# Funções podem receber parametros (inseridos) ou parametros default (opcional)
# As funções podem ter tipos de parâmetro explicitamente definidos.
# As funções podem retornar valores.
# As funções têm seu próprio escopo (área de visibilidade), onde as variáveis e constantes são definidas.
# Funções possuem uma lista de conceitos que permitem várias ações.
# [Esses métodos são usados para manipular e processar os argumentos e valores de volta da função.]


# BLOCO DE EXPLICAÇÃO! [Fim]


# CONCEITOS E FUNÇÕES:

# "*args" ou "**kwargs": [permite que uma função receba um número variável de argumentos posicionais:]

def minha_func(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)
    
minha_func(1, 2, 3, nome="João", idade=25)  # imprime: a: 1, args: (2, 3), kwargs: {'nome': 'João', 'idade': 25}

# 



