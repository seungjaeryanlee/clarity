#!/usr/bin/env python3
"""
This file defines the Board class.
"""
import numpy as np
from .MoveType import MoveType
from .Sq import Sq


class Move:
    """
    This class represents a chess move.
    """

    def __init__(self, init, dest, move_type):
        """
        Run when a Board object is created.

        Parameters
        ----------
        init : int or Sq
            initial square of the move.
        dest : int or Sq
            destination square of the move.
        move_type : MoveType
            type of move.
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

    def __eq__(self, other):
        """
        Allows using the equality operator (==) on a Move object. Returns True if self and other have the initial
        and destination square and same move type. Returns False otherwise.

        Parameters
        ----------
        other : Move
            the Move to check equality against

        Returns
        -------
        bool
            True if self and other have the same initial and destination squares and move type, False otherwise.
        """
        return self.num == other.num

    def __lt__(self, other):
        """
        Allows calling sorted() on a list of moves. Returns True if self < other for their underlying 16 bit numbers,
        otherwise False.

        Parameters
        ----------
        other : Move
            the Move to compare against

        Returns
        -------
        bool
            True if self < other for their underlying 16 bit numbers. False otherwise.
        """
        return self.num < other.num

    def __repr__(self):
        """
        Overrides default function to a string with initial square (Sq), destination square (Sq)and move type (MoveType)
        This allows for "correct" output when Move objects are printed in lists.

        Returns
        -------
        str
            A string with initial square, destination square and move type written separated by spaces.
        """
        return str(self)

    def __str__(self):
        """
        Overrides default function to a string with initial square (Sq), destination square (Sq)and move type (MoveType)

        Returns
        -------
        str
            A string with initial square, destination square and move type written separated by spaces.
        """
        return str(Sq(self.init_sq())) + ' ' + str(Sq(self.dest_sq())) + ' ' + str(self.move_type())

    def init_sq(self):
        """
        Returns the bit index of the initial square

        Returns
        -------
        int
            the bit index of the initial square
        """
        return self.num >> np.uint16(10)

    def dest_sq(self):
        """
        Returns the bit index of the destination square

        Returns
        -------
        int
            the bit index of the destination square
        """
        return (self.num >> np.uint16(4)) & np.uint16(63)

    def move_type(self):
        """
        Returns the move type index

        Returns
        -------
        int
            the move type index
        """
        return MoveType(self.num & np.uint16(15))


# only runs when this module is called directly
if __name__ == '__main__':
    move = Move(Sq.E2, Sq.E4, MoveType.QUIET)
    print('{0:b}'.format(move.num))
    print('Init: ' + str(Sq(move.init_sq())))
    print('Dest: ' + str(Sq(move.dest_sq())))
    print('Type: ' + str(move.move_type()))
