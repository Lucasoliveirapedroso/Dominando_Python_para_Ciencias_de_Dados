def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem2(nome):
    print(f"Bem vindo {nome}!")

def exibir_mensagem3(nome="Anonymous"):
    print(f"Bem vindo {nome}")

exibir_mensagem()
exibir_mensagem2(nome="Lucas")
exibir_mensagem3()
exibir_mensagem3(nome='Luque')
