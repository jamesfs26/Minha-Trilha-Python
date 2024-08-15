# O Papel do "def" é indicar que o nome da função "exibir_mensagem" não é uma váriavel e sim uma função.
# Parametro: def mensagem_teste(argumento="valor"):

# Exemplo com Parametro (Vazio)
def exibir_mensagem(): 
    print("Primeira Função")
   
# Parametro só com (argumento)
def exibir_mensagem_2(nome): 
    print(f"Boas Vindas{nome}!")

# Parametro com (argumento="Valor")
def exibir_mensagem_3(nome="James Fonseca"):
    print(f"Esse Carro pertence a {nome}!")
    
def exibir_mensagem_4(nome="Valor Não encontrado"):
    print(f"Ocorreu um erro devido {nome}!")

# CHAMANDO A FUNÇÃO!
exibir_mensagem()
exibir_mensagem_2(nome=" San Disk")
exibir_mensagem_3()
exibir_mensagem_3(nome="João Batista")
exibir_mensagem_4(nome="Valor Não encontrado")




# BLOCO DE EXPLICAÇÃO - Inicio

# Só escrever o código com impressão não é o suficiente para "Chamar a Função", ou seja, executar o bloco de código.
# Para executar o código deve ser escrito fora do bloco.
# As Mensagens 2 e 3 em seus blocos possuem o mesmo argumento "nome"
# A mensagem 2 não consta o (="Valor") nesse caso, se torna obrigatório nomea-los na "Chamada da Função"
# Mensagem_4: Para que o "Erro" ocorra deve ser apagar o (="Valor") do Bloco e da Chamada!



# BLOCO DE EXPLICAÇÃO - Fim








