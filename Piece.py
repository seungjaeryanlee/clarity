#!/usr/bin/env python3
"""
This file defines the Piece enum.
"""
from enum import Enum
from Color import Color


class Piece(Enum):
    """
    This enum contains names and values for each chess piece
    """

    WP = 0
    WN = 1
    WB = 2
    WR = 3
    WQ = 4
    WK = 5
    BP = 6
    BN = 7
    BB = 8
    BR = 9
    BQ = 10
    BK = 11

    @staticmethod
    def color(piece):
        """
        Returns the color of the given piece. If given piece is not in the enum, returns Color.WHITE by default.
        :param piece: piece to check its color
        :return: the color of the given piece or if not piece, Color.WHITE
        """
        return Color.BLACK if piece in {Piece.BP, Piece.BN, Piece.BB, Piece.BR, Piece.BQ, Piece.BK} else Color.WHITE


# only runs when this module is called directly
if __name__ == '__main__':
    print(Piece.WP)
    print(Piece.WN)
    print(Piece.WB)
    print(Piece.WR)
    print(Piece.WQ)
    print(Piece.WK)
    print(Piece.BP)
    print(Piece.BN)
    print(Piece.BB)
    print(Piece.BR)
    print(Piece.BQ)
    print(Piece.BK)
