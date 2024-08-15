
# Em Python, um conjunto (set) é uma "coleção não ordenada de elementos únicos", o que significa que não pode haver elementos duplicados.
# Os conjuntos são úteis para armazenar elementos onde a ordem não importa e as duplicatas não são permitidas. 


# Você pode criar um conjunto usando chaves {} ou a função set():

# Chaves {}

animais = {"ave", "barata", "cavalo", "doninha", "elefante", "foca", "gato"} 
print("Animais:",animais)

# Função set([])
numeros = set([5, 8, 2, 5, 4, 8, 6, 0, 7, 0, 9, 1]) 
print("Números", numeros)

# Adcionando elementos

numeros.add(3)
print("Números:", numeros)

# Removendo Elementos [remove(), discard(), pop()]

numeros.remove(8)
numeros.discard(7)
numeros.pop() #Remove um elemento aleatório
print("Números:", numeros)
print("Discartando Números com .discard:", numeros.pop())
print("Números:", numeros)

# Operações de Conjunto:

# União

conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
uniao = conjunto1.union(conjunto2) #Une os valores de dois ou mais conjuntos.
print("União:", uniao)

# Interseção

conjunto3 = {10, 20, 30}
conjunto4 = {50, 20, 10}
juncao = conjunto3.intersection(conjunto4) #Retorna os valores que aparecem em ambos os conjuntos.
print("Junção:", juncao)

# Diferença

diferenca = conjunto3.difference(conjunto4)
print("Diferença:", diferenca) #Retorna o valor único do conjunto A em relação ao B e vice-versa.

# Diferença Simétrica

diferenca_simetrica = conjunto3.symmetric_difference(conjunto4) #Retorna o valor único de ambos os conjuntos.
print("Diferença Simetrica:", diferenca_simetrica)


# Verificação de Subconjunto e Superconjunto

print("Subcojunto:", conjunto3.issubset(conjunto4)) #Retorna um valor Booleano (Todos os valores de A == B?)
print("Subcojunto:", conjunto4.issubset(conjunto3)) #Retorna um valor Booleano (Todos os valores de B == A?)
print("Superconjunto:", conjunto3.issuperset(conjunto4)) #Retorna um valor Booleano (Todos os valores de A != B?)
print("Subcojunto:", conjunto4.issuperset(conjunto3)) #Retorna um valor Booleano (Todos os valores de B != A?)


# {}.isdisjoint - Operação de Conjunto Disjunto


conjunto_a = {10, 20, 30, 40, 50}
conjunto_b = {60, 70, 80, 90}
conjunto_c = {10, 0}

print("Operação de Conjunto entre A e B:", conjunto_a.isdisjoint(conjunto_b))
print("Operação de Conjunto entre A e C:", conjunto_a.isdisjoint(conjunto_c))

# len

tamanho_conjunto = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
print(len(tamanho_conjunto))

# in

conjunto_duplicado = {10, 90, 80, 20, 60, 40, 30, 40, 10, 50, 80, 60, 90, 50, 70,  90, 100}
print(10 in conjunto_duplicado) # O valor "X" se encontra no conjunto? [Retorna um valor Booleano]
print(50 in conjunto_duplicado)
print(11 in conjunto_duplicado)
print(100 in conjunto_duplicado)







