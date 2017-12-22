#!/usr/bin/env python3
"""
This file defines the recursion functions.
"""
from .Board import Board


def perft(board, depth):
    """
    Returns the number of nodes (depth)-ply deep from the given (board).

    Parameters
    ----------
    board : Board
        the board to search nodes from
    depth : int
        the depth to search nodes for

    Returns
    -------
    int
        the number of nodes (depth)-ply deep from the given (board).
    """
    # TODO untested

    if depth == 0:
        return 1

    nodes = 0

    moves = board.move_gen()
    for move in moves:
        captured_piece, castling, ep_square, half_move_count = board.make_move(move)
        nodes += perft(board, depth-1)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_count)

    return nodes


def negamax(board, depth):
    """
    Returns the best move on the given board after a search of given depth.

    Parameters
    ----------
    board : Board
        the board to find the best move for
    depth : int
        how deep to search to determine the best move

    Returns
    -------
    Move
        the best move determined by Clarity's evaluation algorithm
    """
    # TODO untested

    # TODO check for terminal node (i.e. checkmate, stalemate)
    if depth == 0:
        return board.eval()

    best_score = -999999
    best_move = None

    moves = board.move_gen()
    for move in moves:
        captured_piece, castling, ep_square, half_move_count = board.make_move(move)

        score = -_negamax_recur(board, depth - 1)
        if score > best_score:
            best_score = score
            best_move = move

        board.undo_move(move, captured_piece, castling, ep_square, half_move_count)

    return best_move


def _negamax_recur(board, depth):
    """
    Returns the best evaluation score of all possible board positions after [depth] moves on the given [board].

    Parameters
    ----------
    board : Board
        the board to find the best evaluation score for
    depth : int
        how deep to search to determine the best evaluation score

    Returns
    -------
    int
        the evaluation score of the best board position determined by Clarity's evaluation algorithm
    """
    # TODO untested

    # TODO check for terminal node (i.e. checkmate, stalemate)
    if depth == 0:
        return board.eval()

    best_score = -999999

    moves = board.move_gen()
    for move in moves:
        captured_piece, castling, ep_square, half_move_count = board.make_move(move)

        score = -_negamax_recur(board, depth - 1)
        if score > best_score:
            best_score = score

        board.undo_move(move, captured_piece, castling, ep_square, half_move_count)

    return best_score


# only runs when this module is called directly
if __name__ == '__main__':
    print(perft(Board(), 3))
    print(negamax(Board(), 2))
