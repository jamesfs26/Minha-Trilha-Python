
# DESAFIO 1: Tupla Par com elementos organizado

tupla_par_organizada = [("Abacaxizeiro", "abacaxi"), ("Bananeira", 'banana'), ("Cajueiro", 'caju'), ("Damasqueiro", 'damasco',), ("Figueira", 'figo')]

dicionario_frutas = dict(tupla_par_organizada)
print("Tupla Par com elementos organizado:")
print(dicionario_frutas)
print(" ")


# DESAFIO 2: Organizando Tupla Desorganizada Manualmente para criar o dicionario

tupla_multiplos_elementos2 = [(1, "caixa"), (2, 'D'), (3, 'b'), (4, 'E'), (5,"Bola"), (6, "porta@bol.com"), (7, True)]

dicionario_multiplos_elementos2 = dict(tupla_multiplos_elementos2)
print("Organizando Tupla Desorganizada Manualmente para criar o dicionario:")
print(dicionario_multiplos_elementos2)
print(" ")


# DESAFIO 3: Tupla com Vários Elementos não Organizado em pares [Elementos Par = Execução | Impar = Error + Mensagem]

tupla_multiplos_elementos = (1, 2, 3, 4, 'a', 'b', 'D', 'E', 'F', "caixa", "Bola", "porta@bol.com", True, False)

# Verificando se o comprimento da tupla é par
if len(tupla_multiplos_elementos) % 2 != 0:
    raise ValueError("A tupla deve ter um número par de elementos para ser convertida em um dicionário:")

# Agrupando os elementos em pares
pares = [(tupla_multiplos_elementos[i], tupla_multiplos_elementos[i+1]) for i in range(0, len(tupla_multiplos_elementos), 2)]

# Criando o dicionário a partir dos pares
dicionario_multiplos_elementos = dict(pares)
print("Tupla com Vários Elementos não Organizados em pares:")
print(dicionario_multiplos_elementos)
print(" ")

# DESAFIO 4: Transformando uma Tupla Impar em um Dicionário

# Tupla com um número ímpar de elementos (7 elementos)
tupla_impar = (1, 2, 3, 4, 'a', 'b', 'c')

# Verificando se o comprimento da tupla é par
if len(tupla_multiplos_elementos) % 2 != 0:
    # Descartar o último elemento
    tupla_multiplos_elementos = tupla_multiplos_elementos[:-1]

# Agrupando os elementos em pares
pares = [(tupla_multiplos_elementos[i], tupla_multiplos_elementos[i+1]) for i in range(0, len(tupla_multiplos_elementos), 2)]

# Criando o dicionário a partir dos pares
dicionario_multiplos_elementos = dict(pares)
print("Transformando uma Tupla Impar em um Dicionário:")
print(dicionario_multiplos_elementos)




