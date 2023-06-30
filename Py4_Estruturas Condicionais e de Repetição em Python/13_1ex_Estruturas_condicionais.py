#condição  básica

saldo = 2000
saque = float(input("Informe o valor para saque: "))

if saldo >= saque:
    saldo -= saque
    print("Valor sacado:", saque)
    print("Novo saldo:", saldo)
else:
    print("Saldo insuficiente.")
