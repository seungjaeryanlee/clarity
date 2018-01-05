#!/usr/bin/env python3
"""
This script runs Clarity Chess in UCI (Universal Chess Interface) mode.
"""
import sys

from .Board import Board
from .Move import Move
from .MoveType import MoveType
from .Sq import Sq


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
                print(fen)
                board = Board(fen)
                moves = options[6:]

            for move in moves:
                # change move format from str to Move
                init_sq = Sq.filerank_to_sq(move[0:2])
                dest_sq = Sq.filerank_to_sq(move[2:4])
                # TODO detect correct movetype
                move_type = MoveType.QUIET
                board.make_move(Move(init_sq, dest_sq, move_type))


# only runs when this module is called directly
if __name__ == '__main__':
    uci()
