import time, uuid, re

LIMITE_SAQUE = 500
SAQUES_MAX = 3
AGENCIA = "0001"
NUMERO_BANCO = "999"

usuarios = []

def validacao_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto
    if int(cpf[9]) != digito_verificador1:
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto
    if int(cpf[10]) != digito_verificador2:
        return False
    return True

def saque(*,conta_corrente):
    if conta_corrente == None:
        return
    saldo = conta_corrente["saldo"]
    numero_de_saques = conta_corrente["numero_de_saques"]

    if numero_de_saques < SAQUES_MAX:
        valor_sacado = float(input("Digite o valor a sacar: "))
        if valor_sacado < 0:
            print("Só é possível sacar números positivos")
            time.sleep(1)
        elif valor_sacado > saldo:
            print("O valor sacado é superior ao saldo disponível")
            time.sleep(1)
        elif valor_sacado > LIMITE_SAQUE:
            print("Valor a ser sacado excede o limite de saque")
            time.sleep(1)
        else:
            saldo -= valor_sacado
            numero_de_saques += 1
            conta_corrente["saldo"] = saldo
            conta_corrente["numero_de_saques"] = numero_de_saques
            print(f"Novo Saldo: R${saldo:.2f}")
            time.sleep(1)
    else:
        print("Número máximo de saques diários foi atingido (3)")
        time.sleep(1)

def depositar(conta_corrente):
    if conta_corrente == None:
        return
    valor_deposito = float(input("Digite o valor a depositar: "))
    if valor_deposito > 0:
        saldo = conta_corrente["saldo"]
        saldo += valor_deposito
        conta_corrente["saldo"] = saldo
        print(f"Novo Saldo: R${saldo:.2f}")
        time.sleep(1)
    else:
        print("Digite um valor positivo para depositar")
        time.sleep(1)

def registrar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Este CPF já está registrado.")
            time.sleep(1)
            return

    while True:
        if validacao_cpf(cpf):
            break
        else:
            print("CPF inválido, digite novamente")
            time.sleep(1)
            cpf = input("Digite o CPF: ")
    
    usuario = {"cpf": cpf, "contas_correntes": []}
    usuarios.append(usuario)
    print("Usuário registrado com sucesso!")
    time.sleep(1)
    
    if input("Deseja criar uma conta corrente? (s/n): ") == "s":
        criar_conta_corrente(usuarios, cpf)


def criar_conta_corrente(usuarios):
    cpf = input("Digite o CPF do usuário para criar a conta corrente: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            uuid_str = str(uuid.uuid4())
            uuid_str = uuid_str.replace('-', '')
            uuid_int = int(uuid_str, 16)
            uuid_9digit = str(uuid_int % 10**9)
            uuid_9digit = NUMERO_BANCO +"-"+ uuid_9digit +"-"+ AGENCIA
            conta_corrente = {
                "numero_conta": uuid_9digit,
                "saldo": 0,
                "numero_de_saques": 0
            }
            usuario["contas_correntes"].append(conta_corrente)
            print(f"Conta corrente criada com sucesso! Número da conta: {conta_corrente['numero_conta']}")
            time.sleep(1)
            break
    else:
        print("Usuário não encontrado")

def selecionar_conta_corrente(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            contas = usuario["contas_correntes"]
            if len(contas) == 0:
                print("Usuário não possui conta corrente")
                return None
            for i, conta in enumerate(contas, start=1):
                print(f"{i} - Conta: {conta['numero_conta']}, Saldo: R${conta['saldo']:.2f}")
            opcao = int(input("Selecione o número da conta corrente: "))
            if 1 <= opcao <= len(contas):
                return contas[opcao - 1]
            else:
                print("Opção inválida")
    else:
        print("Usuário não encontrado")
    return None

def menu():
    operacao = ""
    while operacao != "x":
        operacao = input(
            '''
            Operações disponíveis:

            Saque (s)

            Depósito (d)

            Extrato (e)

            Registrar Usuário (r)

            Criar Conta Corrente (c)

            Sair (x)

            ''')

        if operacao == "s":
            saque(conta_corrente=selecionar_conta_corrente(usuarios))
        elif operacao == "d":
            depositar(selecionar_conta_corrente(usuarios), usuarios)
        elif operacao == "e":
            extrato(selecionar_conta_corrente(usuarios), usuarios)
        elif operacao == "r":
            registrar_usuario(usuarios)
        elif operacao == "c":
            criar_conta_corrente(usuarios)
        else:
            continue

menu()

print("Obrigado por utilizar nossos serviços!")
time.sleep(5)
