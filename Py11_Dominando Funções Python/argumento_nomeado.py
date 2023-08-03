def salvar_carro(marca, modelo, ano, placa):
    #salva no BD
    print(f"Carro inserido com sucesso! \nMarca {marca}, modelo {modelo}, ano {ano}, placa {placa}.")
salvar_carro("Mercedes", "F1", 2023, "axt-000")
salvar_carro(marca="RBR", modelo="F1", ano=2023, placa="bvc-345")
salvar_carro(**{"marca": "Ferrari", "modelo": "F1", "ano": 2013, "placa": "aaa-022"}) #dicionario