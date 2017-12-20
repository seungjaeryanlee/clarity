#!/usr/bin/env python3
"""
This file defines the constants used in Clarity.
"""
from clarity.BitBoard import BitBoard
from clarity.Direction import Direction
from clarity.Piece import Piece
from clarity.Sq import Sq


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

# quiet promotion bitboards
_PROMO_WP = [BitBoard(0)] * 64
# only white pawns on row 7 can be promoted quietly
_PROMO_WP[Sq.A7] = BitBoard(int('8000000000000000', 16))
_PROMO_WP[Sq.B7] = BitBoard(int('4000000000000000', 16))
_PROMO_WP[Sq.C7] = BitBoard(int('2000000000000000', 16))
_PROMO_WP[Sq.D7] = BitBoard(int('1000000000000000', 16))
_PROMO_WP[Sq.E7] = BitBoard(int('800000000000000', 16))
_PROMO_WP[Sq.F7] = BitBoard(int('400000000000000', 16))
_PROMO_WP[Sq.G7] = BitBoard(int('200000000000000', 16))
_PROMO_WP[Sq.H7] = BitBoard(int('100000000000000', 16))

_PROMO_BP = [BitBoard(0)] * 64
# only black pawns on row 2 can be promoted quietly
_PROMO_BP[Sq.A2] = BitBoard(int('80', 16))
_PROMO_BP[Sq.B2] = BitBoard(int('40', 16))
_PROMO_BP[Sq.C2] = BitBoard(int('20', 16))
_PROMO_BP[Sq.D2] = BitBoard(int('10', 16))
_PROMO_BP[Sq.E2] = BitBoard(int('8', 16))
_PROMO_BP[Sq.F2] = BitBoard(int('4', 16))
_PROMO_BP[Sq.G2] = BitBoard(int('2', 16))
_PROMO_BP[Sq.H2] = BitBoard(int('1', 16))

PROMO_P = {
    Piece.WP: _PROMO_WP,
    Piece.BP: _PROMO_BP,
}

# capture promotion bitboards
_PROMO_CAPTURE_WP = [BitBoard(0)] * 64
# only white pawns on row 7 can be promoted with a capture
_PROMO_CAPTURE_WP[Sq.A7] = BitBoard(int('4000000000000000', 16))
_PROMO_CAPTURE_WP[Sq.B7] = BitBoard(int('A000000000000000', 16))
_PROMO_CAPTURE_WP[Sq.C7] = BitBoard(int('5000000000000000', 16))
_PROMO_CAPTURE_WP[Sq.D7] = BitBoard(int('2800000000000000', 16))
_PROMO_CAPTURE_WP[Sq.E7] = BitBoard(int('1400000000000000', 16))
_PROMO_CAPTURE_WP[Sq.F7] = BitBoard(int('A00000000000000', 16))
_PROMO_CAPTURE_WP[Sq.G7] = BitBoard(int('500000000000000', 16))
_PROMO_CAPTURE_WP[Sq.H7] = BitBoard(int('200000000000000', 16))

_PROMO_CAPTURE_BP = [BitBoard(0)] * 64
# only black pawns on row 2 can be promoted with a capture
_PROMO_CAPTURE_BP[Sq.A2] = BitBoard(int('40', 16))
_PROMO_CAPTURE_BP[Sq.B2] = BitBoard(int('A0', 16))
_PROMO_CAPTURE_BP[Sq.C2] = BitBoard(int('50', 16))
_PROMO_CAPTURE_BP[Sq.D2] = BitBoard(int('28', 16))
_PROMO_CAPTURE_BP[Sq.E2] = BitBoard(int('14', 16))
_PROMO_CAPTURE_BP[Sq.F2] = BitBoard(int('A', 16))
_PROMO_CAPTURE_BP[Sq.G2] = BitBoard(int('5', 16))
_PROMO_CAPTURE_BP[Sq.H2] = BitBoard(int('2', 16))

PROMO_CAPTURE_P = {
    Piece.WP: _PROMO_CAPTURE_WP,
    Piece.BP: _PROMO_CAPTURE_BP,
}

