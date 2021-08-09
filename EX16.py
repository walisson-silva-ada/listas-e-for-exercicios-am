nome = input('Nome do aluno: ')
idade = int(input('Idade do aluno: '))
n_provas = int(input('Provas feitas: '))
notas = []
soma_notas = 0

for i in range(n_provas):
    nota_prova = float(input('Nota da prova #{}:'.format(i+1)))
    notas.append(nota_prova)
    soma_notas += nota_prova

print(notas)
notas.remove(max(notas))
notas.remove(min(notas))
print(notas)

# Erro no cálculo
media = sum(notas)/len(notas)


if media >= 5:
    aprovado = True
else:
    aprovado = False

infos = [nome, idade, notas, media, aprovado]
print(infos)
