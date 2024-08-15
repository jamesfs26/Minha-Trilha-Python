# Publico: As informações pode ser acessado fora das classes.
# Privado: Apenas as classes conseguem acessas esses dados. Deve ter o _ (underline) iniciando as variaveis.


class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self.__saldo = saldo  # Variável privada
        self.__nro_agencia = nro_agencia  # Variável privada
        
    def depositar(self, valor):
        if valor > 0:  # Verifica se o valor a ser depositado é positivo
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")
        
    def sacar(self, valor):
        if valor > 0:  # Verifica se o valor a ser sacado é positivo
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")
        
    def mostrar_saldo(self):
        return self.__saldo

    def get_agencia(self):
        return self.__nro_agencia

    def set_agencia(self, nro_agencia):
        if isinstance(nro_agencia, int) and nro_agencia > 0:
            self.__nro_agencia = nro_agencia
        else:
            print("Número da agência deve ser um inteiro positivo.")

# Testando a classe Conta
conta = Conta(nro_agencia=2514, saldo=300)
conta.depositar(valor=150)
conta.sacar(100)

# Mostrando o saldo
print(conta.mostrar_saldo())
 
    









