import time

LIMITE_SAQUE=500
SAQUES_MAX=3
numero_de_saques=0

saldo=0

operacao=""

while operacao != "x":
    operacao=input(
'''
Operações disponíveis:
                   
Saque (s)
                   
Depósito (d)
                   
Extrato (e)
                
Sair (x)
                   
'''                 )
    
    if operacao == "s":
        if numero_de_saques < SAQUES_MAX:
            valor_sacado=float(input("Digite o valor a sacar: "))
            if valor_sacado < 0:
                print("Só é possível sacar números positivos")
            elif valor_sacado > saldo:
                print("O valor sacado é superior ao saldo disponível")
            elif valor_sacado > LIMITE_SAQUE:
                print("Valor a ser sacado excede o limite de saque")
            else:
                saldo-=valor_sacado
                numero_de_saques+=1
                print(f"Novo Saldo: R${saldo:.2f}")
        else:
            print("Numero máximo de saques diários foi atingido (3)")
    elif operacao == "d":
        valor_deposito=float(input("Digite o valor a depositar: "))
        if valor_deposito > 0:
            saldo+=valor_deposito
            print(f"Novo Saldo: R${saldo:.2f}")
        else:
            print("Digite um valor positivo para depositar")
    elif operacao == "e":
        print(f"Saldo: R${saldo:.2f}")
    else:
        continue
    time.sleep(1)