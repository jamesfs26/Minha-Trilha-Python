# List Compression: Serve para encurtar o bloco de uma lista criada apartir de outra.
# Filtro 1: O Bloco está bem espalhado
# Filtro 2: O bloco está comprimido



#Filtro versão 1:

numeros = [1, 52, 41, 35, 852, 50, 21, 90]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    
print(numeros)
print(pares)

print(" ")


# Filtro Versão 2: List Compression

valores = [10, 27, 32, 49, 55, 60, 66, 70, 73]
pares = [valor for valor in valores if valor % 2 == 0]

print(pares)







