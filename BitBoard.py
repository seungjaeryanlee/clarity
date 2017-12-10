#!/usr/bin/env python3
"""
This file defines the BitBoard class.
"""
import numpy as np


class BitBoard:
    """
    This class is used to encapsulate a 64-bit integer to use as a chessboard of bits.
    """

    def __init__(self, board):
        """
        Run when a BitBoard object is created.
        """
        # a 64-bit integer that represents the bitboard
        self.board = np.uint64(board)

    def __getitem__(self, n):
        """
        Allows using [] operator for a BitBoard object to retrieve nth bit from the right
        :return: nth bit from the right
        """
        return (self.board >> np.uint64(n)) & np.uint64(1)


# only runs when this module is called directly
if __name__ == '__main__':
    bb = BitBoard(1)
    print(bb[0])
    print(bb[1])
