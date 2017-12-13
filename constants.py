#!/usr/bin/env python3
"""
This file defines the constants used in Clarity.
"""
from BitBoard import BitBoard
from Direction import Direction
from Piece import Piece
from Sq import Sq


# Move bitboards for pawns
_MOVE_WP = [
    # no pawn can exist on row 1
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(int('10000', 16)),  # Sq.H2
    BitBoard(int('20000', 16)),  # Sq.G2
    BitBoard(int('40000', 16)),  # Sq.F2
    BitBoard(int('80000', 16)),  # Sq.E2
    BitBoard(int('100000', 16)),  # Sq.D2
    BitBoard(int('200000', 16)),  # Sq.C2
    BitBoard(int('400000', 16)),  # Sq.B2
    BitBoard(int('800000', 16)),  # Sq.A2
    BitBoard(int('1000000', 16)),  # Sq.H3
    BitBoard(int('2000000', 16)),  # Sq.G3
    BitBoard(int('4000000', 16)),  # Sq.F3
    BitBoard(int('8000000', 16)),  # Sq.E3
    BitBoard(int('10000000', 16)),  # Sq.D3
    BitBoard(int('20000000', 16)),  # Sq.C3
    BitBoard(int('40000000', 16)),  # Sq.B3
    BitBoard(int('80000000', 16)),  # Sq.A3
    BitBoard(int('100000000', 16)),  # Sq.H4
    BitBoard(int('200000000', 16)),  # Sq.G4
    BitBoard(int('400000000', 16)),  # Sq.F4
    BitBoard(int('800000000', 16)),  # Sq.E4
    BitBoard(int('1000000000', 16)),  # Sq.D4
    BitBoard(int('2000000000', 16)),  # Sq.C4
    BitBoard(int('4000000000', 16)),  # Sq.B4
    BitBoard(int('8000000000', 16)),  # Sq.A4
    BitBoard(int('10000000000', 16)),  # Sq.H5
    BitBoard(int('20000000000', 16)),  # Sq.G5
    BitBoard(int('40000000000', 16)),  # Sq.F5
    BitBoard(int('80000000000', 16)),  # Sq.E5
    BitBoard(int('100000000000', 16)),  # Sq.D5
    BitBoard(int('200000000000', 16)),  # Sq.C5
    BitBoard(int('400000000000', 16)),  # Sq.B5
    BitBoard(int('800000000000', 16)),  # Sq.A5
    BitBoard(int('1000000000000', 16)),  # Sq.H6
    BitBoard(int('2000000000000', 16)),  # Sq.G6
    BitBoard(int('4000000000000', 16)),  # Sq.F6
    BitBoard(int('8000000000000', 16)),  # Sq.E6
    BitBoard(int('10000000000000', 16)),  # Sq.D6
    BitBoard(int('20000000000000', 16)),  # Sq.C6
    BitBoard(int('40000000000000', 16)),  # Sq.B6
    BitBoard(int('80000000000000', 16)),  # Sq.A6

    # white pawns on row 7 can only make promotion moves
    BitBoard(0),  # Sq.H7
    BitBoard(0),  # Sq.G7
    BitBoard(0),  # Sq.F7
    BitBoard(0),  # Sq.E7
    BitBoard(0),  # Sq.D7
    BitBoard(0),  # Sq.C7
    BitBoard(0),  # Sq.B7
    BitBoard(0),  # Sq.A7

    # no pawn can exist on row 8
    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

_MOVE_BP = [
    # no pawn can exist on row 1
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    # black pawns on row 2 can only make promotion moves
    BitBoard(0),  # Sq.H2
    BitBoard(0),  # Sq.G2
    BitBoard(0),  # Sq.F2
    BitBoard(0),  # Sq.E2
    BitBoard(0),  # Sq.D2
    BitBoard(0),  # Sq.C2
    BitBoard(0),  # Sq.B2
    BitBoard(0),  # Sq.A2

    BitBoard(int('100', 16)),  # Sq.H3
    BitBoard(int('200', 16)),  # Sq.G3
    BitBoard(int('400', 16)),  # Sq.F3
    BitBoard(int('800', 16)),  # Sq.E3
    BitBoard(int('1000', 16)),  # Sq.D3
    BitBoard(int('2000', 16)),  # Sq.C3
    BitBoard(int('4000', 16)),  # Sq.B3
    BitBoard(int('8000', 16)),  # Sq.A3
    BitBoard(int('10000', 16)),  # Sq.H4
    BitBoard(int('20000', 16)),  # Sq.G4
    BitBoard(int('40000', 16)),  # Sq.F4
    BitBoard(int('80000', 16)),  # Sq.E4
    BitBoard(int('100000', 16)),  # Sq.D4
    BitBoard(int('200000', 16)),  # Sq.C4
    BitBoard(int('400000', 16)),  # Sq.B4
    BitBoard(int('800000', 16)),  # Sq.A4
    BitBoard(int('1000000', 16)),  # Sq.H5
    BitBoard(int('2000000', 16)),  # Sq.G5
    BitBoard(int('4000000', 16)),  # Sq.F5
    BitBoard(int('8000000', 16)),  # Sq.E5
    BitBoard(int('10000000', 16)),  # Sq.D5
    BitBoard(int('20000000', 16)),  # Sq.C5
    BitBoard(int('40000000', 16)),  # Sq.B5
    BitBoard(int('80000000', 16)),  # Sq.A5
    BitBoard(int('100000000', 16)),  # Sq.H6
    BitBoard(int('200000000', 16)),  # Sq.G6
    BitBoard(int('400000000', 16)),  # Sq.F6
    BitBoard(int('800000000', 16)),  # Sq.E6
    BitBoard(int('1000000000', 16)),  # Sq.D6
    BitBoard(int('2000000000', 16)),  # Sq.C6
    BitBoard(int('4000000000', 16)),  # Sq.B6
    BitBoard(int('8000000000', 16)),  # Sq.A6
    BitBoard(int('10000000000', 16)),  # Sq.H7
    BitBoard(int('20000000000', 16)),  # Sq.G7
    BitBoard(int('40000000000', 16)),  # Sq.F7
    BitBoard(int('80000000000', 16)),  # Sq.E7
    BitBoard(int('100000000000', 16)),  # Sq.D7
    BitBoard(int('200000000000', 16)),  # Sq.C7
    BitBoard(int('400000000000', 16)),  # Sq.B7
    BitBoard(int('800000000000', 16)),  # Sq.A7

    # no pawn can exist on row 8
    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

# double pawn push bitboards
_DOUBLE_WP = [BitBoard(0)] * 64
# only white pawns on row 2 can do double pawn push
_DOUBLE_WP[Sq.A2] = BitBoard(int('80000000', 16))
_DOUBLE_WP[Sq.B2] = BitBoard(int('40000000', 16))
_DOUBLE_WP[Sq.C2] = BitBoard(int('20000000', 16))
_DOUBLE_WP[Sq.D2] = BitBoard(int('10000000', 16))
_DOUBLE_WP[Sq.E2] = BitBoard(int('8000000', 16))
_DOUBLE_WP[Sq.F2] = BitBoard(int('4000000', 16))
_DOUBLE_WP[Sq.G2] = BitBoard(int('2000000', 16))
_DOUBLE_WP[Sq.H2] = BitBoard(int('1000000', 16))

_DOUBLE_BP = [BitBoard(0)] * 64
# only black pawns on row 7 can do double pawn push
_DOUBLE_BP[Sq.A7] = BitBoard(int('8000000000', 16))
_DOUBLE_BP[Sq.B7] = BitBoard(int('4000000000', 16))
_DOUBLE_BP[Sq.C7] = BitBoard(int('2000000000', 16))
_DOUBLE_BP[Sq.D7] = BitBoard(int('1000000000', 16))
_DOUBLE_BP[Sq.E7] = BitBoard(int('800000000', 16))
_DOUBLE_BP[Sq.F7] = BitBoard(int('400000000', 16))
_DOUBLE_BP[Sq.G7] = BitBoard(int('200000000', 16))
_DOUBLE_BP[Sq.H7] = BitBoard(int('100000000', 16))

MOVE_P = {
    Piece.WP: _MOVE_WP,
    Piece.BP: _MOVE_BP,
}
DOUBLE_P = {
    Piece.WP: _DOUBLE_WP,
    Piece.BP: _DOUBLE_BP,
}

# Attack bitboards
# TODO fill data
_ATTACK_WP = [

    # no pawn can exist on row 1
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(int('20000', 16)),  # Sq.H2
    BitBoard(int('50000', 16)),  # Sq.G2
    BitBoard(int('A0000', 16)),  # Sq.F2
    BitBoard(int('140000', 16)),  # Sq.E2
    BitBoard(int('280000', 16)),  # Sq.D2
    BitBoard(int('500000', 16)),  # Sq.C2
    BitBoard(int('A00000', 16)),  # Sq.B2
    BitBoard(int('400000', 16)),  # Sq.A2
    BitBoard(int('2000000', 16)),  # Sq.H3
    BitBoard(int('5000000', 16)),  # Sq.G3
    BitBoard(int('A000000', 16)),  # Sq.F3
    BitBoard(int('14000000', 16)),  # Sq.E3
    BitBoard(int('28000000', 16)),  # Sq.D3
    BitBoard(int('50000000', 16)),  # Sq.C3
    BitBoard(int('A0000000', 16)),  # Sq.B3
    BitBoard(int('40000000', 16)),  # Sq.A3
    BitBoard(int('200000000', 16)),  # Sq.H4
    BitBoard(int('500000000', 16)),  # Sq.G4
    BitBoard(int('A00000000', 16)),  # Sq.F4
    BitBoard(int('1400000000', 16)),  # Sq.E4
    BitBoard(int('2800000000', 16)),  # Sq.D4
    BitBoard(int('5000000000', 16)),  # Sq.C4
    BitBoard(int('A000000000', 16)),  # Sq.B4
    BitBoard(int('4000000000', 16)),  # Sq.A4
    BitBoard(int('20000000000', 16)),  # Sq.H5
    BitBoard(int('50000000000', 16)),  # Sq.G5
    BitBoard(int('A0000000000', 16)),  # Sq.F5
    BitBoard(int('140000000000', 16)),  # Sq.E5
    BitBoard(int('280000000000', 16)),  # Sq.D5
    BitBoard(int('500000000000', 16)),  # Sq.C5
    BitBoard(int('A00000000000', 16)),  # Sq.B5
    BitBoard(int('400000000000', 16)),  # Sq.A5
    BitBoard(int('2000000000000', 16)),  # Sq.H6
    BitBoard(int('5000000000000', 16)),  # Sq.G6
    BitBoard(int('A000000000000', 16)),  # Sq.F6
    BitBoard(int('14000000000000', 16)),  # Sq.E6
    BitBoard(int('28000000000000', 16)),  # Sq.D6
    BitBoard(int('50000000000000', 16)),  # Sq.C6
    BitBoard(int('A0000000000000', 16)),  # Sq.B6
    BitBoard(int('40000000000000', 16)),  # Sq.A6

    # white pawns on row 7 can only make promotion capture moves
    BitBoard(0),  # Sq.H7
    BitBoard(0),  # Sq.G7
    BitBoard(0),  # Sq.F7
    BitBoard(0),  # Sq.E7
    BitBoard(0),  # Sq.D7
    BitBoard(0),  # Sq.C7
    BitBoard(0),  # Sq.B7
    BitBoard(0),  # Sq.A7

    # no pawn can exist on row 8
    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]
_ATTACK_BP = [

    # no pawn can exist on row 1
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    # black pawns on row 2 can only make promotion capture moves
    BitBoard(0),  # Sq.H2
    BitBoard(0),  # Sq.G2
    BitBoard(0),  # Sq.F2
    BitBoard(0),  # Sq.E2
    BitBoard(0),  # Sq.D2
    BitBoard(0),  # Sq.C2
    BitBoard(0),  # Sq.B2
    BitBoard(0),  # Sq.A2

    BitBoard(int('200', 16)),  # Sq.H3
    BitBoard(int('500', 16)),  # Sq.G3
    BitBoard(int('A00', 16)),  # Sq.F3
    BitBoard(int('1400', 16)),  # Sq.E3
    BitBoard(int('2800', 16)),  # Sq.D3
    BitBoard(int('5000', 16)),  # Sq.C3
    BitBoard(int('A000', 16)),  # Sq.B3
    BitBoard(int('4000', 16)),  # Sq.A3
    BitBoard(int('20000', 16)),  # Sq.H4
    BitBoard(int('50000', 16)),  # Sq.G4
    BitBoard(int('A0000', 16)),  # Sq.F4
    BitBoard(int('140000', 16)),  # Sq.E4
    BitBoard(int('280000', 16)),  # Sq.D4
    BitBoard(int('500000', 16)),  # Sq.C4
    BitBoard(int('A00000', 16)),  # Sq.B4
    BitBoard(int('400000', 16)),  # Sq.A4
    BitBoard(int('2000000', 16)),  # Sq.H5
    BitBoard(int('5000000', 16)),  # Sq.G5
    BitBoard(int('A000000', 16)),  # Sq.F5
    BitBoard(int('14000000', 16)),  # Sq.E5
    BitBoard(int('28000000', 16)),  # Sq.D5
    BitBoard(int('50000000', 16)),  # Sq.C5
    BitBoard(int('A0000000', 16)),  # Sq.B5
    BitBoard(int('40000000', 16)),  # Sq.A5
    BitBoard(int('200000000', 16)),  # Sq.H6
    BitBoard(int('500000000', 16)),  # Sq.G6
    BitBoard(int('A00000000', 16)),  # Sq.F6
    BitBoard(int('1400000000', 16)),  # Sq.E6
    BitBoard(int('2800000000', 16)),  # Sq.D6
    BitBoard(int('5000000000', 16)),  # Sq.C6
    BitBoard(int('A000000000', 16)),  # Sq.B6
    BitBoard(int('4000000000', 16)),  # Sq.A6

    # no pawn can exist on row 8
    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]


_ATTACK_N = [BitBoard(0)] * 64
_ATTACK_N[Sq.B1] = BitBoard(int('00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '10100000'
                                '00010000'
                                '00000000', 2))
_ATTACK_N[Sq.G1] = BitBoard(int('00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '00000101'
                                '00001000'
                                '00000000', 2))

_ATTACK_B_UL = [BitBoard(0)] * 64
_ATTACK_B_UL[Sq.H1] = BitBoard(int('10000000'
                                   '01000000'
                                   '00100000'
                                   '00010000'
                                   '00001000'
                                   '00000100'
                                   '00000010'
                                   '00000000', 2))
_ATTACK_B_UL[Sq.F3] = BitBoard(int('10000000'
                                   '01000000'
                                   '00100000'
                                   '00010000'
                                   '00001000'
                                   '00000000'
                                   '00000000'
                                   '00000000', 2))
_ATTACK_B_UL[Sq.G1] = BitBoard(int('00000000'
                                   '10000000'
                                   '01000000'
                                   '00100000'
                                   '00010000'
                                   '00001000'
                                   '00000100'
                                   '00000000', 2))
_ATTACK_B_UR = [BitBoard(0)] * 64
_ATTACK_B_UR[Sq.F3] = BitBoard(int('00000000'
                                   '00000000'
                                   '00000000'
                                   '00000001'
                                   '00000010'
                                   '00000000'
                                   '00000000'
                                   '00000000', 2))
_ATTACK_B_UR[Sq.G1] = BitBoard(int('00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000001'
                                   '00000000', 2))
_ATTACK_B_DL = [BitBoard(0)] * 64
_ATTACK_B_DL[Sq.F3] = BitBoard(int('00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00001000'
                                   '00010000', 2))
_ATTACK_B_DR = [BitBoard(0)] * 64
_ATTACK_B_DR[Sq.F3] = BitBoard(int('00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000000'
                                   '00000010'
                                   '00000001', 2))

_ATTACK_B = {
    Direction.UL: _ATTACK_B_UL,
    Direction.UR: _ATTACK_B_UR,
    Direction.DL: _ATTACK_B_DL,
    Direction.DR: _ATTACK_B_DR,
}

_ATTACK_R_U = [
    BitBoard(int('101010101010100', 16)),  # Sq.H1
    BitBoard(int('202020202020200', 16)),  # Sq.G1
    BitBoard(int('404040404040400', 16)),  # Sq.F1
    BitBoard(int('808080808080800', 16)),  # Sq.E1
    BitBoard(int('1010101010101000', 16)),  # Sq.D1
    BitBoard(int('2020202020202000', 16)),  # Sq.C1
    BitBoard(int('4040404040404000', 16)),  # Sq.B1
    BitBoard(int('8080808080808000', 16)),  # Sq.A1

    BitBoard(int('101010101010000', 16)),  # Sq.H2
    BitBoard(int('202020202020000', 16)),  # Sq.G2
    BitBoard(int('404040404040000', 16)),  # Sq.F2
    BitBoard(int('808080808080000', 16)),  # Sq.E2
    BitBoard(int('1010101010100000', 16)),  # Sq.D2
    BitBoard(int('2020202020200000', 16)),  # Sq.C2
    BitBoard(int('4040404040400000', 16)),  # Sq.B2
    BitBoard(int('8080808080800000', 16)),  # Sq.A2

    BitBoard(int('101010101000000', 16)),  # Sq.H3
    BitBoard(int('202020202000000', 16)),  # Sq.G3
    BitBoard(int('404040404000000', 16)),  # Sq.F3
    BitBoard(int('808080808000000', 16)),  # Sq.E3
    BitBoard(int('1010101010000000', 16)),  # Sq.D3
    BitBoard(int('2020202020000000', 16)),  # Sq.C3
    BitBoard(int('4040404040000000', 16)),  # Sq.B3
    BitBoard(int('8080808080000000', 16)),  # Sq.A3

    BitBoard(int('101010100000000', 16)),  # Sq.H4
    BitBoard(int('202020200000000', 16)),  # Sq.G4
    BitBoard(int('404040400000000', 16)),  # Sq.F4
    BitBoard(int('808080800000000', 16)),  # Sq.E4
    BitBoard(int('1010101000000000', 16)),  # Sq.D4
    BitBoard(int('2020202000000000', 16)),  # Sq.C4
    BitBoard(int('4040404000000000', 16)),  # Sq.B4
    BitBoard(int('8080808000000000', 16)),  # Sq.A4

    BitBoard(int('101010000000000', 16)),  # Sq.H5
    BitBoard(int('202020000000000', 16)),  # Sq.G5
    BitBoard(int('404040000000000', 16)),  # Sq.F5
    BitBoard(int('808080000000000', 16)),  # Sq.E5
    BitBoard(int('1010100000000000', 16)),  # Sq.D5
    BitBoard(int('2020200000000000', 16)),  # Sq.C5
    BitBoard(int('4040400000000000', 16)),  # Sq.B5
    BitBoard(int('8080800000000000', 16)),  # Sq.A5

    BitBoard(int('101000000000000', 16)),  # Sq.H6
    BitBoard(int('202000000000000', 16)),  # Sq.G6
    BitBoard(int('404000000000000', 16)),  # Sq.F6
    BitBoard(int('808000000000000', 16)),  # Sq.E6
    BitBoard(int('1010000000000000', 16)),  # Sq.D6
    BitBoard(int('2020000000000000', 16)),  # Sq.C6
    BitBoard(int('4040000000000000', 16)),  # Sq.B6
    BitBoard(int('8080000000000000', 16)),  # Sq.A6

    BitBoard(int('100000000000000', 16)),  # Sq.H6
    BitBoard(int('200000000000000', 16)),  # Sq.G6
    BitBoard(int('400000000000000', 16)),  # Sq.F6
    BitBoard(int('800000000000000', 16)),  # Sq.E6
    BitBoard(int('1000000000000000', 16)),  # Sq.D6
    BitBoard(int('2000000000000000', 16)),  # Sq.C6
    BitBoard(int('4000000000000000', 16)),  # Sq.B6
    BitBoard(int('8000000000000000', 16)),  # Sq.A6

    # nowhere to go up if the rook is on row 8
    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

_ATTACK_R_D = [
    # nowhere to go down if the rook is on row 1
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(int('1', 16)),  # Sq.H2
    BitBoard(int('2', 16)),  # Sq.G2
    BitBoard(int('4', 16)),  # Sq.F2
    BitBoard(int('8', 16)),  # Sq.E2
    BitBoard(int('10', 16)),  # Sq.D2
    BitBoard(int('20', 16)),  # Sq.C2
    BitBoard(int('40', 16)),  # Sq.B2
    BitBoard(int('80', 16)),  # Sq.A2

    BitBoard(int('101', 16)),  # Sq.H3
    BitBoard(int('202', 16)),  # Sq.G3
    BitBoard(int('404', 16)),  # Sq.F3
    BitBoard(int('808', 16)),  # Sq.E3
    BitBoard(int('1010', 16)),  # Sq.D3
    BitBoard(int('2020', 16)),  # Sq.C3
    BitBoard(int('4040', 16)),  # Sq.B3
    BitBoard(int('8080', 16)),  # Sq.A3

    BitBoard(int('10101', 16)),  # Sq.H4
    BitBoard(int('20202', 16)),  # Sq.G4
    BitBoard(int('40404', 16)),  # Sq.F4
    BitBoard(int('80808', 16)),  # Sq.E4
    BitBoard(int('101010', 16)),  # Sq.D4
    BitBoard(int('202020', 16)),  # Sq.C4
    BitBoard(int('404040', 16)),  # Sq.B4
    BitBoard(int('808080', 16)),  # Sq.A4

    BitBoard(int('1010101', 16)),  # Sq.H5
    BitBoard(int('2020202', 16)),  # Sq.G5
    BitBoard(int('4040404', 16)),  # Sq.F5
    BitBoard(int('8080808', 16)),  # Sq.E5
    BitBoard(int('10101010', 16)),  # Sq.D5
    BitBoard(int('20202020', 16)),  # Sq.C5
    BitBoard(int('40404040', 16)),  # Sq.B5
    BitBoard(int('80808080', 16)),  # Sq.A5

    BitBoard(int('101010101', 16)),  # Sq.H6
    BitBoard(int('202020202', 16)),  # Sq.G6
    BitBoard(int('404040404', 16)),  # Sq.F6
    BitBoard(int('808080808', 16)),  # Sq.E6
    BitBoard(int('1010101010', 16)),  # Sq.D6
    BitBoard(int('2020202020', 16)),  # Sq.C6
    BitBoard(int('4040404040', 16)),  # Sq.B6
    BitBoard(int('8080808080', 16)),  # Sq.A6

    BitBoard(int('10101010101', 16)),  # Sq.H7
    BitBoard(int('20202020202', 16)),  # Sq.G7
    BitBoard(int('40404040404', 16)),  # Sq.F7
    BitBoard(int('80808080808', 16)),  # Sq.E7
    BitBoard(int('101010101010', 16)),  # Sq.D7
    BitBoard(int('202020202020', 16)),  # Sq.C7
    BitBoard(int('404040404040', 16)),  # Sq.B7
    BitBoard(int('808080808080', 16)),  # Sq.A7

    BitBoard(int('1010101010101', 16)),  # Sq.H8
    BitBoard(int('2020202020202', 16)),  # Sq.G8
    BitBoard(int('4040404040404', 16)),  # Sq.F8
    BitBoard(int('8080808080808', 16)),  # Sq.E8
    BitBoard(int('10101010101010', 16)),  # Sq.D8
    BitBoard(int('20202020202020', 16)),  # Sq.C8
    BitBoard(int('40404040404040', 16)),  # Sq.B8
    BitBoard(int('80808080808080', 16)),  # Sq.A8
]

_ATTACK_R_L = [BitBoard(0)] * 64
_ATTACK_R_L[Sq.H1] = BitBoard(int('00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '11111110', 2))
_ATTACK_R_L[Sq.G1] = BitBoard(int('00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '11111100', 2))

_ATTACK_R_R = [
    BitBoard(0),  # Sq.H1
    BitBoard(int('1', 16)),  # Sq.G1
    BitBoard(int('3', 16)),  # Sq.F1
    BitBoard(int('7', 16)),  # Sq.E1
    BitBoard(int('F', 16)),  # Sq.D1
    BitBoard(int('1F', 16)),  # Sq.C1
    BitBoard(int('3F', 16)),  # Sq.B1
    BitBoard(int('7F', 16)),  # Sq.A1

    BitBoard(0),  # Sq.H2
    BitBoard(int('100', 16)),  # Sq.G2
    BitBoard(int('300', 16)),  # Sq.F2
    BitBoard(int('700', 16)),  # Sq.E2
    BitBoard(int('F00', 16)),  # Sq.D2
    BitBoard(int('1F00', 16)),  # Sq.C2
    BitBoard(int('3F00', 16)),  # Sq.B2
    BitBoard(int('7F00', 16)),  # Sq.A2

    BitBoard(0),  # Sq.H3
    BitBoard(int('10000', 16)),  # Sq.G3
    BitBoard(int('30000', 16)),  # Sq.F3
    BitBoard(int('70000', 16)),  # Sq.E3
    BitBoard(int('F0000', 16)),  # Sq.D3
    BitBoard(int('1F0000', 16)),  # Sq.C3
    BitBoard(int('3F0000', 16)),  # Sq.B3
    BitBoard(int('7F0000', 16)),  # Sq.A3

    BitBoard(0),  # Sq.H4
    BitBoard(int('1000000', 16)),  # Sq.G4
    BitBoard(int('3000000', 16)),  # Sq.F4
    BitBoard(int('7000000', 16)),  # Sq.E4
    BitBoard(int('F000000', 16)),  # Sq.D4
    BitBoard(int('1F000000', 16)),  # Sq.C4
    BitBoard(int('3F000000', 16)),  # Sq.B4
    BitBoard(int('7F000000', 16)),  # Sq.A4

    BitBoard(0),  # Sq.H5
    BitBoard(int('100000000', 16)),  # Sq.G5
    BitBoard(int('300000000', 16)),  # Sq.F5
    BitBoard(int('700000000', 16)),  # Sq.E5
    BitBoard(int('F00000000', 16)),  # Sq.D5
    BitBoard(int('1F00000000', 16)),  # Sq.C5
    BitBoard(int('3F00000000', 16)),  # Sq.B5
    BitBoard(int('7F00000000', 16)),  # Sq.A5

    BitBoard(0),  # Sq.H6
    BitBoard(int('10000000000', 16)),  # Sq.G6
    BitBoard(int('30000000000', 16)),  # Sq.F6
    BitBoard(int('70000000000', 16)),  # Sq.E6
    BitBoard(int('F0000000000', 16)),  # Sq.D6
    BitBoard(int('1F0000000000', 16)),  # Sq.C6
    BitBoard(int('3F0000000000', 16)),  # Sq.B6
    BitBoard(int('7F0000000000', 16)),  # Sq.A6

    BitBoard(0),  # Sq.H7
    BitBoard(int('1000000000000', 16)),  # Sq.G7
    BitBoard(int('3000000000000', 16)),  # Sq.F7
    BitBoard(int('7000000000000', 16)),  # Sq.E7
    BitBoard(int('F000000000000', 16)),  # Sq.D7
    BitBoard(int('1F000000000000', 16)),  # Sq.C7
    BitBoard(int('3F000000000000', 16)),  # Sq.B7
    BitBoard(int('7F000000000000', 16)),  # Sq.A7

    BitBoard(0),  # Sq.H8
    BitBoard(int('100000000000000', 16)),  # Sq.G8
    BitBoard(int('300000000000000', 16)),  # Sq.F8
    BitBoard(int('700000000000000', 16)),  # Sq.E8
    BitBoard(int('F00000000000000', 16)),  # Sq.D8
    BitBoard(int('1F00000000000000', 16)),  # Sq.C8
    BitBoard(int('3F00000000000000', 16)),  # Sq.B8
    BitBoard(int('7F00000000000000', 16)),  # Sq.A8
]

_ATTACK_R = {
    Direction.U: _ATTACK_R_U,
    Direction.D: _ATTACK_R_D,
    Direction.L: _ATTACK_R_L,
    Direction.R: _ATTACK_R_R,
}

_ATTACK_Q = {
    Direction.UL: _ATTACK_B_UL,
    Direction.UR: _ATTACK_B_UR,
    Direction.DL: _ATTACK_B_DL,
    Direction.DR: _ATTACK_B_DR,
    Direction.U: _ATTACK_R_U,
    Direction.D: _ATTACK_R_D,
    Direction.L: _ATTACK_R_L,
    Direction.R: _ATTACK_R_R,
}

_ATTACK_K = [
    BitBoard(int('302', 16)),  # Sq.H1
    BitBoard(int('705', 16)),  # Sq.G1
    BitBoard(int('E0A', 16)),  # Sq.F1
    BitBoard(int('1C14', 16)),  # Sq.E1
    BitBoard(int('3828', 16)),  # Sq.D1
    BitBoard(int('7050', 16)),  # Sq.C1
    BitBoard(int('E0A0', 16)),  # Sq.B1
    BitBoard(int('C040', 16)),  # Sq.A1

    BitBoard(int('30203', 16)),  # Sq.H2
    BitBoard(int('70507', 16)),  # Sq.G2
    BitBoard(int('E0A0E', 16)),  # Sq.F2
    BitBoard(int('1C141C', 16)),  # Sq.E2
    BitBoard(int('382838', 16)),  # Sq.D2
    BitBoard(int('705070', 16)),  # Sq.C2
    BitBoard(int('E0A0E0', 16)),  # Sq.B2
    BitBoard(int('C040C0', 16)),  # Sq.A2
    BitBoard(int('3020300', 16)),  # Sq.H3
    BitBoard(int('7050700', 16)),  # Sq.G3
    BitBoard(int('E0A0E00', 16)),  # Sq.F3
    BitBoard(int('1C141C00', 16)),  # Sq.E3
    BitBoard(int('38283800', 16)),  # Sq.D3
    BitBoard(int('70507000', 16)),  # Sq.C3
    BitBoard(int('E0A0E000', 16)),  # Sq.B3
    BitBoard(int('C040C000', 16)),  # Sq.A3
    BitBoard(int('302030000', 16)),  # Sq.H4
    BitBoard(int('705070000', 16)),  # Sq.G4
    BitBoard(int('E0A0E0000', 16)),  # Sq.F4
    BitBoard(int('1C141C0000', 16)),  # Sq.E4
    BitBoard(int('3828380000', 16)),  # Sq.D4
    BitBoard(int('7050700000', 16)),  # Sq.C4
    BitBoard(int('E0A0E00000', 16)),  # Sq.B4
    BitBoard(int('C040C00000', 16)),  # Sq.A4
    BitBoard(int('30203000000', 16)),  # Sq.H5
    BitBoard(int('70507000000', 16)),  # Sq.G5
    BitBoard(int('E0A0E000000', 16)),  # Sq.F5
    BitBoard(int('1C141C000000', 16)),  # Sq.E5
    BitBoard(int('382838000000', 16)),  # Sq.D5
    BitBoard(int('705070000000', 16)),  # Sq.C5
    BitBoard(int('E0A0E0000000', 16)),  # Sq.B5
    BitBoard(int('C040C0000000', 16)),  # Sq.A5
    BitBoard(int('3020300000000', 16)),  # Sq.H6
    BitBoard(int('7050700000000', 16)),  # Sq.G6
    BitBoard(int('E0A0E00000000', 16)),  # Sq.F6
    BitBoard(int('1C141C00000000', 16)),  # Sq.E6
    BitBoard(int('38283800000000', 16)),  # Sq.D6
    BitBoard(int('70507000000000', 16)),  # Sq.C6
    BitBoard(int('E0A0E000000000', 16)),  # Sq.B6
    BitBoard(int('C040C000000000', 16)),  # Sq.A6
    BitBoard(int('302030000000000', 16)),  # Sq.H7
    BitBoard(int('705070000000000', 16)),  # Sq.G7
    BitBoard(int('E0A0E0000000000', 16)),  # Sq.F7
    BitBoard(int('1C141C0000000000', 16)),  # Sq.E7
    BitBoard(int('3828380000000000', 16)),  # Sq.D7
    BitBoard(int('7050700000000000', 16)),  # Sq.C7
    BitBoard(int('E0A0E00000000000', 16)),  # Sq.B7
    BitBoard(int('C040C00000000000', 16)),  # Sq.A7

    BitBoard(int('203000000000000', 16)),  # Sq.H8
    BitBoard(int('507000000000000', 16)),  # Sq.G8
    BitBoard(int('A0E000000000000', 16)),  # Sq.F8
    BitBoard(int('141C000000000000', 16)),  # Sq.E8
    BitBoard(int('2838000000000000', 16)),  # Sq.D8
    BitBoard(int('5070000000000000', 16)),  # Sq.C8
    BitBoard(int('A0E0000000000000', 16)),  # Sq.B8
    BitBoard(int('2060000000000000', 16)),  # Sq.A8
]

ATTACK = {
    Piece.WP: _ATTACK_WP,
    Piece.WN: _ATTACK_N,
    Piece.WB: _ATTACK_B,
    Piece.WR: _ATTACK_R,
    Piece.WQ: _ATTACK_Q,
    Piece.WK: _ATTACK_K,
    Piece.BP: _ATTACK_BP,
    Piece.BN: _ATTACK_N,
    Piece.BB: _ATTACK_B,
    Piece.BR: _ATTACK_R,
    Piece.BQ: _ATTACK_Q,
    Piece.BK: _ATTACK_K,
}
