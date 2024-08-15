# LEN: É usado para contar os itens em diversos tipos de dados, ela possui uma "ação polimorfica", ou seja, ela muda a sua forma de agir dependendo do tipo de dado que for passado para ela.


# Len usado em String Única:
palavra = "Python"
print("String Simples: Palavra Única")
print(palavra)
tamanho = len(palavra)
print(tamanho)
print("Função do Len em uma String única: Ela conta letra por letra")

# Len usado em Frase String:
frase = "Em uma frase grande com utilização dos espaços, eles também são contados pela função Len!"
print("String Completa:")
print(frase)
tamanho = len(frase)
print(tamanho)
print("Função do Len em uma Frase: Até mesmo os espaços, que separaram as palavras são contados por ela!")
print(" ")

# Em lista:
lista = [1, 2, 3, 4, 5]
print("Lista Simples:")
print(lista)
tamanho = len(lista)
print(tamanho) 
print("Igual ocorre com uma string única, ela conta caractere por caractere!")

# Em lista de Strings:
lista_frases = ["O avião caiu no mar", "O céu é azul", "A roda gigante gira"]
print("Lista de Strings:")
print(lista_frases)
tamanho = len(lista_frases)
print(tamanho)
print("Função do Len em uma Lista de Strings: Ele conta a quantidade de itens da lista")
print(" ")

# Em dicionários:
dicionario = {'Caixa:': "Recipiente para guardar objetos", '10 + 50 = ??': 60, 'c': 3}
print(dicionario)
tamanho = len(dicionario)
print(tamanho) 
print("Função do Len em um Dicionario Simples: É contado pela quantidades de ':' chaves")

conjunto_dicionarios = {'abc' : 1234, True : False, 50 : '50'}, {'700' : 700, True : 'True'}, {100 : 100, 'abcd' : 'abcd'}
print(conjunto_dicionarios)
tamanho = len(conjunto_dicionarios)
print(tamanho)
print("Função do Len em um Conjunto de Dicionarios: É contado pela quantidade de dicionarios")
print(" ")


# Em tuplas:

tupla = (1, 2, 3)
print("Tupla:")
print(tupla)
tamanho = len(tupla)
print(tamanho)
print("Função do Len em uma Tupla Simples: É contado pelo número de itens")

conjunto_tuplas = ("abcd", 1234, "ab34"), (True, False), (2.541, 320, 5.15, 200)
print("Conjunto de Tuplas:")
print(conjunto_tuplas)
tamanho = len(conjunto_tuplas)
print(tamanho)
print("Função do Len em um Conjunto de Tuplas: É contado pelo números de Tuplas")
print(" ")

# Len usado em POO
class MinhaColecao:
    def __init__(self, items):
        self.items = items
    
    def __len__(self): # Uso do Len em POO
        return len(self.items)

    

# Criando uma instância da classe MinhaColecao
colecao = MinhaColecao([1, 2, 3, 4, 5])

# Usando a função len() no objeto colecao
print("Minha Coleção: [1, 2, 3, 4, 5]")
print(len(colecao))
print("Função do Len em POO: Depende do tipo de dados, neste caso se trata de uma lista, a regra da Lista é mantida! ")













