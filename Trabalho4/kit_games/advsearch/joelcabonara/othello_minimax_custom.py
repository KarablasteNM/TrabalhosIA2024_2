import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 5, evaluate_custom)

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

def evaluate_custom(state, player: str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    opponent = Board.opponent(player)
    if state.is_terminal():
        winner = state.winner()
        if winner == player:
            return 999999
        elif winner == opponent:
            return -999999
        else:
            return 0
        
    board = state.get_board()

    player_pieces = board.num_pieces(player)
    opponent_pieces = board.num_pieces(opponent)
    piece_difference = player_pieces - opponent_pieces

    corner_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]
    player_corners = sum(1 for pos in corner_positions if board.tiles[pos[1]][pos[0]] == player)
    opponent_corners = sum(1 for pos in corner_positions if board.tiles[pos[1]][pos[0]] == opponent)
    corner_difference = player_corners - opponent_corners

    edges = [(x, y) for x in range(8) for y in range(8) if x in [0, 7] or y in [0, 7]]
    player_edges = sum(1 for pos in edges if board.tiles[pos[1]][pos[0]] == player)
    opponent_edges = sum(1 for pos in edges if board.tiles[pos[1]][pos[0]] == opponent)
    edge_difference = player_edges - opponent_edges

    player_mobility = len(state.legal_moves())
    opponent_mobility = len(GameState(board, opponent).legal_moves())
    mobility_difference = player_mobility - opponent_mobility

    player_positional_score = sum(
        EVAL_TEMPLATE[x][y] for x in range(8) for y in range(8) if board.tiles[y][x] == player
    )
    opponent_positional_score = sum(
        EVAL_TEMPLATE[x][y] for x in range(8) for y in range(8) if board.tiles[y][x] == opponent
    )
    positional_difference = player_positional_score - opponent_positional_score

    total_pieces = player_pieces + opponent_pieces
    if total_pieces < 20:
        score = (8 * mobility_difference + 25 * corner_difference + 2 * edge_difference + 10 * positional_difference)
    elif total_pieces < 44: 
        score = (7 * mobility_difference + 40 * corner_difference + 3 * edge_difference + 20 * positional_difference + 3 * piece_difference)
    else:
        score = (20 * piece_difference + 50 * corner_difference + 5 * edge_difference + 10 * positional_difference)
    return score
