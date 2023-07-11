usuarios = []  # lista para armazenar os usuários
contas = []  # lista para armazenar as contas
numero_conta = 1  # número da próxima conta a ser criada

def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço do usuário: ")
    cpf_existente = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    if cpf_existente:
        print("CPF já cadastrado. Não é possível cadastrar o usuário.")
    else:
        usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
        print("Usuário cadastrado com sucesso!")

def cadastrar_conta_corrente():
    global numero_conta
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Não é possível cadastrar a conta.")
    else:
        conta = {'agencia': '0001', 'numero_conta': numero_conta, 'usuario': usuario}
        contas.append(conta)
        numero_conta += 1
        print("Conta corrente cadastrada com sucesso!")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo >= valor and len(extrato) < limite and valor <= limite_saques:
        extrato.append(f"Saque: R$ {valor:.2f}")
        saldo -= valor
        numero_saques += 1
        print("Saque realizado com sucesso!")
    elif saldo < valor:
        print("Saldo insuficiente. Não é possível realizar o saque.")
    elif len(extrato) >= limite:
        print("Limite de saques diários atingido.")
    elif valor > limite_saques:
        print("O valor máximo de saque é R$ 500,00.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    extrato.append(f"Depósito: R$ {valor:.2f}")
    saldo += valor
    print("Depósito realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("Extrato:")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

def menu():
    continuar = True
    while continuar:
        print("----- Sistema Bancário -----")
        print("1 - Cadastrar Usuário")
        print("2 - Cadastrar Conta Corrente")
        print("3 - Saque")
        print("4 - Depósito")
        print("5 - Extrato")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            cadastrar_conta_corrente()
        elif opcao == 3:
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta['numero_conta'] == numero_conta), None)
            if not conta:
                print("Conta não encontrada.")
            else:
                saldo_atual = float(input("Informe o saldo atual da conta: "))
                valor_saque = float(input("Informe o valor do saque: "))
                limite_saques = 500
                limite_diario = 3
                conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
                    saldo=saldo_atual,
                    valor=valor_saque,
                    extrato=conta['extrato'],
                    limite=limite_diario,
                    numero_saques=conta.get('numero_saques', 0),
                    limite_saques=limite_saques
                )
        elif opcao == 4:
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta['numero_conta'] == numero_conta), None)
            if not conta:
                print("Conta não encontrada.")
            else:
                saldo_atual = float(input("Informe o saldo atual da conta: "))
                valor_deposito = float(input("Informe o valor do depósito: "))
                conta['saldo'], conta['extrato'] = depositar(
                    saldo=saldo_atual,
                    valor=valor_deposito,
                    extrato=conta['extrato']
                )
        elif opcao == 5:
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta['numero_conta'] == numero_conta), None)
            if not conta:
                print("Conta não encontrada.")
            else:
                exibir_extrato(
                    saldo=conta['saldo'],
                    extrato=conta['extrato']
                )
        elif opcao == 0:
            continuar = False
            print("Saindo do sistema...")
        else:
            print("Opção inválida. Tente novamente.")

menu()