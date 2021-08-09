""" Questão 16 - Faça um programa como o do item anterior, porém que imprima a média sem considerar a maior e menor nota do aluno (nesse caso o número de provas precisa ser obrigatoriamente maior que dois).

Dica: crie uma cópia com a lista de todas as notas antes de fazer a média. """

boletim_aluno = list()
notas = list()

nome_do_aluno = input('Digite o nome do aluno: ')  
idade_do_aluno = int(input('Digite a idade do aluno:')) 
num_provas = int(input('Digite o número de provas que o aluno realizou (número de provas deve ser maior que 2): '))
    
for i in range(num_provas):
    if num_provas >= 2:
        nota = float(input(f'Digite a nota {i+1} do aluno: '))
        notas.append(nota)
    else:
        print('Número invalido, o número de provas deve ser maior que 2.')
    
notas.remove(max(notas))
notas.remove(min(notas))
    
media = sum(notas)/num_provas   
    
if media > 5 :
    aprovado = True
else:
    aprovado = False    
            
boletim_aluno.append([nome_do_aluno, idade_do_aluno, [notas], media, aprovado])
     

boletim_aluno = [f'Nome: {nome_do_aluno}, Idade: {idade_do_aluno}, Notas: {notas}, Média: {media:.1f}, Aluno aprovado: {aprovado}']
print(boletim_aluno)   