# Attack bitboards
_ATTACK_WP = [

    # no pawn can exist on row 1, BUT these BitBoards are used in Board._get_attacking_sqs() to detect for black pawns
    # putting the white king on check
    BitBoard(int('200', 16)),  # Sq.H1
    BitBoard(int('500', 16)),  # Sq.G1
    BitBoard(int('A00', 16)),  # Sq.F1
    BitBoard(int('1400', 16)),  # Sq.E1
    BitBoard(int('2800', 16)),  # Sq.D1
    BitBoard(int('5000', 16)),  # Sq.C1
    BitBoard(int('A000', 16)),  # Sq.B1
    BitBoard(int('4000', 16)),  # Sq.A1

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
    BitBoard(int('20000000000', 16)),  # Sq.H7
    BitBoard(int('50000000000', 16)),  # Sq.G7
    BitBoard(int('A0000000000', 16)),  # Sq.F7
    BitBoard(int('140000000000', 16)),  # Sq.E7
    BitBoard(int('280000000000', 16)),  # Sq.D7
    BitBoard(int('500000000000', 16)),  # Sq.C7
    BitBoard(int('A00000000000', 16)),  # Sq.B7
    BitBoard(int('400000000000', 16)),  # Sq.A7

    # no pawn can exist on row 8, BUT these BitBoards are used in Board._get_attacking_sqs() to detect for white pawns
    # putting the black king on check
    BitBoard(int('2000000000000', 16)),  # Sq.H8
    BitBoard(int('5000000000000', 16)),  # Sq.G8
    BitBoard(int('A000000000000', 16)),  # Sq.F8
    BitBoard(int('14000000000000', 16)),  # Sq.E8
    BitBoard(int('28000000000000', 16)),  # Sq.D8
    BitBoard(int('50000000000000', 16)),  # Sq.C8
    BitBoard(int('A0000000000000', 16)),  # Sq.B8
    BitBoard(int('40000000000000', 16)),  # Sq.A8
]

_ATTACK_N = [
    BitBoard(int('020400', 16)),  # Sq.H1
    BitBoard(int('050800', 16)),  # Sq.G1
    BitBoard(int('0A1100', 16)),  # Sq.F1
    BitBoard(int('142200', 16)),  # Sq.E1
    BitBoard(int('284400', 16)),  # Sq.D1
    BitBoard(int('508800', 16)),  # Sq.C1
    BitBoard(int('A01000', 16)),  # Sq.B1
    BitBoard(int('402000', 16)),  # Sq.A1

    BitBoard(int('02040004', 16)),  # Sq.H2
    BitBoard(int('05080008', 16)),  # Sq.G2
    BitBoard(int('0A110011', 16)),  # Sq.F2
    BitBoard(int('14220022', 16)),  # Sq.E2
    BitBoard(int('28440044', 16)),  # Sq.D2
    BitBoard(int('50880088', 16)),  # Sq.C2
    BitBoard(int('A0100010', 16)),  # Sq.B2
    BitBoard(int('40200020', 16)),  # Sq.A2

    BitBoard(int('0204000402', 16)),  # Sq.H3
    BitBoard(int('0508000805', 16)),  # Sq.G3
    BitBoard(int('0A1100110A', 16)),  # Sq.F3
    BitBoard(int('1422002214', 16)),  # Sq.E3
    BitBoard(int('2844004428', 16)),  # Sq.D3
    BitBoard(int('5088008850', 16)),  # Sq.C3
    BitBoard(int('A0100010A0', 16)),  # Sq.B3
    BitBoard(int('4020002040', 16)),  # Sq.A3

    BitBoard(int('020400040200', 16)),  # Sq.H4
    BitBoard(int('050800080500', 16)),  # Sq.G4
    BitBoard(int('0A1100110A00', 16)),  # Sq.F4
    BitBoard(int('142200221400', 16)),  # Sq.E4
    BitBoard(int('284400442800', 16)),  # Sq.D4
    BitBoard(int('508800885000', 16)),  # Sq.C4
    BitBoard(int('A0100010A000', 16)),  # Sq.B4
    BitBoard(int('402000204000', 16)),  # Sq.A4

    BitBoard(int('02040004020000', 16)),  # Sq.H5
    BitBoard(int('05080008050000', 16)),  # Sq.G5
    BitBoard(int('0A1100110A0000', 16)),  # Sq.F5
    BitBoard(int('14220022140000', 16)),  # Sq.E5
    BitBoard(int('28440044280000', 16)),  # Sq.D5
    BitBoard(int('50880088500000', 16)),  # Sq.C5
    BitBoard(int('A0100010A00000', 16)),  # Sq.B5
    BitBoard(int('40200020400000', 16)),  # Sq.A5

    BitBoard(int('0204000402000000', 16)),  # Sq.H6
    BitBoard(int('0508000805000000', 16)),  # Sq.G6
    BitBoard(int('0A1100110A000000', 16)),  # Sq.F6
    BitBoard(int('1422002214000000', 16)),  # Sq.E6
    BitBoard(int('2844004428000000', 16)),  # Sq.D6
    BitBoard(int('5088008850000000', 16)),  # Sq.C6
    BitBoard(int('A0100010A0000000', 16)),  # Sq.B6
    BitBoard(int('4020002040000000', 16)),  # Sq.A6

    BitBoard(int('0400040200000000', 16)),  # Sq.H7
    BitBoard(int('0800080500000000', 16)),  # Sq.G7
    BitBoard(int('1100110A00000000', 16)),  # Sq.F7
    BitBoard(int('2200221400000000', 16)),  # Sq.E7
    BitBoard(int('4400442800000000', 16)),  # Sq.D7
    BitBoard(int('8800885000000000', 16)),  # Sq.C7
    BitBoard(int('100010A000000000', 16)),  # Sq.B7
    BitBoard(int('2000204000000000', 16)),  # Sq.A7

    BitBoard(int('0004020000000000', 16)),  # Sq.H8
    BitBoard(int('0008050000000000', 16)),  # Sq.G8
    BitBoard(int('00110A0000000000', 16)),  # Sq.F8
    BitBoard(int('0022140000000000', 16)),  # Sq.E8
    BitBoard(int('0044280000000000', 16)),  # Sq.D8
    BitBoard(int('0088500000000000', 16)),  # Sq.C8
    BitBoard(int('0010A00000000000', 16)),  # Sq.B8
    BitBoard(int('0020400000000000', 16)),  # Sq.A8
]

