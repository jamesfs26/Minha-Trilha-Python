
# Dicionario aninhado

modelos_carros = {
    "Carro 1": {"Nome": "Celta",
    "Marca": "Chevrolet",
    "Ano": "2020",
    "Tipo de Combustivel": "Gasolina",
    "4 Portas": "Sim",
    "Valor R$": "30.000"},
    "Carro 2": {"Nome": "Gol",
    "Marca": "Volkswagen",
    "Ano": "2022",
    "Tipo de Combustivel": "Gasolina",
    "4 Portas": "Não",
    "Valor R$": "38.000"        
    },
    "Carro 3": {"Nome": "Uno",
    "Marca": "Fiat",
    "Ano": "2018",
    "Tipo de Combustivel": "Gasolina",
    "4 Portas": "Sim",
    "Valor R$": "32.000"        
    }
    }

# Acessando Valores:
print("Acessando Valores!")
print(modelos_carros["Carro 1"] ["Marca"])
print(modelos_carros["Carro 2"] ["Nome"])
print(modelos_carros["Carro 3"] ["Ano"])
print(" ")

# Adcionando e Modificando Valores:

modelos_carros["Carro 1"] ["Estado de Conservação"] = "Semi-novo" # Adciona
modelos_carros["Carro 2"] ["Valor R$"] = "29,000" # Modifica
modelos_carros["Carro 3"] ["Estado do Pneu"] = "Novo"
modelos_carros["Carro 3"] ["Exclusão"] = "Teste"
print("Adicionando, Modificando Valores!")
print(modelos_carros)
print(" ")


# Removendo Itens:

del modelos_carros["Carro 3"] ["Estado do Pneu"]
del modelos_carros["Carro 3"]["Exclusão"]
print("Removendo Valores e Chaves!")
print(modelos_carros)


