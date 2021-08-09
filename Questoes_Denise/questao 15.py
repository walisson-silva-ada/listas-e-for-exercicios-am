""" Questão 15 - Faça um programa que peça para o usuário digitar o nome e a idade de um aluno e o número de provas que esse aluno fez. Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. Ao final o programa deve imprimir uma lista contendo:

a. Nome do aluno na posição 0;

b. Idade do aluno na posição 1;

c. Uma lista com todas as notas na posição 2;

d. A média do aluno na posição 3;

e. Verdadeiro ou falso, caso a média seja maior que 5 ou não, na posição 4.

Dica: Use o que você fez nos exercícios anteriores para criar esse programa. """

boletim_aluno = list()
notas = list()

nome_do_aluno = input('Digite o nome do aluno: ')  
idade_do_aluno = int(input('Digite a idade do aluno: ')) 
num_provas = int(input('Digite o número de provas que o aluno realizou: '))
            
    
for i in range(num_provas): 
    nota = float(input(f'Digite a nota {i+1} do aluno:'))
    notas.append(nota)
    media = sum(notas) / len(notas)   
    if media > 5 :
        aprovado = True
    else:
        aprovado = False    
    
boletim_aluno.append([nome_do_aluno, idade_do_aluno, [notas], media, aprovado])


boletim_aluno = [f'Nome: {nome_do_aluno}, Idade: {idade_do_aluno}, Notas: {notas}, Média: {media:.1f}, Aluno aprovado: {aprovado}']
print(boletim_aluno)
