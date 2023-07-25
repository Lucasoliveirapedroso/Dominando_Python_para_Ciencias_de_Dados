#issubset é um método de conjuntos que verifica se um conjunto é um subconjunto de outro conjunto. 
# Ele retorna True se todos os elementos do primeiro conjunto estiverem presentes no segundo conjunto 
# (também conhecido como conjunto pai), caso contrário, retorna False.

conjunto_a = {1,2,3}
conjunto_b = {2,3,5,6,1,7,4}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
