def calcular_total(numeros):
    return sum(numeros)
print(calcular_total([10,102]))

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return print(f"Seu antecessor é: {antecessor}, e seu sucessor é: {sucessor}")
retorna_antecessor_e_sucessor(1)

def function_3():
    print("function")
print(function_3())

#sem return padrão retornar none