#[Retorna uma visualização dos valores do dicionário]

# EXEMPLO 1: Iterando sobre os valores do dicionário

meu_dicionario = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

valores = meu_dicionario.values()

# Iterando sobre os valores
for valor in valores:
    print(valor)


# EXEMPLO 2: Verificando a existência de um valor no dicionário

meu_dicionario = {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'}

valores = meu_dicionario.values()

# Verificando se um valor específico existe
if 'Rio de Janeiro' in valores:
    print('O valor "Rio de Janeiro" existe no dicionário.')
else:
    print('O valor "Rio de Janeiro" não existe no dicionário.')


# EXEMPLO 3: Convertendo os valores do dicionário para uma lista

meu_dicionario = {'nome': 'Carlos', 'idade': 40, 'cidade': 'Curitiba'}

valores = meu_dicionario.values()

# Convertendo a visão dos valores para uma lista
lista_valores = list(valores)
print(lista_valores)


# EXEMPLO 4: Somando os valores númericos do dicionario

meu_dicionario = {'a': 10, 'b': 20, 'c': 30}

valores = meu_dicionario.values()

# Somando os valores
soma = sum(valores)
print(f'A soma dos valores é: {soma}')


# EXEMPLO 5: Usando values.() em uma função

def imprimir_valores(dicionario):
    # Usando .values() para obter os valores
    valores = dicionario.values()
    print("Os valores do dicionário são:")
    for valor in valores:
        print(valor)

# Exemplo de uso da função
meu_dicionario = {'nome': 'Fernanda', 'idade': 22, 'cidade': 'Florianópolis'}
imprimir_valores(meu_dicionario)


# EXEMPLO 06: Encontrando valores comuns entre dois dicionários
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'x': 2, 'y': 3, 'z': 4}

valores1 = dicionario1.values()
valores2 = dicionario2.values()

# Encontrando valores comuns
valores_comuns = set(valores1) & set(valores2)
print(valores_comuns)



