matriz_jogo = [[0,1,2],[3,4,5],[6,7,8]]
numeros_restantes = [0,1,2,3,4,5,6,7,8]
def menu_jogo(matriz_jogo):
    print(*matriz_jogo,sep='\n')

def horizontal(matriz_jogo,vez_do_jogador):
    jogador = 'X' if vez_do_jogador % 2 == 0 else 'O'
    for i in range(3):
        acc = 0
        for j in range(3):
            if matriz_jogo[i][j] == jogador:
                acc += 1
            if acc == 3:
                return True

def vertical(matriz_jogo,vez_do_jogador=None):
    jogador = 'X' if vez_do_jogador % 2 == 0 else 'O'
    for i in range(3):
        acc = 0
        for j in range(3):
            if matriz_jogo[j][i] == jogador:
                acc += 1
            if acc == 3:
                return True
def diagonal(matriz_jogo,vez_do_jogador):
    jogador = 'X' if vez_do_jogador % 2 == 0 else 'O'
    acc = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if matriz_jogo[j][i] == jogador:
                    acc += 1
                if acc == 3:
                    return True

def diagonal_invertida(matriz_jogo,vez_do_jogador):
    jogador = 'X' if vez_do_jogador % 2 == 0 else 'O'
    acc = 0
    for i in range(3):
        if matriz_jogo[i][len(matriz_jogo) - 1 - i] == jogador:
            acc += 1
        if acc == 3:
            return True


def verificar_jogadas(matriz_jogo,vez_do_jogador):# faça verificacao de jogadas
    return horizontal(matriz_jogo,vez_do_jogador) or vertical(matriz_jogo,vez_do_jogador) or diagonal(matriz_jogo,vez_do_jogador) or diagonal_invertida(matriz_jogo,vez_do_jogador)


def trocar_valores(matriz_jogo,user1=None,user2=None,vez=None):
    jogador_ver = 'X' if vez % 2 == 0 else 'O'
    jogadores = user1 if vez % 2 == 0 else user2
    for i in range(3):
        for j in range(3):
            if  jogadores == matriz_jogo[i][j]:
                matriz_jogo[i][j] = jogador_ver

    menu_jogo(matriz_jogo)


def jogadas(matriz_jogo,numeros_restantes):
    menu_jogo(matriz_jogo)

    for i in range(2,11):
        print('Jogada', i-1)
        if i % 2 == 0:
            while True:
                user1 = int(input('user1 Digite a posicao 1 a 8: '))
                if user1 <= 8 and user1 in numeros_restantes:
                    numeros_restantes.remove(user1)
                    break
                else:
                    print('Digite indice correto, ou esse numero ja foi escolhido')
            trocar_valores(matriz_jogo,user1,vez=i)
            if verificar_jogadas(matriz_jogo,vez_do_jogador=i):
                return 'Jogador1 ganhou'

        else:
            while True:
                user2_ = int(input('user2 Digite a posicao 1 a 8: '))
                if user2_ <= 8 and user2_ in numeros_restantes:
                    numeros_restantes.remove(user2_)
                    break
                else:
                    print('Digite indice correto ou esse numero ja foi escolhido')
            trocar_valores(matriz_jogo,user2=user2_,vez=i)
            if verificar_jogadas(matriz_jogo,vez_do_jogador=i):
                return 'Jogador 2 Ganhou'
    return 'Deu velha!!!'


jogadas(matriz_jogo,numeros_restantes)
