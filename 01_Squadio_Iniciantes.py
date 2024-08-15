# EXPLICAÇÃO DO DESAFIO
# Regras:
# Entrada: 
# Saída: 



# Solicitar a entrada do usuário
quantidade_passos = int(input("Digite a quantidade de passos que o explorador deve dar na floresta: "))

# Verificar se a quantidade de passos é positiva
if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    # Utilizar um laço de repetição para simular os passos do explorador
    for passo in range(1, quantidade_passos + 1):
        print(f"O explorador deu {passo} passo(s) na floresta.")




