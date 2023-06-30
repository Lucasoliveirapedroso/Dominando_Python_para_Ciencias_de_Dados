#old style
nome = "lucas"
idade = 22
profissao = "Data analyst"
linguagem = "SQL"

print("Ola sou %s, tenho %d de idade, quero ser %s estudo Python e %s" %(nome, idade, profissao, linguagem))

#format
print("Ola sou {}, tenho {} de idade, quero ser {} estudo Python e {}.".format(nome, idade, profissao, linguagem))

#format com nome dentro
print("Olá, sou {nome}, tenho {idade} anos, quero ser {profissao}, estudo Python e {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#f-string

print(f"Olá, sou {nome}, tenho {idade} anos, quero ser {profissao}, estudo Python e {linguagem}.")

#formatar com f-string
PI = 3.14159
print(f"Valor de PI: {PI:.3f}")
print(f"Valor de PI: {PI:10.3f}") # passa antes espaço
