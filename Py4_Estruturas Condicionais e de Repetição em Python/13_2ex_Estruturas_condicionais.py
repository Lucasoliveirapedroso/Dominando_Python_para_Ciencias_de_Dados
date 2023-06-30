#condição com elif
idade = int(input("Informe a idade: "))

if idade >= 18:
    print("Pode tirar a carteira")
elif idade > 16 and idade < 18:
    print("Pode fazer as aulas online.")
else:
    print("Precisa ter uma idade mínima válida")