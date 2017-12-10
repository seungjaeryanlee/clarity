#!/usr/bin/env python3
"""
This file defines the Board class.
"""
from BitBoard import BitBoard


class Board:
    """
    This class represents the status of a board.
    """

    def __init__(self):
        """
        Run when a Board object is created.
        """
        # bitboard for each piece on their starting positions
        self.wp = BitBoard(65280)
        self.wn = BitBoard(66)
        self.wb = BitBoard(36)
        self.wr = BitBoard(129)
        self.wq = BitBoard(16)
        self.wk = BitBoard(8)
        self.bp = BitBoard(71776119061217280)
        self.bn = BitBoard(4755801206503243776)
        self.bb = BitBoard(2594073385365405696)
        self.br = BitBoard(9295429630892703744)
        self.bq = BitBoard(1152921504606846976)
        self.bk = BitBoard(576460752303423488)


# only runs when this module is called directly
if __name__ == '__main__':
    board = Board()
    print("White Pawns:")
    print(board.wp)
    print("White Knights:")
    print(board.wn)
    print("White Bishops:")
    print(board.wb)
    print("White Rooks:")
    print(board.wr)
    print("White Queen:")
    print(board.wq)
    print("White King:")
    print(board.wk)
    print("Black Pawns:")
    print(board.bp)
    print("Black Knights:")
    print(board.bn)
    print("Black Bishops:")
    print(board.bb)
    print("Black Rooks:")
    print(board.br)
    print("Black Queen:")
    print(board.bq)
    print("Black King:")
    print(board.bk)
