#!/usr/bin/env python3
"""
This file defines the Color enum.
"""
from enum import Enum


class Color(Enum):
    """
    This enum contains names and values for colors of piece or turn.
    """

    WHITE = 0
    BLACK = 1
    NEITHER = 2

    @staticmethod
    def switch(color):
        """
        Returns the opposite color of the given color

        Returns
        -------
        Color
            the opposite color of the given color
        """
        if color == Color.WHITE:
            return Color.BLACK
        if color == Color.BLACK:
            return Color.WHITE
        return Color.NEITHER


# only runs when this module is called directly
if __name__ == '__main__':
    print(Color.WHITE)
    print(Color.BLACK)
    print(Color.NEITHER)
