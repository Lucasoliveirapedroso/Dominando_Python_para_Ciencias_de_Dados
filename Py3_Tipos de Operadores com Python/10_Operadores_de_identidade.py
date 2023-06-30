#ocupa mesma posição na memoria
curso = "Curso de python"
nome_curso = curso
saldo = 100
limite =  100

print(curso is nome_curso)
#true
print(curso is not nome_curso)
#false
print(saldo is limite)
#true
print(saldo is not limite)
#false