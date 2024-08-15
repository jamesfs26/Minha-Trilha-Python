#[Retorna uma vizualização das chaves do dicionário]

# EXEMPLO 1: Iterando sobre as chaves do dicionário

empresa1 = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

chaves = empresa1.keys()

# Iterando sobre as chaves
for chave in chaves:
    print(chave)
    

# EXEMPLO 2: Verificando a existência de uma chave no dicionário

empresa2 = {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'}

chaves = empresa2.keys()

# Verificando se uma chave específica existe
if 'nome' in chaves:
    print('A chave "nome" existe no dicionário.')
   
else:
    print('A chave "nome" não existe no dicionário.')
   


# EXEMPLO 3: Convertendo as chaves do dicionário para uma lista

empresa3 = {'nome': 'Carlos', 'idade': 40, 'cidade': 'Curitiba'}

chaves = empresa3.keys()

# Convertendo a visão das chaves para uma lista
lista_chaves = list(chaves)
print(lista_chaves)



# EXEMPLO 4: Comparando as chaves de dois dicionários

dicionario1 = {'nome': 'Daniel', 'idade': 35, 'cidade': 'Salvador'}
dicionario2 = {'nome': 'Elena', 'idade': 28, 'estado': 'Bahia'}

chaves1 = dicionario1.keys()
chaves2 = dicionario2.keys()

# Encontrando chaves comuns
chaves_comuns = chaves1 & chaves2  # Usando operador & para interseção
print(chaves_comuns)


# EXEMPLO 5: Usando .keys() em uma função

def imprimir_chaves(dicionario):
    # Usando .keys() para obter as chaves
    chaves = dicionario.keys()
    print("As chaves do dicionário são:")
    for chave in chaves:
        print(chave)

# Exemplo de uso da função
meu_dicionario = {'nome': 'Fernanda', 'idade': 22, 'cidade': 'Florianópolis'}
imprimir_chaves(meu_dicionario)



