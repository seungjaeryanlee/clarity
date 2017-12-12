#!/usr/bin/env python3
"""
This file defines the MoveType enum.
"""
from enum import IntEnum


class MoveType(IntEnum):
    """
    This enum contains values for possible move types.
    """

    # following this flag set: https://chessprogramming.wikispaces.com/Encoding+Moves
    QUIET = 0  # quiet moves
    DOUBLE = 1  # double pawn push
    K_CASTLE = 2  # king castling
    Q_CASTLE = 3  # queen castling
    CAPTURE = 4  # capture
    EP_CAPTURE = 5  # en passant capture
    N_PROMO = 8  # promotion to knight
    B_PROMO = 9  # promotion to bishop
    R_PROMO = 10  # promotion to rook
    Q_PROMO = 11  # promotion to queen
    N_PROMO_CAPTURE = 12  # promotion to knight
    B_PROMO_CAPTURE = 13  # promotion to bishop
    R_PROMO_CAPTURE = 14  # promotion to rook
    Q_PROMO_CAPTURE = 15  # promotion to queen


# only runs when this module is called directly
if __name__ == '__main__':
    for m_type in MoveType:
        print(m_type)
