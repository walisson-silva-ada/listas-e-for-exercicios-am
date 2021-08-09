""" Questão 20 - Super Desafio! - Faça um jogo de BlackJack usando funções: o BlackJack, ou Vinte e Um, é um jogo em que os jogadores podem comprar cartas perdidas, enquanto leva menos de 21 pontos. No nosso jogo, o Ás vale um ponto; como cartas de 2 a 10 valem o número de pontos que elas representam; e Valete, Dama e Rei valem 10 pontos cada. Ganha o jogador que tiver o maior número de pontos, desde que este seja menor ou igual a 21. Nosso jogo deve ter as seguintes funções:

uma. Função principal: uma função que vamos chamar para iniciar o jogo. Essa função não irá receber nem retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome de cada um. Em seguida ela chama as outras funções do jogo.

b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho.

c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar uma jogada e, caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) deve perguntar se ele quer comprar uma carta. Se ele responder que sim, uma função deve chamar a função próxima para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder que não, uma função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve ser chamada enquanto houver jogadores ativos.

d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de pontos que essa carta vale.

e. Função verificação: verifica e indica qual / quais jogador / jogadores tem o maior número de pontos, que seja menor ou igual a 21. """
import random

def inicio_do_jogo():
    jogadores = []
    status_jogador = []
    scores = []    
    num_jogadores = int(input('Informe o número de jogadores: '))
    
    for i in range(num_jogadores):
        jogadores[input('Digite o nome dos jogadores: ')] = [0, Ativo]
        status_jogador .append('Ativo')
        scores.append(0)
                   
    def criar_baralho():
        baralho = []
        naipes = ['ouros', 'espadas', 'copas', 'paus']

        for naipe in naipes:
            barlho.append(f'Ás de{naipe}')

            for numeros in range(2, 10):
                baralho.append(f'{numeros} de {naipe}')
            baralho.append(f'Valete de {naipe}')
            baralho.append(f'Dama de {naipe}')
            baralho.append(f'Rei de {naipe}')

        return baralho

    baralho = criar_baralho ()
        
    def comprar_uma_carta ():
            carta = random.cho
            
            carta = random.choice(baralho)
            print ('Carta comprada: ', carta)
            baralho.remove(carta)
            
            if 'Ás' in carta:
                return 1
            elif 'Valete' in carta or 'Dama' in carta or 'Rei' in carta or '10' in carta:
                return 10
            else:
                return int (carta[10])
            
    def jogar(jogador):
        if jogadores[jogador][1] == 'Ativo':
            acao = input('Escolha uma ação: comprar uma carta ou desistir.\n')

            if acao == 'comprar_uma_carta':
                jogadores[jogador][0] += comprar_uma_carta()

                if jogadores[jogador][0] > 21:
                        jogadores[jogador][1] = "Inativo"

            elif acao == 'desistir':
                    jogadores[jogador][1] = "Inativo"

        elif jogadores[jogador][1] != 'Ativo':
                print('Jogador fora do jogo')

                
    while any(status == 'Ativo' for status in status_jogador):
        print(jogadores)
        jogar(input('Qual o jogador irá jogar?'))
        for i in range(0, num_jogadores):
                status_jogador[i] = jogadores[list(jogadores.keys())[i]][1]
                scores[i] = jogadores[list(jogadores.keys())[i]][0]
        
    def verifica():
        pontuacao_valida = []        
        for score in scores:
            if score <= 21:
                pontuacao_valida.append(score)
                
        maior_pontuacao = max(pontuacao_valida)       
        lista_melhores_jogadores = []
        lista_do_dicionario = jogadores.items()
        
        for item in lista_do_dicionario:
            if item[1][0] <= maior_pontuacao:
                lista_melhores_jogadores.append(item[0])
        
            rint(f'A maior pontuação foi:\n{maior_pontuacao}\nVitoriosos:\n{lista_melhores_jogadores}')


    verifica()
    
inicio_do_jogo()   