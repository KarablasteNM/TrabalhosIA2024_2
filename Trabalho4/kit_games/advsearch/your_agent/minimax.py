import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    value, action = max_move(state, state.player, max_depth, eval_func, depth = 0)
    return action

def max_move(state, player, max_depth:int, eval_func:Callable, depth:int = 0, alpha = float('-inf'), beta = float('inf')):
    if state.is_terminal() or depth == max_depth:
        return eval_func(state, player), None
    best_value = float('-inf')
    best_action = None
    for move in state.legal_moves():
        sucessor = state.next_state(move)
        value, _ = min_move(sucessor, player, max_depth, eval_func, depth + 1, alpha, beta)
        if value > best_value:
            best_value = value
            best_action = move
        alpha = max(alpha, best_value)
        if alpha >= beta:
            break
    return best_value, best_action

def min_move(state, player, max_depth:int, eval_func:Callable, depth:int = 0, alpha = float('-inf'), beta = float('inf')):
    if state.is_terminal() or depth == max_depth:
        return eval_func(state, player), None
    best_value = float('inf')
    best_action = None
    for move in state.legal_moves():
        sucessor = state.next_state(move)
        value, _ = max_move(sucessor, player, max_depth, eval_func, depth + 1, alpha, beta)
        if value < best_value:
            best_value = value
            best_action = move
        beta = min(beta, best_value)
        if beta <= alpha:
            break
    return best_value, best_action
