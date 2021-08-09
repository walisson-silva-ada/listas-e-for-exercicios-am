cpf = input('Digite o CPF: ')
cpf = list(cpf)
x = 0
verificador1 = 10
verificador2 = 11

for i in range(len(cpf)):
    cpf[i] = int(cpf[i])

for i in range(9):
    x += cpf[i] * verificador1
    verificador1 -= 1

if x*10 % 11 == cpf[9]:
    x = 0
    for i in range(10):
        x += cpf[i]*verificador2
        verificador2 -= 1
        if x*10 % 11 == cpf[10]:
            valido = True
        else:
            valido = False
else:
    valido = False

if valido is True:
    print('CPF Válido')
else:
    print('CPF Inválido')


