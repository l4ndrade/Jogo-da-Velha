cores = {"fecha_cor": '\033[m', "vermelho": '\033[1;31m', "cinza": '\033[37m', "amarelo": '\033[1;33m'}


def tittle(txt, tam=30):
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)


def printmatrix(lst):
    for line in range(len(lst)):
        for item in range(len(lst)):
            if lst[line][item] in '123456789':
                cor = cores["cinza"]
            else:
                cor = cores["amarelo"]
            print(f'[{cor}{lst[line][item]}{cores["fecha_cor"]}]', end='\t')
        print()


def readint(msg, minint, maxint):
    valid = False
    while not valid:
        try:
            a = int(input(msg))
        except ValueError:
            print(f'{cores["vermelho"]}ERRO: Digite apenas valores inteiros{cores["fecha_cor"]}')
        except KeyboardInterrupt:
            print('/Sentimos muito em saber que você não quer mais jogar, adeus!/')
            return -1
        else:
            if maxint >= a >= minint:
                return a
            else:
                print(f'{cores["vermelho"]}ERRO: O número deve estar entre {minint} e {maxint}{cores["fecha_cor"]}')


def acceptcord(msg, maxnum):
    ints = []
    while True:
        entrada = str(input(msg)).strip()
        for c in entrada:
            if c.isnumeric():
                if int(c) <= maxnum:
                    ints.append(c)
        if len(ints) == 2:
            break
        print(f'{cores["vermelho"]}ERRO: Digite coordenadas válidas!{cores["fecha_cor"]}')
        ints.clear()
    return [ints[0], ints[1]]


def popadd(lst, cordx, cordy, marca):
    if lst[cordx][cordy] not in 'XO':
        lst[cordx].pop(cordy)
        lst[cordx].insert(cordy, marca)


def checkwin(lst, marca1, marca2):
    if lst[0][0] == lst[0][1] == lst[0][2]:  # 1---
        if lst[0][0] != '':
            if lst[0][0] == marca1:
                return marca1
            elif lst[0][0] == marca2:
                return marca2

    elif lst[1][0] == lst[1][1] == lst[1][2]:  # 2---
        if lst[1][0] != '':
            if lst[1][0] == marca1:
                return marca1
            elif lst[1][0] == marca2:
                return marca2

    elif lst[2][0] == lst[2][1] == lst[2][2]:  # 3---
        if lst[2][0] != '':
            if lst[2][0] == marca1:
                return marca1
            elif lst[2][0] == marca2:
                return marca2

    elif lst[0][0] == lst[1][0] == lst[2][0]:  # 1|
        if lst[0][0] != '':
            if lst[0][0] == marca1:
                return marca1
            elif lst[0][0] == marca2:
                return marca2

    elif lst[0][1] == lst[1][1] == lst[2][1]:  # 2|
        if lst[0][1] != '':
            if lst[0][1] == marca1:
                return marca1
            elif lst[0][1] == marca2:
                return marca2

    elif lst[0][2] == lst[1][2] == lst[2][2]:  # 3|
        if lst[0][2] != '':
            if lst[0][2] == marca1:
                return marca1
            elif lst[0][2] == marca2:
                return marca2

    elif lst[2][0] == lst[1][1] == lst[0][2]:  # /
        if lst[2][0] != '':
            if lst[2][0] == marca1:
                return marca1
            elif lst[2][0] == marca2:
                return marca2

    elif lst[0][0] == lst[1][1] == lst[2][2]:  # \
        if lst[0][0] != '':
            if lst[0][0] == marca1:
                return marca1
            elif lst[0][0] == marca2:
                return marca2
