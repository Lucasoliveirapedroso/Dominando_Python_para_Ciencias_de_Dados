while True:
    numero = int(input("Digite um número: "))
    if numero  == 77:
        break
    print(numero)

for numero in range(100):
    if numero == 77:
        continue
    print(numero, end=" ")