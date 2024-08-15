


def cadastro_pessoas(nome, idade, profissao, cidade):
    
    print(f"Cliente cadastrado com sucesso! {nome}/{idade}/{profissao}/{cidade}")

# Parametros Posicionais
cadastro_pessoas("João", 53, "Técnico em Informatica", "Parazinho")

# Argumentos nomeados (argumento=valor)
cadastro_pessoas(nome="Rafael", idade=35, profissao="Pedreiro", cidade="Rio de Janeiro")

# Argumentos Nomeados com Chave e Valor (**{Argumento: "Valor"})
cadastro_pessoas(**{"nome": "Marcos", "idade": 25, "profissao": "Engenheiro", "cidade": "Natal"}) # ** = Kwargs


# BLOCO DE EXPLICAÇÃO - Inicio

# Parametros Posicionais: Deve estar sempre na ordem, já que não possui os "Argumentos" como indentificador.
# Nomeação com (argumento=valor): Melhora a vizualização e evita problemas causado por desordem.
# Nomeação com (**{Argumento: "Valor"}): Atribui a estrutura de um dicionario a uma função e converte para (argumento="Valor")


# BLOCO DE EXPLICAÇÃ - Fim















