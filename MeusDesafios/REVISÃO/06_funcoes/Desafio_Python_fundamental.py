# DEF e RETURN

# Função com Operadores Aritimeticos

def somando_numeros(a, b):
    return a + b
print(somando_numeros(a=15, b=60))
print(" ")

def diminuindo_numeros(a, b , c, d):
    return a - b - c - d

print(diminuindo_numeros(a=50, b=25, c=8, d=10))
print(" ")

def multiplicando_numeros(a, b, c):
    return a * b * c

print(multiplicando_numeros(a=30, b=10, c=2))
print(" ")

def dividindo_numeros(a, b, c):
    return a / b / c
print(dividindo_numeros(a=50, b=10, c=2))
print(" ")

def multiplos_operadores(a, b, c, d, e, f):
    return a + b - c * d / e * f

print(multiplos_operadores(a=100, b=80, c=50, d=35, e=25, f=70))


def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "impar"
    
print(par_ou_impar(8))
print(par_ou_impar(15))

# Conversão de Temperatura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_para_fahrenheit(0))
print(celsius_para_fahrenheit(25))
    

















