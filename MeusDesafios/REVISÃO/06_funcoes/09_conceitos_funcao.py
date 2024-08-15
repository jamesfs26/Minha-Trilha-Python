#


# *args (Função com parâmetros váriaveis)

def parametros_variaveis(*args):
    print("Número de argumentos:", len(args))
    for arg in args:
        print(arg)

parametros_variaveis(1, 2, 3, 4, 5)


# **kwargs (Função com paramêtros nomeados)

def minha_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

minha_func(nome="João", idade=25, cidade="São Paulo")


# return (Função que retorna um valor)

def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)


# yeild (Função que retorna múltiplos valores)

def minha_iteracao():
    yield from [1, 2, 3]
    yield from [4, 5, 6]

for valor in minha_iteracao():
    print(valor)


# default (Função que define um valor padrão para um parâmetro)

def minha_func(a=10):
    return a

print(minha_func())  
print(minha_func(20))  


# lambda (Função anônima)

soma = lambda a, b: a + b
print(soma(2, 3))  












