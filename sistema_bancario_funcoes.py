import textwrap

def menu():
    menu = """\n
    ===========MENU===========
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar usuário
        [5] Criar conta
        [6] Listar contas
        [0] Sair
    ==========================
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R${deposito}\n"
        print(f"Depósito de R${deposito} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, numero_saques, LIMITE_SAQUES, limite):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedidos. @@@")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R${valor_saque}\n"
        numero_saques += 1
        print(f"Saque de R${valor_saque} realizado com sucesso!")
    else:
        print("@@@ Valor de saque inválido! @@@")
    
    return saldo, extrato, numero_saques  # Adicionei numero_saques aqui

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo}")
    print("==============================\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um cadastro com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro - Número - Bairro -cidade - Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereco": endereco})
    print("Usuário criado conforme solicitado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada conforme solicitado!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            deposito = float(input("Quanto você deseja depositar? "))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "2":
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato, numero_saques = sacar(  # Recebe numero_saques atualizado
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,  # numero_saques sendo passado corretamente
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Operação inválida!")

main()
