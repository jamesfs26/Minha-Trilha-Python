menu = '''

[d] depositar [s] sacar [e] extrato [q] sair

=>'''

saldo = 5000 
limite = 1000
extrato = "" 
numero_saques = 0 
LIMITE_SAQUE = 5 
total_saque = 0  # Variável para armazenar o total dos saques realizados

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor  # Atualiza o saldo com o valor depositado
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou, o valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
      
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE
       
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
          
        elif excedeu_limite:
            print("Operação falhou! O valor de saque supera o limite.")
    
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
    
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo com o valor sacado
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            total_saque += valor  # Atualiza o total de saques realizados
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Total de saques realizados: R$ {total_saque:.2f}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor, selecione novamente a opção desejada.")