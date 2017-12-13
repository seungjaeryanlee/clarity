r"""
This file defines the constants used in Clarity.
"""
from BitBoard import BitBoard
from Direction import Direction
from Piece import Piece
from Sq import Sq


# Move bitboards for pawns
_MOVE_WP = [BitBoard(0)] * 64
_MOVE_WP[Sq.A2] = BitBoard(8388608)
_MOVE_WP[Sq.B2] = BitBoard(4194304)
_MOVE_WP[Sq.C2] = BitBoard(2097152)
_MOVE_WP[Sq.D2] = BitBoard(1048576)
_MOVE_WP[Sq.E2] = BitBoard(524288)
_MOVE_WP[Sq.F2] = BitBoard(262144)
_MOVE_WP[Sq.G2] = BitBoard(131072)
_MOVE_WP[Sq.H2] = BitBoard(65536)

_MOVE_BP = [BitBoard(0)] * 64
_MOVE_BP[Sq.A7] = BitBoard(int('80000000000000', 16))
_MOVE_BP[Sq.B7] = BitBoard(int('40000000000000', 16))
_MOVE_BP[Sq.C7] = BitBoard(int('20000000000000', 16))
_MOVE_BP[Sq.D7] = BitBoard(int('10000000000000', 16))
_MOVE_BP[Sq.E7] = BitBoard(int('8000000000000', 16))
_MOVE_BP[Sq.F7] = BitBoard(int('4000000000000', 16))
_MOVE_BP[Sq.G7] = BitBoard(int('2000000000000', 16))
_MOVE_BP[Sq.H7] = BitBoard(int('1000000000000', 16))

_DOUBLE_WP = [BitBoard(0)] * 64
_DOUBLE_WP[Sq.A2] = BitBoard(int('80000000', 16))
_DOUBLE_WP[Sq.B2] = BitBoard(int('40000000', 16))
_DOUBLE_WP[Sq.C2] = BitBoard(int('20000000', 16))
_DOUBLE_WP[Sq.D2] = BitBoard(int('10000000', 16))
_DOUBLE_WP[Sq.E2] = BitBoard(int('8000000', 16))
_DOUBLE_WP[Sq.F2] = BitBoard(int('4000000', 16))
_DOUBLE_WP[Sq.G2] = BitBoard(int('2000000', 16))
_DOUBLE_WP[Sq.H2] = BitBoard(int('1000000', 16))

_DOUBLE_BP = [BitBoard(0)] * 64
_DOUBLE_BP[Sq.A7] = BitBoard(int('800000000000', 16))
_DOUBLE_BP[Sq.B7] = BitBoard(int('400000000000', 16))
_DOUBLE_BP[Sq.C7] = BitBoard(int('200000000000', 16))
_DOUBLE_BP[Sq.D7] = BitBoard(int('100000000000', 16))
_DOUBLE_BP[Sq.E7] = BitBoard(int('80000000000', 16))
_DOUBLE_BP[Sq.F7] = BitBoard(int('40000000000', 16))
_DOUBLE_BP[Sq.G7] = BitBoard(int('20000000000', 16))
_DOUBLE_BP[Sq.H7] = BitBoard(int('10000000000', 16))

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
_ATTACK_WP = [BitBoard(0)] * 64
_ATTACK_BP = [BitBoard(0)] * 64

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

_ATTACK_R_U = [BitBoard(0)] * 64
_ATTACK_R_U[Sq.H1] = BitBoard(int('00000001'
                                  '00000001'
                                  '00000001'
                                  '00000001'
                                  '00000001'
                                  '00000001'
                                  '00000001'
                                  '00000000', 2))
_ATTACK_R_U[Sq.G1] = BitBoard(int('00000010'
                                  '00000010'
                                  '00000010'
                                  '00000010'
                                  '00000010'
                                  '00000010'
                                  '00000010'
                                  '00000000', 2))
_ATTACK_R_D = [BitBoard(0)] * 64
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
_ATTACK_R_R = [BitBoard(0)] * 64
_ATTACK_R_R[Sq.G1] = BitBoard(int('00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000000'
                                  '00000001', 2))

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

_ATTACK_K = [BitBoard(0)] * 64
_ATTACK_K[Sq.H1] = BitBoard(int('00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '00000000'
                                '00000011'
                                '00000010', 2))
_ATTACK_K[Sq.D5] = BitBoard(int('00000000'
                                '00000000'
                                '00111000'
                                '00101000'
                                '00111000'
                                '00000000'
                                '00000000'
                                '00000000', 2))

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
