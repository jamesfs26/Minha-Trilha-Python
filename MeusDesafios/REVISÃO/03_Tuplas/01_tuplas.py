# Em Python, uma tupla é um tipo de dado que permite armazenar uma sequência ordenada de elementos.
# As tuplas são imutáveis, o que significa que, uma vez criadas, seus elementos não podem ser alterados.


# Criando uma Tupla:

tupla_vazia = ()
print(tupla_vazia)

# Tupla de Multiplos Elementos:

multiplos_elementos = (1, 2, 3, 4, 'a', 'b', 'c', 'D', 'E', 'F', "caixa", "Bola", "porta@bol.com", True, False)
print(multiplos_elementos)

# Tupla Elemento Único:

elemento_unico = ("zebra",)
print(elemento_unico)

# Acessando Elementos

elemento_zero = multiplos_elementos[0]
elemento_onze = multiplos_elementos[11]
ultimo_elemento = multiplos_elementos[-1]

print(elemento_zero)
print(elemento_onze)
print(ultimo_elemento)

# Desembalando Tuplas

tupla_desembalada = ('@', '#', "+")

a, b, c, = tupla_desembalada

print(a)
print(b)
print(c)

# Operações com Tuplas

tupla1 = (1, 2, 3, 4)
tupla2 = (4, 5, 6, 7)
tupla3 = tupla1 + tupla2 #Concatenação (combinar 2 tuplas usando "+")

tupla4 = (1, 2, 3)
tupla_repetida = tupla4 * 2 #Repetição (repete os elementos das tuplas)

tupla5 = ('a', 'b', 'c', 'd', 'e')
sub_tupla = tupla5[2:4] #Fatiamento (Obter um subconjunto de uma tupla)

print(tupla3)
print(tupla_repetida)
print(sub_tupla)

# Métodos de Tuplas: count() | index()

# Count()
tupla6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 6, 7, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 1, 7, 3)
count_oito = tupla6.count(8)
count_dois = tupla6.count(2)
count_sete = tupla6.count(7)

print(count_oito)
print(count_dois)
print(count_sete)

# index()
tupla7 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0,)
index_5 = tupla7.index(5)
index_9 = tupla7.index(9)
index_dois = tupla7.index(2)

print(index_5)
print(index_9)
print(index_dois)

# Tuplas VS Listas

#Embora as tuplas e listas sejam sequências em Python, existem algumas diferenças importantes:
#   { Imutabilidade: Tuplas são imutáveis, listas são mutáveis.
#  Sintaxe: Tuplas usam parênteses (), listas usam colchetes [].
#  Performance: Tuplas podem ser mais rápidas e consumir menos memória do que listas.}

# Type Error: Tentando mudar valores de uma tupla

#tupla8 = (1, 2, 3, 4,)
#print(tupla8)

#tupla8[0] = 'a'
#print(tupla8)


