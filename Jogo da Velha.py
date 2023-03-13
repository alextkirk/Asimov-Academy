import random
import os

os.system('cls')

class Jogo_da_Velha:
    def __init__(self):
        self.lista_tabuleiro = [[' ',' ',' '] for i in range(3)]
        self.tabuleiro()

    def tabuleiro(self):
        os.system('cls')
        for i in range(len(self.lista_tabuleiro)):
            print('|', end='')
            for j in range(len(self.lista_tabuleiro[i])):
                print('{:^3}'.format(self.lista_tabuleiro[i][j]), end='|')
            print('\n {}'.format('-' * 12))

    def reset_tabuleiro(self):
        self.lista_tabuleiro.clear
        self.lista_tabuleiro = [[' ',' ',' '] for i in range(3)]

    def resultado_jogo(self):
        for l in range(3):
            if self.lista_tabuleiro[l][0] == self.lista_tabuleiro[l][1] and self.lista_tabuleiro[l][0] == self.lista_tabuleiro[l][2]:
                if self.lista_tabuleiro[l][0] == 'X':
                    print('Você ganhou!')
                    return True
                    break
                if self.lista_tabuleiro[l][0] == 'O':
                    print('O computador ganhou!')
                    return True
                    break
        for c in range(3):
            if self.lista_tabuleiro[0][c] == self.lista_tabuleiro[1][c] and self.lista_tabuleiro[0][c] == self.lista_tabuleiro[2][c]:
                if self.lista_tabuleiro[0][c] == 'X':
                    print('Você ganhou!')
                    return True
                    break
                if self.lista_tabuleiro[0][c] == 'O':
                    print('O computador ganhou!')
                    return True
                    break



    def jogada_player(self):
        print("Digite a linha do seu próximo lance:")
        l = int(input())
        print("Digite a coluna do seu próximo lance:")
        c = int(input())
        while self.lista_tabuleiro[l][c] != ' ':
            print('Posição não disponível, por favor digite outra jogada:')
            print("Digite a linha do seu próximo lance:")
            l = int(input())
            print("Digite a coluna do seu próximo lance:")
            c = int(input())
        self.lista_tabuleiro[l][c] = 'X'

    def jogada_computador(self):
        l = random.randint(0,2)
        c = random.randint(0,2)
        while self.lista_tabuleiro[l][c] != ' ':
            l = random.randint(0,2)
            c = random.randint(0,2)
        self.lista_tabuleiro[l][c] = 'O'


j = Jogo_da_Velha()
while True:
    j.jogada_player()
    j.jogada_computador()
    j.tabuleiro()
    if j.resultado_jogo() == True:
        break
