def calcular_desconto(valor_total, desconto):
    return valor_total * (1 - desconto)

def formatar_valor(valor):
    return "{:.2f}".format(valor)

num_pedidos = int(input())

valor_total_pedidos = 0.0

for _ in range(num_pedidos):
    pedido, valor = input().split()
    valor = float(valor)
    valor_total_pedidos += valor

cupom_desconto = input()
if cupom_desconto == "10%":
    desconto = 0.1
elif cupom_desconto == "20%":
    desconto = 0.2
else:
    desconto = 0.0

valor_com_desconto = calcular_desconto(valor_total_pedidos, desconto)
valor_formatado = formatar_valor(valor_com_desconto)

print(f"Valor total: {valor_formatado}")
