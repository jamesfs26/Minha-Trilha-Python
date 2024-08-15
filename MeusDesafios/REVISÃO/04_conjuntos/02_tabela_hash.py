# A "ordem dos elementos" em um conjunto em Python é arbitrária e "não deve ser considerada previsível ou ordenada".
# No entanto, o comportamento observado pode ser explicado pela implementação interna do conjunto em Python.

# Implementação dos Conjuntos:
# Os conjuntos em Python são implementados como "tabelas de hash".
# Isso significa que cada elemento em um conjunto é armazenado em uma posição baseada no valor hash do elemento.

# Tabela de Hash com Números inteiros criados com a Função "range":

for i in range(10): # Cria uma Sequência de 0-10 mostrando as respectivas posições na tabela Hash
    print(f"Hash de {i}: {hash(i)}")


# Tabela Hash - Conjunto de Números Inteiros:

numeros = set([5, 8, 2, 4, 6, 0, 7, 9, 1])

def mostrar_posicoes_hash_numeros(numeros, tamanho_tabela):
    for numero in numeros:
        valor_hash = hash(numero)
        posicao = valor_hash % tamanho_tabela
        print(f"Número: {numero}, Hash: {valor_hash}, Posição: {posicao}")

N = 7

mostrar_posicoes_hash_numeros(numeros, N)


# "EXPLICAÇÃO"

# Tabela Hash Para Números Inteiros:
# Os Valores atribuindos as posições da "Tabela Hash para números inteiros" são exatamente iguais aos aos valores dos números.
# Exemplos: 0 = 0 | 1 = 1 | 2 = 2...
# Um conjunto em Python contendo uma sequência aleatória de números inteiros será impresso como uma sequência semelhante a uma ordenada.
# Isso se deve pelos valores da Tabela Hash serem iguais aos valores inteiros



# Tabela de Hash para Strings:

animais = {"ave", "barata", "cavalo", "doninha", "elefante", "foca", "gato"}

# Função para mostrar valores de hash e posição na tabela de hash
def mostrar_posicoes_hash_animais(animais, tamanho_tabela):
    resultados = []
    for animal in animais:
        valor_hash = hash(animal)
        posicao = valor_hash % tamanho_tabela
        resultados.append((animal, valor_hash, posicao))
    return resultados

# Usando um tamanho de tabela de hash para melhor visualização
N = 10

resultados_animais = mostrar_posicoes_hash_animais(animais, N)

# Exibir os resultados
for animal, valor_hash, posicao in resultados_animais:
    print(f"Animal: {animal}, Hash: {valor_hash}, Posição: {posicao}")



