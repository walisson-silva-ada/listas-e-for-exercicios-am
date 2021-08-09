# Super desafio! Faça um sistema de cadastro de clientes. 
# Modele cada cliente como uma lista de três elementos: nome, CPF e e-mail.

# a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e 
# retorne uma lista contendo esses elementos nessa ordem.
# b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já 
# que cada cliente será uma lista tal como produzido no item a).
# c. Faça uma função que recebe a lista do item b) e um CPF e, se esse 
# cliente estiver na lista de cadastro, sua função deve devolver a lista
# de dados desse cliente; caso contrário, sua função deve imprimir “não encontrado”.
# d. Enquanto não for digitado 0, o seu programa deve continuar rodando. 
# Se digitado 1, seu programa deve cadastrar um novo cliente; se digitado 2, seu 
# programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, 
# seu programa deve imprimir todos os clientes cadastrados.
nome = str('')
cad = {}


def cadastrar(nome=''):
    # Variáveis
    choice = str(".")
    vitorias = int()
    cabecalho = str("Cadastro de Usuarios")
    cabecalho2 = str("por Gabriel Abades")

    # Página Inicial
    print(10 * "=-")
    print(f"{cabecalho:^20}")
    print(f"{cabecalho2:^20}")
    print(10 * "=-")

    # Escolhas
    while choice not in 'ABCD' or choice == "ABCD":
        print('''
    (A) NOVO CADASTRO
    (B) CADASTRADOS
    (C) PESQUISAR POR CPF
    (D) FECHAR

    ''')
        choice = str(input("")).upper().strip()

        # Escolhas caso resposta errada
        if choice not in ("ABCD") or choice == "ABCD":
            print("Desculpe, não entendi...")
    # Cadastramento
    if choice == "A":
        inserir()

        cadastrar()
    elif choice == "B":
        exibir()

        cadastrar()
    elif choice == "C":
        pesquisar()

        cadastrar()


def exibir():
    for nome in cadastros.keys():
        print("CPF: ", nome, " - Outros dados: ", cadastros[nome])
        

def inserir():
    nome = input('Qual seu nome?')
    cpf = int(input('Digite seu cpf:'))
    email = input('Digite seu e-mail:')

    if cadastros.get(nome):
        print("Ja existe cadastrado ",nome)
    else:
        cadastros[cpf] = nome, cpf, email
        print(cadastros)


def pesquisar():
    x = int(input('Digite o cpf para pesquisar:'))
    
    for nome in cadastros.keys():
        if x == nome:
            print("CPF: ", nome, " - Outros dados: ", cadastros[nome])
        else: 
            print('CPF não foi encontrado!')
    
    

cadastros = {}
cadastrar()