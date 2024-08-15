# Código da Aula - Inicio

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

# Fim - Código da Aula


# Somando
def multiplicar(a, b):
    return a * b
print(multiplicar(a=15, b=20))

# Multiplicando
def calculando(c, d, ambos):
    final = ambos(c, d)
    print(f"O resultado da operação {c} * {d} = {final}")


calculando(25, 40, multiplicar)  # O resultado da operação 25 * 40 = 1000











