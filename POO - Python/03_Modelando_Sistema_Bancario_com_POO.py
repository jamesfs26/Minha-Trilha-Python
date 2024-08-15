from abc import ABC, abstractmethod
from datetime import datetime


def menu():
    menu = '''\n
================ MENU ================
[d]\tdepositar
[s]\tsacar
[e]\textrato
[lc]\tlista de contas
[cu]\tcadastrar usuário
[cc]\tcadastrar conta
[exu]\texcluir usuário
[exc]\texcluir conta
[q]\tsair

=>'''
    return input(menu)

class CLiente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = [] #Lista Vazia
        
    def realizar_transação(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.conta.append(conta) # .append = Adiciona um novo item ao final de uma lista.

class Pessoa_Fisica(CLiente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"  
        self._cliente = cliente
        self._historico = Historico()
      
    @classmethod    #Método de Classe
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property #Atributo Gerenciado
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property 
    def agencia(self):
        return self._agencia
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@") #\n = Sequencia de Escape: É usado para quebrar linhas em Strings, ele quebra a linha no ponto onde está inserido.
            
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realiazado com sucesso!===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é invalido. @@@")
            
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é invalido. @@@")
            return False
        
        return True
    

class Conta_Corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__(saldo, numero, agencia, cliente, historico)
   
    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__
        ])
        
        excedeu_limite = valor > self.historico
        excedeu_saques = numero_saques >= self._limite_saques
        
        if excedeu_limite:
            print("\n@@@ Operação falhou! O Valor do saque excede o limite. @@@")
            
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedidos. @@@")
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """    
     
class Historico:
    def __init__(self):
        self._transacoes = []
      
    @property  
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
       self.transacoes.append(
           {
               "tipo": transacao.__class__.__name__,
               "valor": transacao.valor,
               "data": datetime.now().strftime
               ("%d-%m-%Y %H:%M:%s"),
           }
       )
    
     
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self): 
        return self._valor
        
    def registrar(self, conta):
       sucesso_transacao = conta.sacar(self.valor)
       
       if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
                       
class Deposito(Transacao):            
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            

    
        
       
        
    
# DEPOSITAR
def depositar(saldo, valor, extrato, /):  # Positional only
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

# SACAR
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # Keyword Only
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques foi excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

# EXTRATO
def exibir_extrato(saldo, /, *, extrato):  # Positional only e Keyword only
    print("\n=============== EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===========================================")

# CRIAR USUÁRIO
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if len(cpf) != 11 or not cpf.isdigit():
        print("Entrada inválida. Por favor, digite um CPF com 11 números.")
        return

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return

    nome_completo = input("Informe o nome completo: ")
    if not nome_completo.replace(" ", "").isalpha():
        print("\n@@@ Entrada inválida! Por favor, digite o nome completo usando somente letras e espaços. @@@")
        return

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado): ")

    usuarios.append({"cpf": cpf, "nome": nome_completo, "data de nascimento": data_nascimento, "endereço": endereco})

    print("=== Usuário criado com sucesso ===")

# FILTRAR USUÁRIO
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# CRIAR CONTA
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

# LISTAR CONTAS
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta encontrada.")
    for conta in contas:
        linha = f"""\
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
        print("=" * 100)
        print(linha)


# EXCLUIR CONTA
def excluir_conta(contas):
    numero_conta = input("Informe o número da conta a ser excluída: ")
    conta = [conta for conta in contas if conta["numero_conta"] == numero_conta]

    if conta:
        contas.remove(conta[0])
        print("\n=== Conta excluída com sucesso! ===")
    else:
        print("\n@@@ Conta não encontrada! @@@")

# MAIN
def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 5000
    extrato = ""
    numero_saques = 0
    usuarios = [
        {"cpf": "12345678901", "nome": "João Silva", "data de nascimento": "01-01-1990", "endereço": "Rua A, 123 - Centro - Cidade/UF"},
        {"cpf": "23456789012", "nome": "Maria Oliveira", "data de nascimento": "02-02-1985", "endereço": "Rua B, 456 - Bairro - Cidade/UF"},
        {"cpf": "34567890123", "nome": "José Souza", "data de nascimento": "03-03-1975", "endereço": "Rua C, 789 - Zona Sul - Cidade/UF"}
    ]
    contas = [
        {"agencia": AGENCIA, "numero_conta": "1", "usuario": usuarios[0]},
        {"agencia": AGENCIA, "numero_conta": "2", "usuario": usuarios[1]},
        {"agencia": AGENCIA, "numero_conta": "3", "usuario": usuarios[2]}
    ]

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "cu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "exc":
            excluir_conta(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor, selecione novamente a opção desejada.")

main()