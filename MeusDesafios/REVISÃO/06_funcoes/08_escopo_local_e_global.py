salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(500))  # 2500


# Novo exemplo
conta_corrente = 3000


def movimentacao(saque):
    global conta_corrente
    conta_corrente -= saque
    return conta_corrente

print(movimentacao(1500))  # 1500










