# ESTRUTURA DE DADOS COM FUNÇÕES:

# Contar Ocorrência em Listas

def contar_ocorrencias(lista, valor):
    return lista.count(valor)

print(contar_ocorrencias([1, 2, 2, 3, 4, 2], 2))

# Filtrar Numeros Pares

def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0] 

print(filtrar_pares([1, 2, 3, 4, 5, 6]))

# Filtrar Numeros impares

def filtrar_impares(numeros):
    return [num for num in numeros if num % 2 == 1] 

print(filtrar_impares([1, 2, 3, 4, 5, 6, 7 , 8, 9]))

# Remover Duplicadas

def remover_duplicados(lista):
    return list(set(lista)) #Set: Remove valores duplicados em uma lista

print(remover_duplicados([1, 2, 3, 8, 1, 5, 2, 4, 6, 7, 8, 9, 1, 2, 5, 0]))
    
# Verificar números Primos

def e_primo(n):
  if n < 2:
      return False
  
    















