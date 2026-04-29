import random

lista = ['vazio', 'papel', 'tesoura', 'pedra']
pontos = 0 

def form():
    print(40*'=')

def jogo():
    #meu código estava dando erro sem essa linha e tive que pesquisar na internet o que ela significava
    global pontos
    num = random.randint(1, 3)
    jogador = int(input('Você escolhe pedra, papel ou tesoura?\n 1 = papel, 2 = tesoura, 3 = pedra\n'))
    if jogador == num:
        print(f'Empate! Os dois escolheram {lista[jogador]}')
    elif (jogador == 1 and num == 3) or (jogador == 2 and num == 1) or (jogador == 3 and num == 2):
        print(f'Você ganhou! Você escolheu {lista[jogador]} e o programa {lista[num]}')
        pontos = pontos + 1 
    else:
        print(f'Você perdeu! Você escolheu {lista[jogador]} e o programa {lista[num]}')

    denovo()

def denovo():
    jogar = input(f'Você está com {pontos} pontos! Você quer jogar novamente?\n')
    if jogar == 'sim':
        form()
        jogo()
    elif jogar == 'não':
        form()
        print(f'Tudo bem, obrigado por jogar! - Você fez {pontos} pontos no total!')

jogo()
