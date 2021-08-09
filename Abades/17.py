# Desafio 3 - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. 
# Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF 
# pelos números de 10 a 2 e somar todas as respostas. O resultado deve ser multiplicado por 10 
# e dividido por 11. O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito). 
# Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e 
# repetir o procedimento anterior para verificar o segundo dígito verificador.

# Exemplo:
# Se o CPF for 286.255.878-87 o programa deve fazer primeiro:
# x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)
# Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim, o programa deve calcular:
# x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)
# e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).
cpf = input('Digite um CPF para validação:\n')
lista1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista2 = []
lista3 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

for num in cpf:
    lista2.append(int(num))

juntar = zip(lista1,lista2)
listaTotal = [x*y for x,y in juntar]

x = sum(listaTotal)   

if len(lista2) == 11:
    if x*10%11 == lista2[9]:
        juntar = zip(lista3,lista2)
        listaTotal2 = [x*y for x,y in juntar]

        y = sum(listaTotal2) 
        if y*10%11 == lista2[10]:
            print('O CPF digitado é válido!')
        else:
            ('O CPF digitado não é válido, tente rever o que foi digitado e corrija!')
else:
    print('O CPF digitado não é válido, tente rever o que foi digitado e corrija, ele deve conter 11 números!')        



