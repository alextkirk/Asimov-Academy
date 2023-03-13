import random
import os

os.system('cls')

class Jogo_da_Velha:
    def __init__(self):
        self.reset_tabuleiro()

    def tabuleiro(self):
        print("")
        print(" " + self.lista_tabuleiro[0][0] + " | " + self.lista_tabuleiro[0][1] + " | " + self.lista_tabuleiro[0][2])
        print("-" * 11)
        print(" " + self.lista_tabuleiro[1][0] + " | " + self.lista_tabuleiro[1][1] + " | " + self.lista_tabuleiro[1][2])
        print("-" * 11)
        print(" " + self.lista_tabuleiro[2][0] + " | " + self.lista_tabuleiro[2][1] + " | " + self.lista_tabuleiro[2][2])

    def reset_tabuleiro(self):
        self.lista_tabuleiro.clear
        self.lista_tabuleiro = [[' ',' ',' '] for i in range(3)]

    def resultado_jogo(self):
        dict_win = {}

        for i in ['X', 'O']:
            # Horizontal
            dict_win[i] = (self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2])
            dict_win[i] = (self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2]) or dict_win[i]
            dict_win[i] = (self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2]) or dict_win[i]

            # Vertical
            dict_win[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0]) or dict_win[i]
            dict_win[i] = (self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1]) or dict_win[i]
            dict_win[i] = (self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2]) or dict_win[i]

            # Diagonais
            dict_win[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2]) or dict_win[i]
            dict_win[i] = (self.tabuleiro[2][2] == self.tabuleiro[1][1] == self.tabuleiro[0][0]) or dict_win[i]

        if dict_win['X']:
            self.done = 'X'
            print('Você venceu, parabéns!')
            return

        elif dict_win['O']:
            self.donw = 'O'
            print('O computador venceu!')
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != ' ':
                    c += 1
                    break

        if c == 0:
            self.done = 'Empate'
            print('Empate!')
            return


    def jogada_player(self):
        invalid_mode = True

        while invalid_mode:
            try:
                print('Digite a linha do seu próximo lance:')
                l = int(input())
                print('Digite a coluna do seu próximo lance:')
                c = int(input())

                if l > 2 or l < 0 or c > 2 or c < 0:
                    print('Coordenadas inválidas!')

                if self.tabuleiro[l][c] != ' ':
                    print('Posição já preenchida.')
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_mode = False
            self.tabuleiro[l][c] = 'X'
            
            
    def jogada_computador(self):
        pass

j = Jogo_da_Velha()
j.tabuleiro()