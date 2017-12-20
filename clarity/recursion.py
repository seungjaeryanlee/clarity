#!/usr/bin/env python3
"""
This file defines the recursion functions.
"""
from clarity.Board import Board


def perft(board, depth):
    """
    Returns the number of nodes (depth)-ply deep from the given (board).

    :param :class:`Board` board: the board to search nodes from
    :param int depth: the depth to search nodes for
    :return: the number of nodes (depth)-ply deep from the given (board).
    :rtype: int
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

# only runs when this module is called directly
if __name__ == '__main__':
    print(perft(Board(), 3))
