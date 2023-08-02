contatos = {
    'Lucas0@gmail.com': {'nome': 'Lucas0', 'telefone': '1111-1111'},
}

copia = contatos.copy()
copia['Lucas0@gmail.com'] = {'nome': 'Lucas0111'}
print(copia['Lucas0@gmail.com'])

print(contatos['Lucas0@gmail.com'])