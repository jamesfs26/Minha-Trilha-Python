# Palavra Reservada: "return"
# Funções Python retornam "None" por padrão
# Python permite retornar mais de um valor (algumas linguagens não permitem).

# FUNÇÃO COM OPERAÇÕES MATÉMATICAS:

# Adição (+)

def adicao(a, b):
    return a + b

# Exemplo de uso
print(adicao(50, 30))  # Saída: 80

# Subtração (-)

def subtracao(a, b):
    return a - b

print(subtracao(50, 10)) # Saída: 40

def multiplicacao(a, b, c):
    return a * b * c

print(multiplicacao(10, 4, 5)) # Saída: 200

# Divisão

def divisao(a, b):
    return b / a
print(divisao(2, 50))

# FUNÇÃO CÁLCULO DE SUCESSOR E ANTECESSOR:

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

# Chamando a Função!
print(calcular_total ([15, 25, 86])) # Saída: 126
print(retornar_antecessor_e_sucessor(20)) # Saída: 19, 21


# RETORNANDO "NONE"'

def retornando_padrao():
    print("Retornando o Valor Padrão")
    
print(retornando_padrao()) # Saída: None

def retornando_padrao_direto():
    return None
    
print(retornando_padrao_direto())
    














