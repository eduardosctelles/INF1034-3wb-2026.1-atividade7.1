import random
pontos = 0
lista = ["cachorro", "gato", "elefante", "leão", "tigre", "girafa", "zebra", "gorila", "pinguim", "golfinho", "baleia", "tubarão", "águia", "papagaio", "cobra", "jacaré", "tartaruga", "coelho", "cavalo", "lobo"]

def intro():
    print(30*'=')
    print('Bem vindo ao jogo da forca!')
    print(30*'=')

def tela_final():
    jogar = input('Você quer jogar denovo? - sim ou não?\n')
    if jogar == 'sim':
        jogo()
    elif jogar == 'não':
        print(f'Tudo bem, obrigado por jogar! - Sua pontuação foi de {pontos} pontos')

def jogo():
    global pontos 
    intro()
    p_escolhida = list(random.choice(lista))
    mostra_p_tela = ['_'] * len(p_escolhida)
    print(mostra_p_tela)

    for i in range(1, 7):
        tent = input(f'Escreva a letra que você quer adivinhar: - Tentativa {i}\n')

        repetido = True

        for letra in range(len(p_escolhida)):
            if tent == p_escolhida[letra]:
                if repetido:
                    print('Você acertou uma letra!')
                    repetido = False
                mostra_p_tela[letra] = p_escolhida[letra]
                
        print(mostra_p_tela)

        if mostra_p_tela == p_escolhida or tent == str(p_escolhida):
            print('Você ganhou!')
            pontos = pontos + 1
            tela_final()
            return
    
    print(30*'=')
    print(f'Suas vidas acabaram! - A palávra era {str(p_escolhida)}')
    tela_final()

jogo()