menu = """
    [d] Depósito
    [s] Sacar
    [e] Extrato
    [q] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
            print("Depósito efetuado com sucesso.")
        else:
            print("Digite um valor válido.")

    elif opcao == "s":
        valor_saque = float(input("Valor do saque: "))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente")
        elif excedeu_limite:
            print("Saque excede o limite")
        elif excedeu_saques:
            print("Número de saques excedidos")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: {valor_saque:.2f}\n" 
            numero_saques += 1
            print("Saque efetuado com sucesso.")
        else:
            print("Operação falhou. Digite um valor válido.")

    elif opcao == "e":
        print("============= Extrato ============")
        print("Não foram encontradas operações" if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Digite uma opção válida.")
