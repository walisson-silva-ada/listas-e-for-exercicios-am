'''Se o CPF for 286.255.878-87 o programa deve fazer primeiro:

x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)

Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim, o programa deve calcular:

x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)

e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).'''

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











'''CPF = list(input("Digite o seu CPF(apenas dígitos): "))  # Convertemos para uma lista de dígitos
for i in range(len(CPF)):
    CPF[i] = int(CPF[i])  # Convertemos a lista para inteiros
print(CPF)

soma = 0

for i in range(9):
    soma = soma + CPF[i]*(10-i)

if soma*10 % 11 == CPF[9]:
    soma = 0
    for i in range(10):
        soma = soma + CPF[i] * (11 - i)
    if soma*10 % 11 == CPF[10]:
        print("CPF Válido")
    else:
        print("CPF Inválido")
else:
    print("CPF Inválido")'''