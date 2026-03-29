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

def verificar_jogadas(matriz_jogo,vez_do_jogador):# verificacao de jogadas
    return horizontal(matriz_jogo,vez_do_jogador) or vertical(matriz_jogo,vez_do_jogador) or diagonal(matriz_jogo,vez_do_jogador) or diagonal_invertida(matriz_jogo,vez_do_jogador)

def trocar_valores(matriz_jogo,user,vez=None):
    jogador_ver = 'X' if vez % 2 == 0 else 'O'
    for i in range(3):
        for j in range(3):
            if  user == matriz_jogo[i][j]:
                matriz_jogo[i][j] = jogador_ver
    print(f'====jogada{vez}====')
    menu_jogo(matriz_jogo)

def vez_jogadores(jogador,matriz_jogo,numeros_restantes,indice):
    print('\nVez do ',jogador)
    while True:
        try:
            user = int(input('Digite a posicao 0 a 8: '))
            if user <= 8 and user in numeros_restantes:
                numeros_restantes.remove(user)
                break
            else:
                print('Digite indice incorreto, ou esse numero ja foi escolhido')
        except ValueError:
            print('apenas numeros!!')
    trocar_valores(matriz_jogo,user,vez=indice)
    

def jogadas(matriz_jogo,numeros_restantes):
    jogador1 = input('Digite nome do jogador 1: ')
    jogador2 = input('Digite nome do jogador 2: ')
    print('====Jogada 1====')
    menu_jogo(matriz_jogo)
    for i in range(2,11):
        if i % 2 == 0: # jogador 1
            vez_jogadores(jogador1,matriz_jogo,numeros_restantes,indice=i)
            if verificar_jogadas(matriz_jogo,vez_do_jogador=i):
                return f'{jogador1}, Ganhou!!'
        else: # jogador 2
            vez_jogadores(jogador2,matriz_jogo,numeros_restantes,indice=i)
            if verificar_jogadas(matriz_jogo,vez_do_jogador=i):
                return f'{jogador2}, Ganhou!!'
            
    return 'Deu velha!!!'

print(jogadas(matriz_jogo,numeros_restantes))
