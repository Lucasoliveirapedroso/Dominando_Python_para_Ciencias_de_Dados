#bloco em python 
def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print("Valor sacado:", valor)
        print("Novo saldo:", saldo)
    else:
        print("Saldo insuficiente.")

sacar(100)

#utiliza 4 espaços fora de indentação  não funciona DEF é a função do python

import time
def pensar_em_python():
    print("pyyyyyyyyyyyyyyyython")
    print("Indeeeentação")
    time.sleep(1)
    print("Sempre usar indentação")

pensar_em_python()