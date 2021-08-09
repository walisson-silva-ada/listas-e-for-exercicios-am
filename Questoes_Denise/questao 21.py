""" Questão 21 - Super desafio! Faça um sistema de cadastro de clientes. Modele cada cliente como uma lista de três elementos: nome, CPF e e-mail.

a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos nessa ordem.

b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já que cada cliente será uma lista tal como produzido no item a).

c. Faça uma função que recebe a lista do item b) e um CPF e, se esse cliente estiver na lista de cadastro, sua função deve devolver a lista de dados desse cliente; caso contrário, sua função deve imprimir “não encontrado”.

d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve cadastrar um novo cliente; se digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, seu programa deve imprimir todos os clientes cadastrados. """

def cadastro():
    cad_cliente = []
    nome = input('Digite o nome do cliente: ')
    cad_cliente.append(nome)
    cpf = input('Digite o CPF do cliente (somente numeros): ')
    cad_cliente.append(cpf)
    email = input('Digite o e-mail do cliente: ')
    cad_cliente.append(email)
    return cad_cliente 

def busca(cadastros, buscaCPF):
    NaoEncontrado = True
    for i in range(len(cadastros)):
        if cadastros[i][1] == buscaCPF:
            NaoEncontrado = False
            return cadastros[i]
    if NaoEncontrado:
        print('CPF não encontrado')   
        return ''

def opcoes():
    resposta = ''
    try:
        while resposta not in (0, 1, 2, 3):
            resposta = int(input('Digite uma das opções:\n 1 Cadastrar um cliente \n 2 Buscar um cliente por CPF\n 3 Imprimir usuários já cadastrados\n 0 Encerrar o programa:\n '))
    except:
        opcoes()
    return resposta

resposta = opcoes()
cadastros = []
while resposta != 0:
    if resposta == 1:
        cadastros.append(cadastro())
        resposta = opcoes()
    elif resposta == 3:
        for i in range(len(cadastros)):
            print(f'Nome: {cadastros[i][0]}; CPF: {cadastros[i][1]}; E-mail: {cadastros[i][2]}')
        resposta = opcoes()
    elif resposta == 2:
        buscaCPF = input('Informe o CPF: ')
        procura = busca(cadastros, buscaCPF)
        if procura != '':
            print(f'Nome: {procura[0]}; CPF: {procura[1]}; E-mail: {procura[2]}')     
        resposta = opcoes()
    else:
        resposta = 0
print('Programa Encerrado')   