import time

LIMITE_SAQUE=500
SAQUES_MAX=3
numero_de_saques=0

usuarios = {}

saldo=0

operacao=""

def saque(*,usuarios, conta_corrente):
    saldo = usuarios[conta_corrente]["saldo"]
    numero_de_saques = usuarios[conta_corrente]["numero_de_saques"]

    if numero_de_saques < SAQUES_MAX:
        valor_sacado = float(input("Digite o valor a sacar: "))
        if valor_sacado < 0:
            print("Só é possível sacar números positivos")
        elif valor_sacado > saldo:
            print("O valor sacado é superior ao saldo disponível")
        elif valor_sacado > LIMITE_SAQUE:
            print("Valor a ser sacado excede o limite de saque")
        else:
            saldo -= valor_sacado
            numero_de_saques += 1
            usuarios[conta_corrente] = {"saldo": saldo, "numero_de_saques": numero_de_saques}
            print(f"Novo Saldo: R${saldo:.2f}")
    else:
        print("Numero máximo de saques diários foi atingido (3)")

def depositar(conta_corrente,usuarios):
    
    valor_deposito=float(input("Digite o valor a depositar: "))
    if valor_deposito > 0:
        saldo = usuarios[conta_corrente]["saldo"]
        saldo+=valor_deposito
        usuarios[conta_corrente] = {"saldo": saldo}
        print(f"Novo Saldo: R${saldo:.2f}")
    else:
        print("Digite um valor positivo para depositar")

def extrato(conta_corrente,usuarios):
    saldo = usuarios[conta_corrente]["saldo"]
    print(f"Saldo: R${saldo:.2f}")

def validacao_cpf(cpf):
    if len(cpf) == 11:
        primeiro1 = int(cpf[0]) * 10
        primeiro2 = int(cpf[1]) * 9
        primeiro3 = int(cpf[2]) * 8
        primeiro4 = int(cpf[3]) * 7
        primeiro5 = int(cpf[4]) * 6
        primeiro6 = int(cpf[5]) * 5
        primeiro7 = int(cpf[6]) * 4
        primeiro8 = int(cpf[7]) * 3
        primeiro9 = int(cpf[8]) * 2

        seg_primeiro1 = int(cpf[0]) * 11
        seg_primeiro2 = int(cpf[1]) * 10
        seg_primeiro3 = int(cpf[2]) * 9
        seg_primeiro4 = int(cpf[3]) * 8
        seg_primeiro5 = int(cpf[4]) * 7
        seg_primeiro6 = int(cpf[5]) * 6
        seg_primeiro7 = int(cpf[6]) * 5
        seg_primeiro8 = int(cpf[7]) * 4
        seg_primeiro9 = int(cpf[8]) * 3
        seg_primeiro10 = int(cpf[9]) * 2

        soma_validacao = (primeiro1 + primeiro2 + primeiro3 + primeiro4 + primeiro5 + primeiro6 + primeiro7 + primeiro8 + primeiro9)
        divisao_soma = (soma_validacao // 11)
        resto = (soma_validacao - (11 * divisao_soma))

        soma_validacao_2 = (seg_primeiro1 + seg_primeiro2 + seg_primeiro3 + seg_primeiro4 + seg_primeiro5 + seg_primeiro6 + seg_primeiro7 + seg_primeiro8 + seg_primeiro9 + seg_primeiro10)
        divisao_soma_2 = (soma_validacao_2 // 11)
        resto_2 = (soma_validacao_2 - (11 * divisao_soma_2))

        val_1 = False
        val_2 = False
        val_3 = False
        val_4 = False

        if(resto <=1) and (cpf[9] == 0):
            val_1 = True
        if( resto >=2 and resto < 10) and (11 - resto == cpf[9]):
            val_2 = True
        if( resto_2 <=1 ) and (cpf[10] == 0):
            val_3 = True
        if ( resto_2 >=2 and resto_2 < 10 ) and (11 - resto_2 == cpf[10]):
            val_4 = True
        else: ()

        if (val_1 == True or val_2 == True) and (val_3 == True or val_4 == True):
            return True
        else:
            return False

    else: 
        return False

def registrar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    while True:
        if validacao_cpf(cpf):
            break
        else:
            print("CPF inválido, digite novamente")
            cpf = input("Digite o CPF: ")
    usuarios[cpf] = {"nome": nome, "logradouro": logradouro, "CPF": cpf}
    print("Usuário registrado com sucesso!")
    
def menu():
    while operacao != "x":
        global operacao
        operacao=input(
        '''
        Operações disponíveis:
                        
        Saque (s)
                        
        Depósito (d)
                        
        Extrato (e)
        
        Registrar Usuário (r)
        
        Criar Conta Corrente (c)
                        
        Sair (x)
                        
        '''                 )
            
        if operacao == "s":
            saque()
        elif operacao == "d":
            depositar()
        elif operacao == "e":
            extrato()
        elif operacao == "r":
            print("Usuário registrado com sucesso!")
        elif operacao == "c":
            print("Conta corrente criada com sucesso!")
        else:
            continue

menu()

print("Obrigado por utilizar nossos serviços!")
time.sleep(500)