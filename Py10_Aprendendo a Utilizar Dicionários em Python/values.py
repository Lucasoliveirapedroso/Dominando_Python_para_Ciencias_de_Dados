contatos = {
    'Lucas0@gmail.com': {'nome': 'Lucas0', 'telefone': '1111-1111'},
    'Lucas2@gmail.com': {'nome': 'Lucas1', 'telefone': '1111-2222'},
    'Lucas3@gmail.com': {'nome': 'Lucas2', 'telefone': '1111-3333'},
    'Lucas4@gmail.com': {'nome': 'Lucas3', 'telefone': '1111-4444'}
}


resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)