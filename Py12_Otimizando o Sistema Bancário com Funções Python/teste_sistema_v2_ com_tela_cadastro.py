import tkinter as tk
import textwrap

# Funções do programa

def depositar():
    valor = float(entry_valor.get())
    if valor > 0:
        saldo_atual = float(label_saldo["text"].split()[-1])
        novo_saldo = saldo_atual + valor
        label_saldo["text"] = f"Saldo: R$ {novo_saldo:.2f}"
        extrato_atual = textwrap.dedent(label_extrato["text"])
        extrato_atual += f"Depósito: R$ {valor:.2f}\n"
        label_extrato["text"] = extrato_atual
        entry_valor.delete(0, tk.END)
    else:
        label_status["text"] = "@@@ Operação falhou! O valor informado é inválido. @@@"

def sacar():
    valor = float(entry_valor.get())
    saldo_atual = float(label_saldo["text"].split()[-1])
    limite = 500
    limite_saques = 3

    if valor <= 0:
        label_status["text"] = "@@@ Operação falhou! O valor informado é inválido. @@@"
    elif valor > saldo_atual:
        label_status["text"] = "@@@ Operação falhou! Você não tem saldo suficiente. @@@"
    elif valor > limite:
        label_status["text"] = "@@@ Operação falhou! O valor do saque excede o limite. @@@"
    elif numero_saques >= limite_saques:
        label_status["text"] = "@@@ Operação falhou! Número máximo de saques excedido. @@@"
    else:
        novo_saldo = saldo_atual - valor
        label_saldo["text"] = f"Saldo: R$ {novo_saldo:.2f}"
        extrato_atual = textwrap.dedent(label_extrato["text"])
        extrato_atual += f"Saque: R$ {valor:.2f}\n"
        label_extrato["text"] = extrato_atual
        entry_valor.delete(0, tk.END)
        numero_saques += 1

def exibir_extrato():
    extrato = textwrap.dedent(label_extrato["text"])
    if extrato.strip() == "Não foram realizadas movimentações.":
        label_status["text"] = "Não foram realizadas movimentações."
    else:
        label_status["text"] = extrato

def criar_usuario():
    cpf = entry_cpf.get()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        label_status["text"] = "@@@ Já existe usuário com esse CPF! @@@"
    else:
        nome = entry_nome.get()
        data_nascimento = entry_data_nascimento.get()
        endereco = entry_endereco.get()

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        label_status["text"] = "=== Usuário criado com sucesso! ==="

def criar_conta():
    cpf = entry_cpf.get()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
        label_status["text"] = "=== Conta criada com sucesso! ==="
    else:
        label_status["text"] = "@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@"

def listar_contas():
    if not contas:
        label_status["text"] = "Não há contas cadastradas."
    else:
        label_status["text"] = ""
        for conta in contas:
            info_conta = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}\n"""
            label_status["text"] += "=" * 100 + "\n" + textwrap.dedent(info_conta)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


import tkinter as tk
import textwrap

# Funções do programa
# (As mesmas funções que você forneceu anteriormente)

def mostrar_dialogo_deposito():
    dialogo = tk.Toplevel(janela)
    dialogo.title("Depósito")
    
    label_valor = tk.Label(dialogo, text="Valor:")
    label_valor.pack()

    entry_valor = tk.Entry(dialogo)
    entry_valor.pack()

    btn_depositar = tk.Button(dialogo, text="Depositar", command=lambda: realizar_deposito(dialogo, entry_valor))
    btn_depositar.pack()

def realizar_deposito(dialogo, entry_valor):
    valor = float(entry_valor.get())
    depositar(valor)
    dialogo.destroy()

def mostrar_dialogo_saque():
    dialogo = tk.Toplevel(janela)
    dialogo.title("Saque")
    
    label_valor = tk.Label(dialogo, text="Valor:")
    label_valor.pack()

    entry_valor = tk.Entry(dialogo)
    entry_valor.pack()

    btn_sacar = tk.Button(dialogo, text="Sacar", command=lambda: realizar_saque(dialogo, entry_valor))
    btn_sacar.pack()

def realizar_saque(dialogo, entry_valor):
    valor = float(entry_valor.get())
    sacar(valor)
    dialogo.destroy()

def mostrar_dialogo_criar_usuario():
    dialogo = tk.Toplevel(janela)
    dialogo.title("Criar Usuário")
    
    label_cpf = tk.Label(dialogo, text="CPF (somente número):")
    label_cpf.pack()

    entry_cpf = tk.Entry(dialogo)
    entry_cpf.pack()

    label_nome = tk.Label(dialogo, text="Nome completo:")
    label_nome.pack()

    entry_nome = tk.Entry(dialogo)
    entry_nome.pack()

    label_data_nascimento = tk.Label(dialogo, text="Data de nascimento (dd-mm-aaaa):")
    label_data_nascimento.pack()

    entry_data_nascimento = tk.Entry(dialogo)
    entry_data_nascimento.pack()

    label_endereco = tk.Label(dialogo, text="Endereço (logradouro, nro - bairro - cidade/sigla estado):")
    label_endereco.pack()

    entry_endereco = tk.Entry(dialogo)
    entry_endereco.pack()

    btn_criar_usuario = tk.Button(dialogo, text="Criar Usuário", command=lambda: realizar_criar_usuario(dialogo, entry_cpf, entry_nome, entry_data_nascimento, entry_endereco))
    btn_criar_usuario.pack()

def realizar_criar_usuario(dialogo, entry_cpf, entry_nome, entry_data_nascimento, entry_endereco):
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    endereco = entry_endereco.get()

    criar_usuario(cpf, nome, data_nascimento, endereco)
    dialogo.destroy()

# Criando a janela principal
janela = tk.Tk()
janela.title("Banco Simples")
janela.geometry("500x400")

# Variáveis para armazenar os dados
usuarios = []
contas = []
saldo_atual = 0
numero_saques = 0

# Criando os widgets da janela
label_saldo = tk.Label(janela, text=f"Saldo: R$ {saldo_atual:.2f}", font=("Arial", 16))
label_saldo.pack(pady=20)

label_extrato = tk.Label(janela, text="Não foram realizadas movimentações.", font=("Arial", 12))
label_extrato.pack(pady=10)

btn_depositar = tk.Button(janela, text="Depositar", font=("Arial", 12), command=mostrar_dialogo_deposito)
btn_depositar.pack()

btn_sacar = tk.Button(janela, text="Sacar", font=("Arial", 12), command=mostrar_dialogo_saque)
btn_sacar.pack()

btn_exibir_extrato = tk.Button(janela, text="Exibir Extrato", font=("Arial", 12), command=exibir_extrato)
btn_exibir_extrato.pack()

btn_criar_usuario = tk.Button(janela, text="Criar Usuário", font=("Arial", 12), command=mostrar_dialogo_criar_usuario)
btn_criar_usuario.pack()

btn_criar_conta = tk.Button(janela, text="Criar Conta", font=("Arial", 12), command=criar_conta)
btn_criar_conta.pack()

btn_listar_contas = tk.Button(janela, text="Listar Contas", font=("Arial", 12), command=listar_contas)
btn_listar_contas.pack()

# Rótulo para exibir mensagens ao clicar nos botões
label_status = tk.Label(janela, text="", fg="blue", font=("Arial", 12))
label_status.pack(pady=10)

# Iniciando o loop principal da aplicação
janela.mainloop()
