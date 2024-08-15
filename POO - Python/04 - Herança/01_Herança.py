# HERANÇA:
# Possibilita a reutilização de código comum e uma relação de hierarquia entre Classes.
# Podemos modelar os comportamentos semelhantes em uma Classe “pai” (Ex: automóvel) que conterá os atributos e comportamentos.
# As Classes "filhas" vão herdar esses atributos e comportamentos, sem precisar reescrevê-los reduzindo assim o tempo de desenvolvimento!


# Sintaxe da Herança (Sintaxe Simples)
class A:
    pass

class B(A): # A classe "B" é filha da "A", portanto ela herda todos os seus atributos.
    pass


# Herança Multipla
class C(A, B):
    pass























# Desafio - Veiculo

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)


























