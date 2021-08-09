''' Desafio 3 - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é
válido. Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros
dígitos do CPF pelos números de 10 a 2 e somar todas as respostas. O resultado deve ser
multiplicado por 10 e dividido por 11. O resto dessa divisão deve ser igual ao primeiro 
dígito verificador (10º dígito). Em seguida, o programa deve multiplicar cada um dos 10
primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior para
verificar o segundo dígito verificador.

Exemplo:

Se o CPF for 286.255.878-87 o programa deve fazer primeiro:

x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)

Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim,
o programa deve calcular:

x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)

e verificar se x*10%11 == 7 (o décimo primeiro número do CPF). '''

if name == 'main': print('Digite o CPF: ') cpf = input()

cpf = cpf.replace('.','').replace('-','')

if len(cpf) < 11:
    print(f'CPF inválido! Documento deve conter 11 dígitos.')
    exit()

int(cpf)

num1 = int(cpf[0])
num2 = int(cpf[1])
num3 = int(cpf[2])
num4 = int(cpf[3])
num5 = int(cpf[4])
num6 = int(cpf[5])
num7 = int(cpf[6])
num8 = int(cpf[7])
num9 = int(cpf[8])
num10 = int(cpf[9])
num11 = int(cpf[10])

if num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9 == num10 == num11:
    print('CPF inválido!')
    exit()

primeira_soma = num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2

primeiro_digito_verificador = (primeira_soma * 10) % 11

if primeiro_digito_verificador == 10:
    primeiro_digito_verificador = 0

segunda_soma = num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 + num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + primeiro_digito_verificador * 2
segundo_digito_verificador = (segunda_soma * 10) % 11

if segundo_digito_verificador == 10:
    segundo_digito_verificador = 0

if (primeiro_digito_verificador == num10 and segundo_digito_verificador == num11):
    print('CPF é válido!')
print('Validação concluída!')