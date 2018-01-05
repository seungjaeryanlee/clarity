#!/usr/bin/env python3
"""
This script runs Clarity Chess in UCI (Universal Chess Interface) mode.
"""
import sys

from .Board import Board
from .Move import Move
from .MoveType import MoveType
from .recursion import negamax
from .Sq import Sq


def detect_move_type(board, init_sq, dest_sq):
    """

    Parameters
    ----------
    board: Board
        the board that the move will be made on
    init_sq: Sq or int
        the destination square of the move to find the MoveType for
    dest_sq: Sq or int
        the destination square of the move to find the MoveType for

    Returns
    -------
    Move
        the Move with the correct MoveType with given init_sq and dest_sq
    """
    # TODO implement
    # TODO untested
    return Move(init_sq, dest_sq, MoveType.QUIET)


def uci():
    """
    Runs Clarity in UCI mode
    """
    while True:
        line = sys.stdin.readline().strip()
        command = line.split(' ')[0]
        options = line.split(' ')[1:]

        if command == 'uci':
            print('id name Clarity')
            print('id author Seung Jae (Ryan) Lee')
            print('uciok')

        if command == 'isready':
            print('readyok')

        if command == 'quit':
            return

        if command == 'position':
            if options[0] == 'startpos':
                board = Board()
                moves = options[1:]
            else:
                fen = ' '.join(options[0:6])
                board = Board(fen)
                moves = options[6:]

            for move in moves:
                # change move format from str to Move
                init_sq = Sq.filerank_to_sq(move[0:2])
                dest_sq = Sq.filerank_to_sq(move[2:4])
                board.make_move(detect_move_type(board, init_sq, dest_sq))

        if command == 'go':
            best_move = negamax(board, 2)
            print('bestmove ' + best_move.short_str())


# only runs when this module is called directly
if __name__ == '__main__':
    uci()
