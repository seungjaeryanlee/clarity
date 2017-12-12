r"""
This file defines the constants used in Clarity.
"""
from BitBoard import BitBoard
from Direction import Direction
from MoveType import MoveType
from Piece import Piece
from Sq import Sq


# Move bitboards for pawns
_MOVE_WP_QUIET = [BitBoard(0)] * 64
_MOVE_WP_DOUBLE = [BitBoard(0)] * 64

MOVE_WP = {
    MoveType.QUIET: _MOVE_WP_QUIET,
    MoveType.DOUBLE: _MOVE_WP_DOUBLE,
}

_MOVE_BP_QUIET = [BitBoard(0)] * 64
_MOVE_BP_DOUBLE = [BitBoard(0)] * 64

MOVE_BP = {
    MoveType.QUIET: _MOVE_BP_QUIET,
    MoveType.DOUBLE: _MOVE_BP_DOUBLE,
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
_ATTACK_B_UR = [BitBoard(0)] * 64
_ATTACK_B_DL = [BitBoard(0)] * 64
_ATTACK_B_DR = [BitBoard(0)] * 64

_ATTACK_B = {
    Direction.UL: _ATTACK_B_UL,
    Direction.UR: _ATTACK_B_UR,
    Direction.DL: _ATTACK_B_DL,
    Direction.DR: _ATTACK_B_DR,
}

_ATTACK_R_U = [BitBoard(0)] * 64
_ATTACK_R_D = [BitBoard(0)] * 64
_ATTACK_R_L = [BitBoard(0)] * 64
_ATTACK_R_R = [BitBoard(0)] * 64

_ATTACK_R = {
    Direction.U: _ATTACK_R_U,
    Direction.D: _ATTACK_R_D,
    Direction.L: _ATTACK_R_L,
    Direction.R: _ATTACK_R_R,
}

_ATTACK_K = [BitBoard(0)] * 64

# TODO create Direction enum for bishop, rook, and queen
ATTACK = {
    Piece.WP: _ATTACK_WP,
    Piece.WN: _ATTACK_N,
    Piece.WB: _ATTACK_B,
    Piece.WR: _ATTACK_R,
    # Piece.WQ should not be needed since we can use N and R
    Piece.WK: _ATTACK_K,
    Piece.BP: _ATTACK_BP,
    Piece.BN: _ATTACK_N,
    Piece.BB: _ATTACK_B,
    Piece.BR: _ATTACK_R,
    # Piece.BQ should not be needed since we can use N and R
    Piece.BK: _ATTACK_K,
}
