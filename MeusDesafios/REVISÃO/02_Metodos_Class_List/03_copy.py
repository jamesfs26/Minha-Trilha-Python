# Retorna uma cópia rasa (shallow copy) da lista.

lista = [1, "python", [40, 30, 20]] # Desafio: Modificar essa segunda lista

copia = lista.copy()

print(id(copia), id(lista))

copia[0] = 35
copia [1] = 12
copia[2] = "50 centavos"


print(copia)
print(lista)

# Id Cópia: 1692767497984 | Id Lista: 1692764524928


# O contéudo exibido no print da lista será o da lista copiada.
# Para ver indentificação das duas listas usamos o "id".




