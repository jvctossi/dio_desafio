#Desadio 1 - Operações Bancárias

menu = """
[1] Depositar
[2] Sacar
[3] Exibir extrato

[0] Sair

"""



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
total_saque = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor que deseja depositar na sua conta: "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + f"\n Depósito de R$ {deposito} realizado com sucesso."
        else:
            print("Valor informado para depósito inválido, por favor informar novamente o valor desejado.")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            if saldo > 0:
                saque = float(input("Informe o valor que deseja sacar da sua conta: "))
                if saque <= 0:
                    print("Valor informado para saque inválido, por favor informar novamente o valor desejado.")
                total_saque = total_saque + saque
                if ((saque <= limite and saque <= saldo) and total_saque <= limite):
                    numero_saques = numero_saques + 1
                    saldo = saldo - saque
                    extrato = extrato + f"\n Saque de R$ {saque} realizado com sucesso."
                else:
                    print("Saldo indisponível em conta ou excedeu o limite de saque disponível por dia na sua conta que é de R$ 500,00")
                    total_saque = total_saque - saque
            else:
                print("Saldo indisponível em conta!")
        else:
            print("Número de saque diário excedido! Selecione outra opção ou 0 para sair")

    elif opcao == "3":
        print(f"{extrato} \n Saldo: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada")
    
