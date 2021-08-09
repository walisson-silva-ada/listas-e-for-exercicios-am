# Super Desafio! - Faça um jogo de BlackJack usando funções: o BlackJack, ou Vinte e Um, 
# é um jogo em que os jogadores podem comprar cartas livremente, enquanto tiverem menos de 21 pontos. 
# No nosso jogo, o Ás vale um ponto; as cartas de 2 a 10 valem o número de pontos que elas representam; 
# e Valete, Dama e Rei valem 10 pontos cada. Ganha o jogador que tiver o maior número de pontos, desde 
# que este seja menor ou igual a 21. Nosso jogo deve ter as seguintes funções:

# a. Função principal: a função que vamos chamar para iniciar o jogo. Essa função não irá receber 
# nem retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome 
# de cada um. Em seguida ela chama as outras funções do jogo.

# b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho.

# c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar a jogada e, 
# caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) 
# deve perguntar se ele quer comprar uma carta. Se ele responder que sim, a função deve chamar a próxima 
# função para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder que 
# não, a função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve 
# ser chamada enquanto houver jogadores ativos.

# d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de
#  pontos que essa carta vale.

# e. Função verificação: verifica e indica qual/quais jogador/jogadores tem o maior número de 
# pontos, que seja menor ou igual a 21.
import random

baralho = []
tracinhos = ('-=')*20

print(f"{tracinhos}\n    BEM-VINDO(A) AO JOGO BLACK JACK!    \n{tracinhos}")
jogadores_dict = {}
nomes_jogadores = []
num_jog = 0

def jogadores():
    num_jog = int(input('Qual o número de jogadores?\n'))
    count = 1
    while count < num_jog + 1:
        nome = input(f'Digite o nome do player {count}: \n')
        nomes_jogadores.append(nome)

        count += 1

def baralho_jogo():
    count = 1
    while count < 11:
        baralho.append(count)
        count += 1

def jogadas():
    
    for jogador in nomes_jogadores:
        print(f'Faça suas jogadas {jogador}, boa sorte...')
        total_jogador = 0
        x = 0
        p2 = 0
       
        while p2 != 'N' and p2 != 'NAO' and p2 != 'NÃO':
            
            x = random.choice(baralho)
            total_jogador += x
            print("\nSua carta é", x)
            print(f'O total até o momento é de {total_jogador}')
            p2 = str(input("Você quer mais cartas?\n>> ").upper()) 

            if total_jogador > 21:
                print('Mas que pena vc estourou!')
                p2 = 'N'
            
        jogadas_dict = {
            jogador: total_jogador
        }
        jogadores_dict.update(jogadas_dict)


def verifica_vencedor():
    print(f"{tracinhos}\n              PLACAR    \n{tracinhos}")
    for jogador in jogadores_dict:

        if jogadores_dict[jogador] <= 21:
            print(f'Parabéns {jogador} você ganhou! Pontuação: {jogadores_dict[jogador]}')
        else:
            print(f'{jogador}, você estourou a pontuação! Pontuação: {jogadores_dict[jogador]}')
        
     
jogadores()
baralho_jogo()
jogadas()
verifica_vencedor()










