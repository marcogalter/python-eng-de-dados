import textwrap
from datetime import datetime  # Import necessário para trabalhar com data e hora

# Função que exibe o menu de opções e coleta a escolha do usuário
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
    # O textwrap.dedent remove a indentação do texto para exibir o menu corretamente
    return input(textwrap.dedent(menu))

# Função responsável por realizar o depósito
def depositar(saldo, deposito, extrato, transacoes_diarias, LIMITE_TRANSACOES, /):
    # Verifica se o número de transações diárias atingiu o limite
    if transacoes_diarias >= LIMITE_TRANSACOES:
        print("\n@@@ Operação falhou! Você atingiu o limite diário de transações. @@@")
        return saldo, extrato, transacoes_diarias

    # Verifica se o valor do depósito é positivo
    if deposito > 0:
        saldo += deposito  # Atualiza o saldo com o valor do depósito
        # Registra a data e hora da transação
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Adiciona o depósito ao extrato
        extrato += f"{data_hora} - Depósito: R${deposito}\n"
        transacoes_diarias += 1  # Incrementa o número de transações diárias
        print(f"Depósito de R${deposito} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")  # Valor de depósito inválido

    return saldo, extrato, transacoes_diarias

# Função responsável por realizar o saque
def sacar(*, saldo, valor_saque, extrato, numero_saques, LIMITE_SAQUES, limite, transacoes_diarias, LIMITE_TRANSACOES):
    # Verifica se o número de transações diárias atingiu o limite
    if transacoes_diarias >= LIMITE_TRANSACOES:
        print("\n@@@ Operação falhou! Você atingiu o limite diário de transações. @@@")
        return saldo, extrato, numero_saques, transacoes_diarias

    # Condições para verificar se o saque pode ser realizado
    excedeu_saldo = valor_saque > saldo  # Verifica se o saldo é suficiente
    excedeu_limite = valor_saque > limite  # Verifica se o valor do saque excede o limite permitido
    excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número de saques permitidos foi excedido

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedidos. @@@")

    elif valor_saque > 0:
        saldo -= valor_saque  # Deduz o valor do saque do saldo
        # Registra a data e hora da transação
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Adiciona o saque ao extrato
        extrato += f"{data_hora} - Saque: R${valor_saque}\n"
        numero_saques += 1  # Incrementa o número de saques realizados
        transacoes_diarias += 1  # Incrementa o número de transações diárias
        print(f"Saque de R${valor_saque} realizado com sucesso!")
    else:
        print("@@@ Valor de saque inválido! @@@")

    return saldo, extrato, numero_saques, transacoes_diarias

# Função responsável por exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    # Verifica se houve movimentações na conta
    if extrato:
        print(extrato)  # Exibe as transações realizadas
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo}")
    print("==============================\n")

# Função para criar um novo usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números): ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o CPF já está cadastrado

    # Verifica se o usuário já existe
    if usuario:
        print("\n@@@ Já existe um cadastro com esse CPF! @@@")
        return

    # Coleta os dados do novo usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro - Número - Bairro - cidade - Estado): ")

    # Adiciona o novo usuário à lista de usuários
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado conforme solicitado!")

# Função que verifica se um usuário já existe na lista de usuários
def filtrar_usuario(cpf, usuarios):
    # Filtra a lista de usuários pelo CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar uma nova conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário já existe

    # Verifica se o usuário foi encontrado
    if usuario:
        print("\nConta criada conforme solicitado!")
        # Retorna os dados da nova conta
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

# Função que lista todas as contas criadas
def listar_contas(contas):
    # Itera sobre todas as contas e exibe suas informações
    for conta in contas:
        linha = f"""\ 
            Agência:\t{conta['agencia']}
            Conta Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal que controla o fluxo do programa
def main():
    saldo = 0  # Saldo inicial
    limite = 500  # Limite para saques
    extrato = ""  # Armazena o extrato das transações
    numero_saques = 0  # Contador de saques realizados
    LIMITE_SAQUES = 3  # Limite de saques diários
    LIMITE_TRANSACOES = 10  # Limite de transações diárias
    transacoes_diarias = 0  # Contador de transações diárias
    AGENCIA = "0001"  # Agência padrão
    usuarios = []  # Lista de usuários
    contas = []  # Lista de contas

    # Loop principal do programa
    while True:
        opcao = menu()  # Exibe o menu e coleta a escolha do usuário

        # Depósito
        if opcao == "1":
            deposito = float(input("Quanto você deseja depositar? "))
            # Realiza o depósito e atualiza o saldo, extrato e número de transações diárias
            saldo, extrato, transacoes_diarias = depositar(saldo, deposito, extrato, transacoes_diarias, LIMITE_TRANSACOES)

        # Saque
        elif opcao == "2":
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            # Realiza o saque e atualiza o saldo, extrato, número de saques e transações diárias
            saldo, extrato, numero_saques, transacoes_diarias = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                transacoes_diarias=transacoes_diarias,
                LIMITE_TRANSACOES=LIMITE_TRANSACOES
            )

        # Exibir extrato
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        # Criar usuário
        elif opcao == "4":
            criar_usuario(usuarios)

        # Criar conta
        elif opcao == "5":
            numero_conta = len(contas) + 1  # Número da nova conta
            conta = criar_conta(AGENCIA, numero_conta, usuarios)  # Cria a conta

            # Adiciona a conta à lista se for criada com sucesso
            if conta:
                contas.append(conta)

        # Listar contas
        elif opcao == "6":
            listar_contas(contas)

        # Sair do programa
        elif opcao == "0":
            print("Saindo...")
            break

        # Opção inválida
        else:
            print("Operação inválida!")

# Executa a função principal
main()
