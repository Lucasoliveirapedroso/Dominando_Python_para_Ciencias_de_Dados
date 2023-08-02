contatos = {"lucas@gmail.com": {"nome": "lucas1", "telefone": "3333-2222"}}

#contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "lucas@gmail.com", {}
) 
print(resultado)