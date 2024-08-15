# POO (Programação Orientada a Objetos)

# Conceitos de CLASSES e OBJETOS
# "class" (palavra reservada - Criar uma classe) | "pass" (bloco vazio)
# "self" (referência para o objeto)
# Caracteristicas: Recebem o nome de "Atributos da Classe"
# Métodos: São funções dentro de uma Classe. Métodos = Comportamentos encapsulados em objetos
# Atributos = dados encapsulados em objetos
# Encapsulamento = Dados e Métodos são agrupados em objetos

# Desafio: Bicicletaria do João

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
  
    def buzinar(self):
      print("Plim Plim...")      

    def parar(self):
        print("Parando Bicicleta!")
        print("Bicileta Parada!")
        
    def correr(self):
        print("Vrummmmm...")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "Monark", 1998, 500)
b1.buzinar()
b1.parar()
b1.correr()
# Troquei a ordem e adcionei Strings de identificação
print("Modelo:", b1.modelo, "Ano:", b1.ano, "Cor:", b1.cor, "Valor: R$", b1.valor, "reais")

b2 = Bicicleta("rosa", "Caloi", 2019, 900)
Bicicleta.buzinar(b2)
b2.parar()
Bicicleta.correr(b2)


b3 = Bicicleta("roxo", "GTS", 2021, 1300)
print(b3.cor)
b3.parar()

b4 = Bicicleta("prata", "Soul Cycless", 2024, 2100)
print("R$", b4.valor, "reais")



# EXPLICAÇÃO: 







