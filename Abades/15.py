# Desafio 1 - Faça um programa que peça para o usuário digitar o nome 
# e a idade de um aluno e o número de provas que esse aluno fez. 
# Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. 
# Ao final o programa deve imprimir uma lista contendo:

# a. Nome do aluno na posição 0;
# b. Idade do aluno na posição 1;
# c. Uma lista com todas as notas na posição 2;
# d. A média do aluno na posição 3;
# e. True ou False, caso a média seja maior que 5 ou não, na posição 4.
# Dica: Use o que você fez nos exercícios anteriores para criar esse programa.

nome = input('Digite o nome do aluno:\n')
idade = int(input('Digite a idade do aluno:\n'))
num_provas = int(input('Quantas provas este aluno fez? \n'))

count = 1
notas = []
while count < (num_provas + 1):
    nota = int(input(f'Digite a nota da prova {count}:\n'))
    notas.append(nota)
    count += 1

media = sum(notas)/len(notas)

def media_aluno(media):
    if media > 5:
        return True
    else:
        return False

lista_final = [nome, idade, notas, media, media_aluno(media)]
print(lista_final)   

