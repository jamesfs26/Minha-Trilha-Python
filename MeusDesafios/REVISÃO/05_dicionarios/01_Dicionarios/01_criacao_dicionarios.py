# Dicionarios: Permitem armazenar pares de chave-valor, onde cada chave única é associada a um valor.

# Criando um dicionário vazio:
meu_dicionario = {}

# Criando um dicionário usando Chaves:
meu_dicionario = {
    "nome": "Rafael",
    "idade": 20,
    "cidade": "Londrina",
    "Estado": "Paraná",
    "Profissão": "Arquiteto",
    "Exclusão": "Teste",
    }

# Criando um dicionario usando a classe "dict":

Carros = dict(carro="Palio", ano=2018, valor="R$ 34.000")
print()
# Acessando Valores:
print(meu_dicionario["idade"])
print(meu_dicionario["cidade"])
print(meu_dicionario["Profissão"])

# Adcionando e Modificando Valores:
meu_dicionario["Endereço"] = "Rua dos Macacos, Nº 71, centro, Nepal-SP" # Adciona
meu_dicionario["Profissão"] = "Engenheiro" # Modifica
print(meu_dicionario["Profissão"])
print(meu_dicionario)

# Removendo Itens:

del meu_dicionario["Endereço"]
Exclusão = meu_dicionario.pop("Exclusão")
idade = meu_dicionario.pop("idade")

# METODOS ÚTEIS CLASS 'DICT':

# keys() 

chaves = meu_dicionario.keys() #[Retorna uma vizualização das chaves do dicionário]
print(chaves)

# Values()

valores = meu_dicionario.values() #[Retorna uma visualização dos valores do dicionário]
print(valores)

# Items()

itens = meu_dicionario.items() # [Retorna uma visualização dos pares chave-valor do dicionário]
print(itens)

# Get()

idade = meu_dicionario.get("idade", "Não Especificado")
print(idade)

# update()

outro_dicionario = {"Idade": 30, "cidade": "João Pessoa"} # Atualiza o dicionário com os pares chave-valor de outro dicionário, iterável de pares ou chave-valor.
meu_dicionario.update(outro_dicionario)
print(meu_dicionario)

# clear()

meu_dicionario.clear()
print(meu_dicionario)


# iteração sobre Dicionarios:

for chave in meu_dicionario:
    print(chave)


for valor in meu_dicionario.values(): # Iterando sobre valores
    print(valor)


for chave, valor in meu_dicionario.items(): # Iterando sobre pares chave-valor
    print(chave, valor)
