
# A classe dict em Python possui vários métodos úteis:

# METODOS ÚTEIS CLASS 'DICT':

# keys() 
meu_dicionario = {
    "nome": "Carlos",
    "idade": 50,
    "cidade": "Bragança Paulista",
    "Estado": "São Paulo",
    "Profissão": "Lenhador",
    
    }


chaves = meu_dicionario.keys() #[Retorna uma visão das chaves do dicionário]
print(chaves)

# Values()

valores = meu_dicionario.values() #[Retorna uma visão dos valores do dicionário]
print(valores)

# Items()

itens = meu_dicionario.items() # [Retorna uma visão dos pares chave-valor do dicionário]
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

for chave in meu_dicionario: # Retorna o "Nome" das Chaves [  {"Idade":}   ]
    print(chave)

for valor in meu_dicionario.values(): # Retorna o "Valor" das chaves [     {idade: "30"}   ]
    print(valor)

for chave, valor in meu_dicionario.items(): # Iterando sobre pares chave-valor
    print(chave, valor)




















