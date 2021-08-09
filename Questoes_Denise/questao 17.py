""" Questão 17 - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. Para isso, principalmente o programa deve: 1 - multiplicar cada um dos 9 primeiros dígitos do CPF pelos números de 10 a 2 e somar todas as respostas. 2 - O resultado deve ser multiplicado por 10 e dividido por 11. 3 - O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito). 4 - Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior para verificar o segundo dígito verificador.

Exemplo:

Consulte o CPF para 286.255.878-87 o programa deve fazer o primeiro:

x = (2 * 10 + 8 * 9 + 6 * 8 + 2 * 7 + 5 * 6 + 5 * 5 + 8 * 4 + 7 * 3 + 8 * 2)

Em seguida, o programa deve testar se x * 10% 11 == 8 (o décimo número do CPF). Se sim, o programa deve calcular:

x = (2 * 11 + 8 * 10 + 6 * 9 + 2 * 8 + 5 * 7 + 5 * 6 + 8 * 5 + 7 * 4 + 8 * 3 + 8 * 2)

e verificar se x * 10% 11 == 7 (o décimo primeiro número do CPF). """

def todos_numeros_iguais(cpf):
    if len(cpf) < 0:
        return True
    return all(x == cpf[0] for x in cpf)

def recupera_soma(cpf, fator):
    return sum([int(n) * (fator -pos) for pos, n in enumerate(cpf[:9])])  

def recupera_digito(soma):
    resultado = (soma * 10) % 11
    if resultado == 10:
        return 0
    return resultado     
def recupera_primeiro_digito(cpf):
    soma = recupera_soma(cpf, 10)
    return recupera_digito(soma)   

def recupera_segundo_digito(cpf, primeiro_digito):
    soma = recupera_soma(cpf, 11) + (primeiro_digito * 2)    
    return recupera_digito(soma)    

def cpf_valido(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isnumeric() or todos_numeros_iguais(cpf):
        return False
    digito1 = recupera_primeiro_digito(cpf)
    digito2 = recupera_segundo_digito(cpf, digito1)
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])      

if __name__ == '__main__':
    print('Informe o CPF')
    cpf = input()
    if cpf_valido(cpf):
        print('CPF é válido.')
    else:
        print('CPF inválido')
