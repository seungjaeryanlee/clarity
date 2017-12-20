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

    def __init__(self, uint64_number):
        """
        Run when a BitBoard object is created.

        Parameters
        ----------
        uint64_number : int or numpy.uint64
                        a 64-bit unsigned integer to initialize the BitBoard to.
        """
        # a 64-bit integer that represents the bitboard
        self.num = np.uint64(uint64_number)

    def __getitem__(self, n):
        """
        Allows using [] operator for a BitBoard object to retrieve nth bit from the right.

        Parameters
        ----------
        n : int
            the index of the bit to retrieve, counting from right to left.

        Returns
        -------
        int
            the bit from the right.
        """
        return (self.num >> np.uint64(n)) & np.uint64(1)

    def __setitem__(self, n, bit):
        """
        Allows using [] operator for a BitBoard object to set the nth bit from the right.

        Parameters
        ----------
        n : int
            the index of the bit to set, counting from right to left.
        bit : int
            the value to set the nth bit to. Should be 0 or 1.
        """
        if self[n] != bit:
            self.num ^= (np.uint64(1) << np.uint64(n))

    def __str__(self):
        """
        Overrides default function to a string showing a 8x8 chessboard with bits.

        Returns
        -------
        str
            a string of 64 bits with line breaks for every 8 bits.
        """
        return textwrap.fill('{:064b}'.format(self.num), 8)

    def __and__(self, other):
        """
        Allows using the AND operator (&) for two BitBoard objects. Returns the result of a bitwise and (&) of self
        and other.

        Parameters
        ----------
        other : BitBoard
            a BitBoard object to AND with self

        Returns
        -------
        BitBoard
            the result of a bitwise and (&) of self and other
        """
        return BitBoard(self.num & other.num)

    def __or__(self, other):
        """
        Allows using the OR operator (|) for two BitBoard objects. Returns the result of a bitwise or (|) of self and
        other.

        Parameters
        ----------
        other : BitBoard
            a BitBoard object to OR with self

        Returns
        -------
        BitBoard
            the result of a bitwise or (|) of self and other.
        """
        return BitBoard(self.num | other.num)

    def __invert__(self):
        """
        Allows using the NOT operator (~) on a BitBoard object. Returns the inverse of the encapsulated 64-bit unsigned
        integer.

        Returns
        -------
        BitBoard
            the inverse of the encapsulated 64-bit unsigned integer
        """
        return BitBoard(~self.num)

    def __eq__(self, other):
        """
        Allows using the equality operator (==) on a BitBoard object. Returns True if self and other have the same
        number, False otherwise.

        Parameters
        ----------
        other : BitBoard
            a BitBoard object to check equality against

        Returns
        -------
        bool
            True if self and other have the same number, False otherwise.
        """
        # TODO considering allowing other to be either Int or BitBoard type
        return self.num == other.num

    def indices(self):
        """
        Returns the indices of bits with value 1.

        Returns
        -------
        list of int
            the indices of bits with value 1
        """
        bits = []
        for i in range(64):
            if self[i] == 1:
                bits.append(i)
        return bits


# only runs when this module is called directly
if __name__ == '__main__':
    bb = BitBoard(1)
    print(bb[0])
    print(bb[1])
    print(bb)
