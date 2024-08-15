

# Argumentos Posicionais "/"
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
print(" ") 


# Criado por mim! :) :D

def cadastro_pessoas(nome, idade, endereco, profissao, /, cidade, estado, nacionalidade, estado_civil):
    print(nome, idade, endereco, profissao, cidade, estado, nacionalidade, estado_civil)
    
cadastro_pessoas("João Tavares /", "52 anos /", "Rua dos Cocais, nº 56 /", "Arquiteto /", cidade="Serra do Mel /", estado="Rio Grande do Norte /", nacionalidade="Brasileiro /", estado_civil="Casado.")

# Causando Erro
def cadastro_pessoas(nome, idade, endereco, profissao, /, cidade, estado, nacionalidade, estado_civil):
    print(nome, idade, endereco, profissao, cidade, estado, nacionalidade, estado_civil)
    
#ERROR! cadastro_pessoas("João Tavares /", "52 anos /", "Rua dos Cocais, nº 56 /", profissao="Arquiteto /", cidade="Serra do Mel /", estado="Rio Grande do Norte /", nacionalidade="Brasileiro /", estado_civil="Casado.")



# BLOCO DE EXPLICAÇÃO - Inicio

# Argumentos Nomeados "*" (Tupla)
# Argumentos Posicionais "/"
# Argumentos arbitrarios == "**" {Dicionario com "Chave-Valor"}
# Colocar 1 espaço no final de cada parametro para melhorar a vizualização
# BLOCO DE EXPLICAÇÃO - Final
















