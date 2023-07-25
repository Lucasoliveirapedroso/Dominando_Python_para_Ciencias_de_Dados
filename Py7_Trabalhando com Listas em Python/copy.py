lista = []

lista.append(1)
lista.append("python")
lista.append([40,50,60])

l2 = lista.copy()

l2[0] = 2

print(l2)
print(lista)