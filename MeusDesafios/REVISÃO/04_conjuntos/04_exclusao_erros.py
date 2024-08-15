


# Removendo Elementos [remove(), discard(), pop()]
numeros = set([5, 8, 2, 4, 6, 0, 7, 9, 1, 20, 10, 20]) 

numeros.remove(8) #Remove o valor indicado [Se o valor não estiver no conjunto causa um "Key Error"]
numeros.discard(4) # Descarta o valor indicado [Se o valor não estiver no conjunto nada acontece]
numeros.discard(15) 
numeros.pop() #Remove um elemento aleatório

print("Números:", numeros)
print("Númemero Aleátorio Removido com .pop():", numeros.pop())
print("Números:", numeros)
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros)











