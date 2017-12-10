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

    @staticmethod
    def to_char(piece):
        """
        Returns the character notation of the given piece
        :param piece: the piece to return the character notation of
        :return: the character notation of the given piece
        """
        # TODO validate piece or add default value for dictionary?
        return {
            Piece.WP: 'P',
            Piece.WN: 'N',
            Piece.WB: 'B',
            Piece.WR: 'R',
            Piece.WQ: 'Q',
            Piece.WK: 'K',
            Piece.BP: 'p',
            Piece.BN: 'n',
            Piece.BB: 'b',
            Piece.BR: 'r',
            Piece.BQ: 'q',
            Piece.BK: 'k',
        }[piece]


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

    print(Piece.to_char(Piece.WP))
    print(Piece.to_char(Piece.WN))
    print(Piece.to_char(Piece.WB))
    print(Piece.to_char(Piece.WR))
    print(Piece.to_char(Piece.WQ))
    print(Piece.to_char(Piece.WK))
    print(Piece.to_char(Piece.BP))
    print(Piece.to_char(Piece.BN))
    print(Piece.to_char(Piece.BB))
    print(Piece.to_char(Piece.BR))
    print(Piece.to_char(Piece.BQ))
    print(Piece.to_char(Piece.BK))
