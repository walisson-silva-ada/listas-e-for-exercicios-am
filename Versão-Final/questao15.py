nome = input("Digite o nome: ") 
idade = int(input("Digite a idade: ")) 
num_provas = int(input("Digite o número de provas: ")) 
lista = []

for i in range (num_provas): 
    notas = float(input(f'Digite a nota {i+1} do aluno: ')) 
    lista.append(notas)

media = sum(lista)/num_provas

if media > 5: 
    validacao = True 
else: 
    validacao = False

lista=[f'Nome:{nome},Idade:{idade}, Notas:{lista}, Média:{media:.1f} ,Validação:{validacao}']

print(lista)