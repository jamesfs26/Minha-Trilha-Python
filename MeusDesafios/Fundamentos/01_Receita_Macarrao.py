# DESAFIO - Receita de Macarrão


# VARIÁVEL SIMPLES

item1 = ("macarrão")
item2 = ("água")
item3 = ("oléo")
item4 = ("sal")
item5 = ("molho de tomate")
lista_de_itens = (item1, item2, item3, item4, item5)
print("Lista de Itens: ", lista_de_itens)
print(" ")

print("Modo de Preparo:")
acao1 = ("Colocar a água para ferver por 10 minutos a um fogo de 150 graus.")
acao2 = ("Separar 300 gramas de macarrão.")
acao3 = ("Adicionar um fio de óleo na água fervida.")
acao4 = ("Colocar o macarrão para cozinhar na água fervida, por 8 minutos a 150 graus.")
acao5 = ("Adicionar o Sal a gosto.")
acao6 = ("Retirar e escorre o macarrão por 5 minutos.")
acao7 = ("Reserve e adicione o molho de tomate.")

print("Passo 1:", acao1)
print("Passo 2:", acao2)
print("Passo 3:", acao3)
print("Passo 4:", acao4)
print("Passo 5:", acao5)
print("Passo 6:", acao6)
print("Passo 7:", acao7)
print(" ")

# USANDO LISTAS
ingredientes = ["macarrão", "água", "oléo", "sal", "molho de tomate"]
modo_de_preparo = ["Colocar a água para ferver por 10 minutos a um fogo de 150 graus.", 
                   "Separar 300 gramas de macarrão.",
                   "Adicionar um fio de óleo na água fervida.",
                   "Colocar o macarrão para cozinhar na água fervida, por 8 minutos a 150 graus.",
                   "Adicionar o Sal a gosto.",
                   "Retirar e escorre o macarrão por 5 minutos.",
                   "Reserve e adicione o molho de tomate."
                   ]

passo1 = (modo_de_preparo[0])
passo2= (modo_de_preparo[1])
passo3 = (modo_de_preparo[2])
passo4 = (modo_de_preparo[3])
passo5 = (modo_de_preparo[4])
passo6 = (modo_de_preparo[5])
passo7 = (modo_de_preparo[6])
print("Conferir lista de ingredientes: ", ingredientes)
print(" ")

print("Já temos todos os ingredientes!")
print(" ")

print("Modo de Preparo: ")
print("Passo 1:", passo1)
print("Passo 2:", passo2)
print("Passo 3:", passo3)
print("Passo 4:", passo4)
print("Passo 5:", passo5)
print("Passo 6:", passo6)
print("Passo 7:", passo7)
print(" ")

    # USANDO FUNÇÕES
def lista_ingredientes(ingrediente1, ingrediente2, ingrediente3, ingrediente4, ingrediente5):
    
    print(f"Lista de Ingredientes: {ingrediente1}/{ingrediente2}/{ingrediente3}/{ingrediente4}/{ingrediente5}")
    
def preparo(fervendo_agua, separacao_macarrao, oleo_na_agua, cozimento_macarrao, tempero, escorrimento, servir):
        
        print(f"Modo de Preparo: {fervendo_agua} {separacao_macarrao} {oleo_na_agua} {cozimento_macarrao} {tempero} {escorrimento}/{servir}")
        
   # Chamando a função preparo com todos os passos
preparo(
    fervendo_agua="Colocar a água para ferver por 10 minutos a um fogo de 150 graus.",
    separacao_macarrao="Separar 300 gramas de macarrão.",
    oleo_na_agua="Adicionar um fio de óleo na água fervida.",
    cozimento_macarrao="Colocar o macarrão para cozinhar na água fervida, por 8 minutos a 150 graus.",
    tempero="Adicionar o Sal a gosto.",
    escorrimento="Retirar e escorrer o macarrão por 5 minutos.",
    servir="Reserve e adicione o molho de tomate."
    ) 


# USANDO CLASSES E OBJETOS
class receita:
    def __init__(self, ingredientes, modo_preparo):
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        
    def lista_Ingredientes(self):
        print("macarrão", "água", "oléo", "sal", "molho de tomate")
    
        


