_ATTACK_B_UL = [
    BitBoard(int('8040201008040200', 16)),  # Sq.H1
    BitBoard(int('80402010080400', 16)),  # Sq.G1
    BitBoard(int('804020100800', 16)),  # Sq.F1
    BitBoard(int('8040201000', 16)),  # Sq.E1
    BitBoard(int('80402000', 16)),  # Sq.D1
    BitBoard(int('804000', 16)),  # Sq.C1
    BitBoard(int('8000', 16)),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(int('4020100804020000', 16)),  # Sq.H2
    BitBoard(int('8040201008040000', 16)),  # Sq.G2
    BitBoard(int('80402010080000', 16)),  # Sq.F2
    BitBoard(int('804020100000', 16)),  # Sq.E2
    BitBoard(int('8040200000', 16)),  # Sq.D2
    BitBoard(int('80400000', 16)),  # Sq.C2
    BitBoard(int('800000', 16)),  # Sq.B2
    BitBoard(0),  # Sq.A2

    BitBoard(int('2010080402000000', 16)),  # Sq.H3
    BitBoard(int('4020100804000000', 16)),  # Sq.G3
    BitBoard(int('8040201008000000', 16)),  # Sq.F3
    BitBoard(int('80402010000000', 16)),  # Sq.E3
    BitBoard(int('804020000000', 16)),  # Sq.D3
    BitBoard(int('8040000000', 16)),  # Sq.C3
    BitBoard(int('80000000', 16)),  # Sq.B3
    BitBoard(0),  # Sq.A3

    BitBoard(int('1008040200000000', 16)),  # Sq.H4
    BitBoard(int('2010080400000000', 16)),  # Sq.G4
    BitBoard(int('4020100800000000', 16)),  # Sq.F4
    BitBoard(int('8040201000000000', 16)),  # Sq.E4
    BitBoard(int('80402000000000', 16)),  # Sq.D4
    BitBoard(int('804000000000', 16)),  # Sq.C4
    BitBoard(int('8000000000', 16)),  # Sq.B4
    BitBoard(0),  # Sq.A4

    BitBoard(int('0804020000000000', 16)),  # Sq.H5
    BitBoard(int('1008040000000000', 16)),  # Sq.G5
    BitBoard(int('2010080000000000', 16)),  # Sq.F5
    BitBoard(int('4020100000000000', 16)),  # Sq.E5
    BitBoard(int('8040200000000000', 16)),  # Sq.D5
    BitBoard(int('80400000000000', 16)),  # Sq.C5
    BitBoard(int('800000000000', 16)),  # Sq.B5
    BitBoard(0),  # Sq.A5

    BitBoard(int('0402000000000000', 16)),  # Sq.H6
    BitBoard(int('0804000000000000', 16)),  # Sq.G6
    BitBoard(int('1008000000000000', 16)),  # Sq.F6
    BitBoard(int('2010000000000000', 16)),  # Sq.E6
    BitBoard(int('4020000000000000', 16)),  # Sq.D6
    BitBoard(int('8040000000000000', 16)),  # Sq.C6
    BitBoard(int('80000000000000', 16)),  # Sq.B6
    BitBoard(0),  # Sq.A6

    BitBoard(int('0200000000000000', 16)),  # Sq.H7
    BitBoard(int('0400000000000000', 16)),  # Sq.G7
    BitBoard(int('0800000000000000', 16)),  # Sq.F7
    BitBoard(int('1000000000000000', 16)),  # Sq.E7
    BitBoard(int('2000000000000000', 16)),  # Sq.D7
    BitBoard(int('4000000000000000', 16)),  # Sq.C7
    BitBoard(int('8000000000000000', 16)),  # Sq.B7
    BitBoard(0),  # Sq.A7

    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

_ATTACK_B_UR = [
    BitBoard(0),  # Sq.H1
    BitBoard(int('0100', 16)),  # Sq.G1
    BitBoard(int('010200', 16)),  # Sq.F1
    BitBoard(int('01020400', 16)),  # Sq.E1
    BitBoard(int('0102040800', 16)),  # Sq.D1
    BitBoard(int('010204081000', 16)),  # Sq.C1
    BitBoard(int('01020408102000', 16)),  # Sq.B1
    BitBoard(int('0102040810204000', 16)),  # Sq.A1

    BitBoard(0),  # Sq.H2
    BitBoard(int('010000', 16)),  # Sq.G2
    BitBoard(int('01020000', 16)),  # Sq.F2
    BitBoard(int('0102040000', 16)),  # Sq.E2
    BitBoard(int('010204080000', 16)),  # Sq.D2
    BitBoard(int('01020408100000', 16)),  # Sq.C2
    BitBoard(int('0102040810200000', 16)),  # Sq.B2
    BitBoard(int('0204081020400000', 16)),  # Sq.A2

    BitBoard(0),  # Sq.H3
    BitBoard(int('01000000', 16)),  # Sq.G3
    BitBoard(int('0102000000', 16)),  # Sq.F3
    BitBoard(int('010204000000', 16)),  # Sq.E3
    BitBoard(int('01020408000000', 16)),  # Sq.D3
    BitBoard(int('0102040810000000', 16)),  # Sq.C3
    BitBoard(int('0204081020000000', 16)),  # Sq.B3
    BitBoard(int('0408102040000000', 16)),  # Sq.A3

    BitBoard(0),  # Sq.H4
    BitBoard(int('0100000000', 16)),  # Sq.G4
    BitBoard(int('010200000000', 16)),  # Sq.F4
    BitBoard(int('01020400000000', 16)),  # Sq.E4
    BitBoard(int('0102040800000000', 16)),  # Sq.D4
    BitBoard(int('0204081000000000', 16)),  # Sq.C4
    BitBoard(int('0408102000000000', 16)),  # Sq.B4
    BitBoard(int('0810204000000000', 16)),  # Sq.A4

    BitBoard(0),  # Sq.H5
    BitBoard(int('010000000000', 16)),  # Sq.G5
    BitBoard(int('01020000000000', 16)),  # Sq.F5
    BitBoard(int('0102040000000000', 16)),  # Sq.E5
    BitBoard(int('0204080000000000', 16)),  # Sq.D5
    BitBoard(int('0408100000000000', 16)),  # Sq.C5
    BitBoard(int('0810200000000000', 16)),  # Sq.B5
    BitBoard(int('1020400000000000', 16)),  # Sq.A5

    BitBoard(0),  # Sq.H6
    BitBoard(int('01000000000000', 16)),  # Sq.G6
    BitBoard(int('0102000000000000', 16)),  # Sq.F6
    BitBoard(int('0204000000000000', 16)),  # Sq.E6
    BitBoard(int('0408000000000000', 16)),  # Sq.D6
    BitBoard(int('0810000000000000', 16)),  # Sq.C6
    BitBoard(int('1020000000000000', 16)),  # Sq.B6
    BitBoard(int('2040000000000000', 16)),  # Sq.A6

    BitBoard(0),  # Sq.H7
    BitBoard(int('0100000000000000', 16)),  # Sq.G7
    BitBoard(int('0200000000000000', 16)),  # Sq.F7
    BitBoard(int('0400000000000000', 16)),  # Sq.E7
    BitBoard(int('0800000000000000', 16)),  # Sq.D7
    BitBoard(int('1000000000000000', 16)),  # Sq.C7
    BitBoard(int('2000000000000000', 16)),  # Sq.B7
    BitBoard(int('4000000000000000', 16)),  # Sq.A7

    BitBoard(0),  # Sq.H8
    BitBoard(0),  # Sq.G8
    BitBoard(0),  # Sq.F8
    BitBoard(0),  # Sq.E8
    BitBoard(0),  # Sq.D8
    BitBoard(0),  # Sq.C8
    BitBoard(0),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

_ATTACK_B_DL = [
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(int('2', 16)),  # Sq.H2
    BitBoard(int('4', 16)),  # Sq.G2
    BitBoard(int('8', 16)),  # Sq.F2
    BitBoard(int('10', 16)),  # Sq.E2
    BitBoard(int('20', 16)),  # Sq.D2
    BitBoard(int('40', 16)),  # Sq.C2
    BitBoard(int('80', 16)),  # Sq.B2
    BitBoard(0),  # Sq.A2

    BitBoard(int('204', 16)),  # Sq.H3
    BitBoard(int('408', 16)),  # Sq.G3
    BitBoard(int('810', 16)),  # Sq.F3
    BitBoard(int('1020', 16)),  # Sq.E3
    BitBoard(int('2040', 16)),  # Sq.D3
    BitBoard(int('4080', 16)),  # Sq.C3
    BitBoard(int('8000', 16)),  # Sq.B3
    BitBoard(0),  # Sq.A3

    BitBoard(int('20408', 16)),  # Sq.H4
    BitBoard(int('40810', 16)),  # Sq.G4
    BitBoard(int('81020', 16)),  # Sq.F4
    BitBoard(int('102040', 16)),  # Sq.E4
    BitBoard(int('204080', 16)),  # Sq.D4
    BitBoard(int('408000', 16)),  # Sq.C4
    BitBoard(int('800000', 16)),  # Sq.B4
    BitBoard(0),  # Sq.A4

    BitBoard(int('2040810', 16)),  # Sq.H5
    BitBoard(int('4081020', 16)),  # Sq.G5
    BitBoard(int('8102040', 16)),  # Sq.F5
    BitBoard(int('10204080', 16)),  # Sq.E5
    BitBoard(int('20408000', 16)),  # Sq.D5
    BitBoard(int('40800000', 16)),  # Sq.C5
    BitBoard(int('80000000', 16)),  # Sq.B5
    BitBoard(0),  # Sq.A5

    BitBoard(int('204081020', 16)),  # Sq.H6
    BitBoard(int('408102040', 16)),  # Sq.G6
    BitBoard(int('810204080', 16)),  # Sq.F6
    BitBoard(int('1020408000', 16)),  # Sq.E6
    BitBoard(int('2040800000', 16)),  # Sq.D6
    BitBoard(int('4080000000', 16)),  # Sq.C6
    BitBoard(int('8000000000', 16)),  # Sq.B6
    BitBoard(0),  # Sq.A6

    BitBoard(int('20408102040', 16)),  # Sq.H7
    BitBoard(int('40810204080', 16)),  # Sq.G7
    BitBoard(int('81020408000', 16)),  # Sq.F7
    BitBoard(int('102040800000', 16)),  # Sq.E7
    BitBoard(int('204080000000', 16)),  # Sq.D7
    BitBoard(int('408000000000', 16)),  # Sq.C7
    BitBoard(int('800000000000', 16)),  # Sq.B7
    BitBoard(0),  # Sq.A7

    BitBoard(int('2040810204080', 16)),  # Sq.H8
    BitBoard(int('4081020408000', 16)),  # Sq.G8
    BitBoard(int('8102040800000', 16)),  # Sq.F8
    BitBoard(int('10204080000000', 16)),  # Sq.E8
    BitBoard(int('20408000000000', 16)),  # Sq.D8
    BitBoard(int('40800000000000', 16)),  # Sq.C8
    BitBoard(int('80000000000000', 16)),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

_ATTACK_B_DR = [
    BitBoard(0),  # Sq.H1
    BitBoard(0),  # Sq.G1
    BitBoard(0),  # Sq.F1
    BitBoard(0),  # Sq.E1
    BitBoard(0),  # Sq.D1
    BitBoard(0),  # Sq.C1
    BitBoard(0),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(0),  # Sq.H2
    BitBoard(int('1', 16)),  # Sq.G2
    BitBoard(int('2', 16)),  # Sq.F2
    BitBoard(int('4', 16)),  # Sq.E2
    BitBoard(int('8', 16)),  # Sq.D2
    BitBoard(int('10', 16)),  # Sq.C2
    BitBoard(int('20', 16)),  # Sq.B2
    BitBoard(int('40', 16)),  # Sq.A2

    BitBoard(0),  # Sq.H3
    BitBoard(int('100', 16)),  # Sq.G3
    BitBoard(int('201', 16)),  # Sq.F3
    BitBoard(int('402', 16)),  # Sq.E3
    BitBoard(int('804', 16)),  # Sq.D3
    BitBoard(int('1008', 16)),  # Sq.C3
    BitBoard(int('2010', 16)),  # Sq.B3
    BitBoard(int('4020', 16)),  # Sq.A3

    BitBoard(0),  # Sq.H4
    BitBoard(int('10000', 16)),  # Sq.G4
    BitBoard(int('20100', 16)),  # Sq.F4
    BitBoard(int('40201', 16)),  # Sq.E4
    BitBoard(int('80402', 16)),  # Sq.D4
    BitBoard(int('100804', 16)),  # Sq.C4
    BitBoard(int('201008', 16)),  # Sq.B4
    BitBoard(int('402010', 16)),  # Sq.A4

    BitBoard(0),  # Sq.H5
    BitBoard(int('1000000', 16)),  # Sq.G5
    BitBoard(int('2010000', 16)),  # Sq.F5
    BitBoard(int('4020100', 16)),  # Sq.E5
    BitBoard(int('8040201', 16)),  # Sq.D5
    BitBoard(int('10080402', 16)),  # Sq.C5
    BitBoard(int('20100804', 16)),  # Sq.B5
    BitBoard(int('40201008', 16)),  # Sq.A5

    BitBoard(0),  # Sq.H6
    BitBoard(int('100000000', 16)),  # Sq.G6
    BitBoard(int('201000000', 16)),  # Sq.F6
    BitBoard(int('402010000', 16)),  # Sq.E6
    BitBoard(int('804020100', 16)),  # Sq.D6
    BitBoard(int('1008040201', 16)),  # Sq.C6
    BitBoard(int('2010080402', 16)),  # Sq.B6
    BitBoard(int('4020100804', 16)),  # Sq.A6

    BitBoard(0),  # Sq.H7
    BitBoard(int('10000000000', 16)),  # Sq.G7
    BitBoard(int('20100000000', 16)),  # Sq.F7
    BitBoard(int('40201000000', 16)),  # Sq.E7
    BitBoard(int('80402010000', 16)),  # Sq.D7
    BitBoard(int('100804020100', 16)),  # Sq.C7
    BitBoard(int('201008040201', 16)),  # Sq.B7
    BitBoard(int('402010080402', 16)),  # Sq.A7

    BitBoard(0),  # Sq.H8
    BitBoard(int('1000000000000', 16)),  # Sq.G8
    BitBoard(int('2010000000000', 16)),  # Sq.F8
    BitBoard(int('4020100000000', 16)),  # Sq.E8
    BitBoard(int('8040201000000', 16)),  # Sq.D8
    BitBoard(int('10080402010000', 16)),  # Sq.C8
    BitBoard(int('20100804020100', 16)),  # Sq.B8
    BitBoard(int('40201008040201', 16)),  # Sq.A8
]

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

_ATTACK_R_L = [
    BitBoard(int('FE', 16)),  # Sq.H1
    BitBoard(int('FC', 16)),  # Sq.G1
    BitBoard(int('F8', 16)),  # Sq.F1
    BitBoard(int('F0', 16)),  # Sq.E1
    BitBoard(int('E0', 16)),  # Sq.D1
    BitBoard(int('C0', 16)),  # Sq.C1
    BitBoard(int('80', 16)),  # Sq.B1
    BitBoard(0),  # Sq.A1

    BitBoard(int('FE00', 16)),  # Sq.H2
    BitBoard(int('FC00', 16)),  # Sq.G2
    BitBoard(int('F800', 16)),  # Sq.F2
    BitBoard(int('F000', 16)),  # Sq.E2
    BitBoard(int('E000', 16)),  # Sq.D2
    BitBoard(int('C000', 16)),  # Sq.C2
    BitBoard(int('8000', 16)),  # Sq.B2
    BitBoard(0),  # Sq.A2

    BitBoard(int('FE0000', 16)),  # Sq.H3
    BitBoard(int('FC0000', 16)),  # Sq.G3
    BitBoard(int('F80000', 16)),  # Sq.F3
    BitBoard(int('F00000', 16)),  # Sq.E3
    BitBoard(int('E00000', 16)),  # Sq.D3
    BitBoard(int('C00000', 16)),  # Sq.C3
    BitBoard(int('800000', 16)),  # Sq.B3
    BitBoard(0),  # Sq.A3

    BitBoard(int('FE000000', 16)),  # Sq.H4
    BitBoard(int('FC000000', 16)),  # Sq.G4
    BitBoard(int('F8000000', 16)),  # Sq.F4
    BitBoard(int('F0000000', 16)),  # Sq.E4
    BitBoard(int('E0000000', 16)),  # Sq.D4
    BitBoard(int('C0000000', 16)),  # Sq.C4
    BitBoard(int('80000000', 16)),  # Sq.B4
    BitBoard(0),  # Sq.A4

    BitBoard(int('FE00000000', 16)),  # Sq.H5
    BitBoard(int('FC00000000', 16)),  # Sq.G5
    BitBoard(int('F800000000', 16)),  # Sq.F5
    BitBoard(int('F000000000', 16)),  # Sq.E5
    BitBoard(int('E000000000', 16)),  # Sq.D5
    BitBoard(int('C000000000', 16)),  # Sq.C5
    BitBoard(int('8000000000', 16)),  # Sq.B5
    BitBoard(0),  # Sq.A5

    BitBoard(int('FE0000000000', 16)),  # Sq.H6
    BitBoard(int('FC0000000000', 16)),  # Sq.G6
    BitBoard(int('F80000000000', 16)),  # Sq.F6
    BitBoard(int('F00000000000', 16)),  # Sq.E6
    BitBoard(int('E00000000000', 16)),  # Sq.D6
    BitBoard(int('C00000000000', 16)),  # Sq.C6
    BitBoard(int('800000000000', 16)),  # Sq.B6
    BitBoard(0),  # Sq.A6

    BitBoard(int('FE000000000000', 16)),  # Sq.H7
    BitBoard(int('FC000000000000', 16)),  # Sq.G7
    BitBoard(int('F8000000000000', 16)),  # Sq.F7
    BitBoard(int('F0000000000000', 16)),  # Sq.E7
    BitBoard(int('E0000000000000', 16)),  # Sq.D7
    BitBoard(int('C0000000000000', 16)),  # Sq.C7
    BitBoard(int('80000000000000', 16)),  # Sq.B7
    BitBoard(0),  # Sq.A7

    BitBoard(int('FE00000000000000', 16)),  # Sq.H8
    BitBoard(int('FC00000000000000', 16)),  # Sq.G8
    BitBoard(int('F800000000000000', 16)),  # Sq.F8
    BitBoard(int('F000000000000000', 16)),  # Sq.E8
    BitBoard(int('E000000000000000', 16)),  # Sq.D8
    BitBoard(int('C000000000000000', 16)),  # Sq.C8
    BitBoard(int('8000000000000000', 16)),  # Sq.B8
    BitBoard(0),  # Sq.A8
]

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
    BitBoard(int('40C0000000000000', 16)),  # Sq.A8
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

PIECE_VALUE = {
    Piece.WP: 100,
    Piece.WN: 300,
    Piece.WB: 300,
    Piece.WR: 500,
    Piece.WQ: 900,
    Piece.WK: 9999,
    Piece.BP: -100,
    Piece.BN: -300,
    Piece.BB: -300,
    Piece.BR: -500,
    Piece.BQ: -900,
    Piece.BK: -9999,
}

# https://chessprogramming.wikispaces.com/Simplified+evaluation+function
_PCSQ_WP = [
     0,    0,   0,   0,   0,   0,   0,   0,
     50,  50,  50,  50,  50,  50,  50,  50,
     10,  10,  20,  30,  30,  20,  10,  10,
     5,    5,  10,  25,  25,  10,   5,   5,
     0,    0,   0,  20,  20,   0,   0,   0,
     5,   -5, -10,   0,   0, -10,  -5,   5,
     5,   10,  10, -20, -20,  10,  10,   5,
     0,    0,   0,   0,   0,   0,   0,   0,
]
_PCSQ_WN = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,   0,   0,   0,   0, -20, -40,
    -30,   0,  10,  15,  15,  10,   0, -30,
    -30,   5,  15,  20,  20,  15,   5, -30,
    -30,   0,  15,  20,  20,  15,   0, -30,
    -30,   5,  10,  15,  15,  10,   5, -30,
    -40, -20,   0,   5,   5,   0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]
_PCSQ_WB = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
_PCSQ_WR = [
     0,    0,   0,   0,   0,   0,   0,   0,
     5,   10,  10,  10,  10,  10,  10,   5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     -5,   0,   0,   0,   0,   0,   0,  -5,
     0,    0,   0,   5,   5,   0,   0,   0,
]
_PCSQ_WQ = [
    -20, -10, -10,  -5,  -5, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,   5,   5,   5,   0, -10,
    -5,    0,   5,   5,   5,   5,   0,  -5,
    0,     0,   5,   5,   5,   5,   0,  -5,
    -10,   5,   5,   5,   5,   5,   0, -10,
    -10,   0,   5,   0,   0,   0,   0, -10,
    -20, -10, -10,  -5,  -5, -10, -10, -20,
]
_PCSQ_WK = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20,   20,   0,   0,   0,   0,  20,  20,
    20,   30,  10,   0,   0,  10,  30,  20,
]

_PCSQ_BP = [0] * 64
_PCSQ_BN = [0] * 64
_PCSQ_BB = [0] * 64
_PCSQ_BR = [0] * 64
_PCSQ_BQ = [0] * 64
_PCSQ_BK = [0] * 64

for i in range(0, 64):
    column = i % 8
    row = int((i - column) / 8)

    _PCSQ_BP[i] = -_PCSQ_WP[8 * (7 - row) + column]
    _PCSQ_BN[i] = -_PCSQ_WN[8 * (7 - row) + column]
    _PCSQ_BB[i] = -_PCSQ_WB[8 * (7 - row) + column]
    _PCSQ_BR[i] = -_PCSQ_WR[8 * (7 - row) + column]
    _PCSQ_BQ[i] = -_PCSQ_WQ[8 * (7 - row) + column]
    _PCSQ_BK[i] = -_PCSQ_WK[8 * (7 - row) + column]

PCSQ_VALUE = {
    Piece.WP: _PCSQ_WP,
    Piece.WN: _PCSQ_WN,
    Piece.WB: _PCSQ_WB,
    Piece.WR: _PCSQ_WR,
    Piece.WQ: _PCSQ_WQ,
    Piece.WK: _PCSQ_WK,
    Piece.BP: _PCSQ_BP,
    Piece.BN: _PCSQ_BN,
    Piece.BB: _PCSQ_BB,
    Piece.BR: _PCSQ_BR,
    Piece.BQ: _PCSQ_BQ,
    Piece.BK: _PCSQ_BK,
}
