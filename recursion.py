#!/usr/bin/env python3
"""
This file defines the recursion functions.
"""
from Board import Board


def perft(board, depth):
    """
    Returns the number of nodes (depth)-ply deep from the given (board).
    :param board: the board to search nodes from
    :param depth: the depth to search nodes for
    :return: the number of nodes (depth)-ply deep from the given (board).
    """
    if depth == 0:
        return 1

    nodes = 0

    moves = board.move_gen()
    for move in moves:
        board.make_move(move)
        nodes += perft(board, depth-1)
        # TODO implement Board.undo_move()
        board.undo_move(move)

    return nodes

# only runs when this module is called directly
if __name__ == '__main__':
    print(perft(Board(), 1))
