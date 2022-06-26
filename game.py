import functions as f
from random import randint
from time import sleep

# DECLARAÇÃO DE VARIÁVEIS
cores = {"fecha_cor": '\033[m', "vermelho": '\033[1;31m', "verde": '\033[1;32m', "cinza": '\033[37m'}
tab = [
    ['1', '2', '3'],  # linha 0
    ['4', '5', '6'],  # linha 1
    ['7', '8', '9']  # linha 2
]
velha = 0
whosplaying = ''

f.tittle('VAMOS JOGAR JOGO DA VELHA', 30)  # Título
# ESCOLHA DE GAMEMODE
gamemode = f.readint("""Selecione o modo de jogo:
1 - SOLO
2 - DUO
> """, 1, 2)

# SOLO
if gamemode == 1:
    # ESCOLHA MARCAÇÃO
    while True:
        ponto = str(input('Digite a sua marcação[X / O]: ')).upper()
        if ponto in 'XO' and ponto != 'XO':
            break
        print(f'{cores["vermelho"]}Marcação inválida!{cores["fecha_cor"]} ')
    if ponto == 'X':
        pontopc = 'O'
    else:
        pontopc = 'X'
    # JOGO
    while True:
        f.tittle('TABULEIRO', 20)  # Título
        f.printmatrix(tab)  # Print Jogo
        # INVERSÃO DE JOGADORES
        if whosplaying == '' or whosplaying == 'pc':
            whosplaying = 'pl'
        else:
            whosplaying = 'pc'
        # VEZ DO JOGADOR
        if whosplaying == 'pl':
            marca = ponto
            who = f'{cores["verde"]}JOGADOR'
            while True:
                num = str(f.readint('Digite a posição que você quer marcar: ', 1, 9)).strip()[
                    0]  # Request de coordenadas
                num = int(num)
                if num == 1:
                    x = 0
                    y = 0
                elif num == 2:
                    x = 0
                    y = 1
                elif num == 3:
                    x = 0
                    y = 2
                elif num == 4:
                    x = 1
                    y = 0
                elif num == 5:
                    x = 1
                    y = 1
                elif num == 6:
                    x = 1
                    y = 2
                elif num == 7:
                    x = 2
                    y = 0
                elif num == 8:
                    x = 2
                    y = 1
                else:
                    x = 2
                    y = 2
                if tab[x][y] not in 'XO':
                    break
                print(f'{cores["vermelho"]}ERRO: O local ja está marcado!{cores["fecha_cor"]}')
            f.popadd(tab, x, y, ponto)
        # VEZ DO COMPUTADOR
        else:
            marca = pontopc
            who = f'{cores["vermelho"]}COMPUTADOR'
            while True:
                x = randint(0, 2)
                y = randint(0, 2)
                if tab[x][y] not in 'XO':
                    break
            f.popadd(tab, x, y, pontopc)
            print('- O Computador está pensando...')
            sleep(2)
        sleep(1)
        # VERIFICA VITÓRIA
        if f.checkwin(tab, ponto, pontopc) == marca:
            print(f'O {who}{cores["fecha_cor"]} GANHOU')
            break
        # VERIFICA VELHA
        for linha in range(3):
            for coluna in range(3):
                if tab[linha][coluna] in 'XO':
                    velha += 1
        if velha == 9:
            print('DEU VELHA, NINGUÉM GANHOU!')
            break
        velha = 0

# DUO
else:
    # ESCOLHA MARCAÇÃO
    while True:
        ponto_1 = str(input('Digite a marcação do JOGADOR 1 [X / O]: ')).upper()
        if ponto_1 in 'XO' and ponto_1 != 'XO':
            break
        print(f'{cores["vermelho"]}Marcação inválida!{cores["fecha_cor"]} ')
    if ponto_1 == 'X':
        ponto_2 = 'O'
    else:
        ponto_2 = 'X'
    print(f'Então, o jogador 2 usará a marcação {ponto_2}!')
    # JOGO
    while True:
        f.tittle('TABULEIRO', 20)  # Título
        f.printmatrix(tab)  # Print Jogo
        # INVERSÃO DE JOGADORES
        if whosplaying == '' or whosplaying == 'p2':
            whosplaying = 'p1'
        else:
            whosplaying = 'p2'
        # VEZ DO JOGADOR
        if whosplaying == 'p1':
            marca = ponto_1
            who = f'{cores["verde"]}JOGADOR 1'
        else:
            marca = ponto_2
            who = f'{cores["verde"]}JOGADOR 2'
        while True:
            num = str(f.readint('Digite a posição que você quer marcar: ', 1, 9)).strip()[0]
            num = int(num)
            if num == 1:
                x = 0
                y = 0
            elif num == 2:
                x = 0
                y = 1
            elif num == 3:
                x = 0
                y = 2
            elif num == 4:
                x = 1
                y = 0
            elif num == 5:
                x = 1
                y = 1
            elif num == 6:
                x = 1
                y = 2
            elif num == 7:
                x = 2
                y = 0
            elif num == 8:
                x = 2
                y = 1
            else:
                x = 2
                y = 2
            if tab[x][y] not in 'XO':
                break
            print(f'{cores["vermelho"]}ERRO: O local ja está marcado!{cores["fecha_cor"]}')
        f.popadd(tab, x, y, marca)
        # VERIFICA VITÓRIA
        if f.checkwin(tab, ponto_1, ponto_2) == marca:
            print(f'O {who}{cores["fecha_cor"]} GANHOU')
            break
        # VERIFICA VELHA
        for linha in range(3):
            for coluna in range(3):
                if tab[linha][coluna] in 'XO':
                    velha += 1
        if velha == 9:
            print('DEU VELHA, NINGUÉM GANHOU!')
            break
        velha = 0

f.printmatrix(tab)
print('FIM')
