#!/usr/bin/env python3
"""
This file defines the BitBoard class.
"""
import numpy as np
import textwrap


class BitBoard:
    """
    This class is used to encapsulate a 64-bit integer to use as a chessboard of bits.
    """

    def __init__(self, board):
        """
        Run when a BitBoard object is created.
        """
        # a 64-bit integer that represents the bitboard
        self.num = np.uint64(board)

    def __getitem__(self, n):
        """
        Allows using [] operator for a BitBoard object to retrieve nth bit from the right
        :return: nth bit from the right
        """
        return (self.num >> np.uint64(n)) & np.uint64(1)

    def __setitem__(self, n, bit):
        """
        Allows using [] operator for a BitBoard object to set nth bit from the right
        """
        if self[n] != bit:
            self.num ^= (np.uint64(1) << np.uint64(n))

    def __str__(self):
        """
        Overrides default function to a string showing a 8x8 chessboard with bits
        :return: a string of 64 bits
        """
        return textwrap.fill('{:064b}'.format(self.num), 8)

    def __and__(self, other):
        """
        Returns the result of bitwise and (&) of two BitBoard objects
        :param other: a BitBoard object to AND with self
        :return: the result of bitwise and (&) of two BitBoard objects
        """
        return BitBoard(self.num & other.num)

    def __or__(self, other):
        """
        Returns the result of bitwise or (|) of two BitBoard objects
        :param other: a BitBoard object to OR with self
        :return: the result of bitwise or (|) of two BitBoard objects
        """
        return BitBoard(self.num | other.num)


# only runs when this module is called directly
if __name__ == '__main__':
    bb = BitBoard(1)
    print(bb[0])
    print(bb[1])
    print(bb)
