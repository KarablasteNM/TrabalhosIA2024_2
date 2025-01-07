import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
import time
import threading

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo retorna uma jogada ilegal
    # Remova-o e coloque a sua implementacao do MCTS

    return monte_carlo_movimento(state)  

# Função que retorna o vencedor
def contar_peças(state):
    tabuleiro = state.get_board().tiles
    preto = sum(row.count('B') for row in tabuleiro)
    branco = sum(row.count('W') for row in tabuleiro)
    return 'B' if preto > branco else 'W' if branco > preto else 'empate'

# Função de Monte Carlo para simular várias partidas a partir de um estado específico
def monte_carlo_movimento(state, iteracoes=15):
    jogador_atual = state.player
    melhor_taxa_vitoria = 0
    # Obter todos os movimentos válidos para o jogador atual
    movimentos_validos = state.legal_moves()
    if len(movimentos_validos) > 1:
        # Simular as partidas para cada movimento válido
        for mov in movimentos_validos:
            vitorias = 0
            empates = 0
            # Simular o jogo para esse movimento
            for _ in range(iteracoes):
                state_copy = state.copy()
                state_copy = state_copy.next_state(mov)
                
                while not state_copy.is_terminal():
                    movimentos_validos_internos = state_copy.legal_moves()
                    if movimentos_validos_internos:
                        state_copy = state_copy.next_state(random.choice(list(movimentos_validos_internos)))

                vencedor = contar_peças(state_copy)
                if vencedor == jogador_atual:
                    vitorias += 1
                elif vencedor == 'empate':
                    empates += 1

            taxa_vitoria = vitorias / iteracoes

            # Verificar se este movimento tem a maior taxa de vitória
            if taxa_vitoria > melhor_taxa_vitoria:
                melhor_taxa_vitoria = taxa_vitoria
                melhor_movimento = mov
    else:
        melhor_movimento = list(movimentos_validos)[0]

    # Retornar o(s) movimento(s) com a maior chance de vitória
    return melhor_movimento