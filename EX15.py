''' Desafio 1 - Faça um programa que peça para o usuário digitar o nome e a idade de um aluno e o número de provas que esse aluno fez. Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. Ao final o programa deve imprimir uma lista contendo:

a. Nome do aluno na posição 0;

b. Idade do aluno na posição 1;

c. Uma lista com todas as notas na posição 2;

d. A média do aluno na posição 3;

e. True ou False, caso a média seja maior que 5 ou não, na posição 4.

Dica: Use o que você fez nos exercícios anteriores para criar esse programa.

 '''

nome = input('Nome do aluno: ')
idade = int(input('Idade do aluno: '))
n_provas = int(input('Provas feitas: '))
notas = []
soma_notas = 0

for i in range(n_provas):
    nota_prova = float(input('Nota da prova #{}:'.format(i+1)))
    notas.append(nota_prova)
    soma_notas += nota_prova

media = soma_notas / len(notas)
media = media.__round__(2)

if media >= 5:
    aprovado = True
else:
    aprovado = False

infos = [nome, idade, notas, media, aprovado]
print(infos)







