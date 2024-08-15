# BLOCO DE EXPLICAÇÃO - Inicio

# Lista [1, 2 , 3] | Tupla (1, 2, 3) | Dicionário {1, 2, 3}
# * (args) == Tupla () | ** (kwargs) == Dicionário {1, 2, 3}
# Tuplas tem seus valores separados por virgulas
# Quando houver um "*" no código, esse código está associado a "args".
# Quando houver um duplo "**" o código estará associado a "kwargs"
# Para estar associado a um dos métodos, os nomes não precisam estar presentes.

# BLOCO DE EXPLICAÇÃO - Final

def exibir_poema(data_extenso, *tupla, **dicionario):
    texto = "\n".join(tupla)
    autoria = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{autoria}"
    print(mensagem)


exibir_poema(
    "Sexta-feira, 26 de março de 2024",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

print(" ")
print("Desafio 2:")


# NOVO DESAFIO
















