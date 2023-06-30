#for com texto, objeto a ser percorrido
texto = input("texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS: 
        print(letra, end="")
print()
