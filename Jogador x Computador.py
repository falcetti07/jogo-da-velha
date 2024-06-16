import random

def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True

    # Verifica colunas
    for col in range(3):
        if all([tabuleiro[linha][col] == jogador for linha in range(3)]):
            return True

    # Verifica diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True

    return False

def tabuleiro_cheio(tabuleiro):
    return all([celula != ' ' for linha in tabuleiro for celula in linha])

def movimento_valido(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' '

def obter_movimento_jogador():
    while True:
        try:
            linha = int(input("Entre com a linha (0, 1, 2): "))
            coluna = int(input("Entre com a coluna (0, 1, 2): "))
            if 0 <= linha <= 2 and 0 <= coluna <= 2:
                return linha, coluna
            else:
                print("Linha e coluna devem ser entre 0 e 2.")
        except ValueError:
            print("Por favor, entre com números válidos.")

def obter_movimento_maquina(tabuleiro):
    movimentos_possiveis = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] == ' ']
    return random.choice(movimentos_possiveis)

def jogo_da_velha():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = 'X'
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        
        if jogador_atual == 'X':
            linha, coluna = obter_movimento_jogador()
        else:
            linha, coluna = obter_movimento_maquina(tabuleiro)
            print(f"Máquina escolheu linha {linha} e coluna {coluna}")
        
        if movimento_valido(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vencedor(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break
            elif tabuleiro_cheio(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Movimento inválido, tente novamente.")

jogo_da_velha()
