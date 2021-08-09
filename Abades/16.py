# Desafio 2 - Faça um programa como o do item anterior, 
# porém que imprima a média sem considerar a maior e menor 
# nota do aluno (nesse caso o número de provas precisa ser obrigatoriamente maior que dois).

# Dica: crie uma cópia com a lista de todas as notas antes de fazer a média.
nome = input('Digite o nome do aluno:\n')
idade = int(input('Digite a idade do aluno:\n'))
num_provas = int(input('Quantas provas este aluno fez(precisa ser obrigatoriamente maior que dois)? \n'))
if num_provas > 2:
    count = 1
    notas = []
    while count < (num_provas + 1):
        nota = int(input(f'Digite a nota da prova {count}:\n'))
        notas.append(nota)
        count += 1
    
    x = max(notas)
    y = min(notas)
    notas.remove(x)
    notas.remove(y)
    print(notas)

    media = sum(notas)/len(notas)

    def media_aluno(media):
        if media > 5:
            return True
        else:
            return False

    lista_final = [nome, idade, notas, media, media_aluno(media)]
    print(lista_final)
else:
    print('Este aluno precisa obrigatoriamente de 3 ou mais notas, para que seja gerado a lista final')
   

