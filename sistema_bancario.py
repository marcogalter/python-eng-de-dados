menu = """
----------------------------
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
----------------------------
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Quanto você deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito}\n"
        else:
            print("Valor de depósito inválido!")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor que deseja relizar o saque? "))

            if valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque!")
            elif valor_saque > limite:
                print(f"O valor excede o limite de saque de R${limite}!")
            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R${valor_saque}\n"
                numero_saques += 1
            else:
                print("Valor de saque inválido!")
        else:
            print("O limite de saque diário foi atingido, tente novamente amanhã!")
        
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo}")
        print("==============================\n")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação inválida!")
        break
