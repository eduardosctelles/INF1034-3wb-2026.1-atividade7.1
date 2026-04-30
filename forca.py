import random
pontos = 0
lista = ["cachorro", "gato", "elefante", "leão", "tigre", "girafa", "zebra", "gorila", "pinguim", "golfinho", "baleia", "tubarão", "águia", "papagaio", "cobra", "jacaré", "tartaruga", "coelho", "cavalo", "lobo"]
n_tent = 6

def intro():
    print(30*'=')
    print('Bem vindo ao jogo da forca!')
    print(30*'=')

def tela_final():
    global n_tent
    n_tent = 6
    jogar = input('Você quer jogar denovo? - sim ou não?\n')
    if jogar == 'sim':
        jogo()
    elif jogar == 'não':
        print(f'Tudo bem, obrigado por jogar! - Sua pontuação foi de {pontos} pontos')

def jogo():
    global n_tent
    global pontos
    intro()
    p_escolhida = list(random.choice(lista))
    mostra_p_tela = ['_'] * len(p_escolhida)
    print(mostra_p_tela)

    for i in range(1, n_tent + 1):
        tent = input(f'Escreva a letra que você quer adivinhar: - Tentativa {i} - Vidas = {n_tent}\n')
        repetido = False
        #Chute da palavra toda
        if len(tent) > 1:
            if list(tent) == p_escolhida:
                print(31*'=')
                print('Você ganhou chutando a palavra!')
                pontos = pontos + 1
                tela_final()
                return
            else:
                print(43*'=')
                print('Você tentou chutar a palávra toda e perdeu!')
                print(f'A palávra era {"".join(p_escolhida)}')
                tela_final()
                return
        #Chute da letra
        elif tent in p_escolhida:
            for letra in range(len(p_escolhida)):
                if tent == p_escolhida[letra]:
                    if repetido == False:
                        print('Você acertou uma letra!')
                        repetido = True
                    mostra_p_tela[letra] = tent
        else:
            print('Você perdeu uma vida.')
            n_tent = n_tent - 1 
        
        print(25*'=')
        print(mostra_p_tela)
        print(25*'=')
        if mostra_p_tela == p_escolhida:
            print('Você ganhou!')
            pontos = pontos + 1
            tela_final()
            return
        
    print(43*'=')
    print(f'Suas vidas acabaram! - A palávra era {"".join(p_escolhida)}')
    tela_final()

jogo()