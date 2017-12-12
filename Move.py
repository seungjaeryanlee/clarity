#!/usr/bin/env python3
"""
This file defines the Board class.
"""
import numpy as np
from MoveType import MoveType
from Sq import Sq


class Move:
    """
    This class represents a chess move.
    """

    def __init__(self, init, dest, move_type):
        """
        Run when a Board object is created.
        """
        # 16 bit number for encoded move
        # first 6 bits: initial square
        # next 6 bits: destination square
        # 4 bits: move type
        self.num = np.uint16(init)
        self.num = self.num << 6
        self.num += np.uint16(dest)
        self.num = self.num << 4
        self.num += np.uint16(move_type)

    def __lt__(self, other):
        """
        Returns True if self < other for their underlying 16 bit numbers, otherwise False.
        Used for calling sorted() on a list of moves.
        """
        return self.num < other.num

    def init_sq(self):
        """
        Returns the bit index of the initial square
        :return: the bit index of the initial square
        """
        return self.num >> np.uint16(10)

    def dest_sq(self):
        """
        Returns the bit index of the destination square
        :return: the bit index of the destination square
        """
        return (self.num >> np.uint16(4)) & np.uint16(63)

    def move_type(self):
        """
        Returns the move type index
        :return: the move type index
        """
        return MoveType(self.num & np.uint16(15))


# only runs when this module is called directly
if __name__ == '__main__':
    move = Move(Sq.E2, Sq.E4, MoveType.QUIET)
    print('{0:b}'.format(move.num))
    print('Init: ' + str(Sq(move.init_sq())))
    print('Dest: ' + str(Sq(move.dest_sq())))
    print('Type: ' + str(move.move_type()))
