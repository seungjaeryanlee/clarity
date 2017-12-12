r"""
This file defines the constants used in Clarity.
"""
from BitBoard import BitBoard
from Direction import Direction
from Piece import Piece


# Attack bitboards
# TODO fill data
ATTACK_WP = [BitBoard(0)] * 64
ATTACK_BP = [BitBoard(0)] * 64

ATTACK_N = [BitBoard(0)] * 64

ATTACK_B_UL = [BitBoard(0)] * 64
ATTACK_B_UR = [BitBoard(0)] * 64
ATTACK_B_DL = [BitBoard(0)] * 64
ATTACK_B_DR = [BitBoard(0)] * 64

ATTACK_B = {
    Direction.UL: ATTACK_B_UL,
    Direction.UR: ATTACK_B_UR,
    Direction.DL: ATTACK_B_DL,
    Direction.DR: ATTACK_B_DR,
}

ATTACK_R_U = [BitBoard(0)] * 64
ATTACK_R_D = [BitBoard(0)] * 64
ATTACK_R_L = [BitBoard(0)] * 64
ATTACK_R_R = [BitBoard(0)] * 64

ATTACK_R = {
    Direction.U: ATTACK_R_U,
    Direction.D: ATTACK_R_D,
    Direction.L: ATTACK_R_L,
    Direction.R: ATTACK_R_R,
}

ATTACK_K = [BitBoard(0)] * 64

# TODO create Direction enum for bishop, rook, and queen
ATTACK = {
    Piece.WP: ATTACK_WP,
    Piece.WN: ATTACK_N,
    Piece.WB: ATTACK_B,
    Piece.WR: ATTACK_R,
    # Piece.WQ should not be needed since we can use N and R
    Piece.WK: ATTACK_K,
    Piece.BP: ATTACK_BP,
    Piece.BN: ATTACK_N,
    Piece.BB: ATTACK_B,
    Piece.BR: ATTACK_R,
    # Piece.BQ should not be needed since we can use N and R
    Piece.BK: ATTACK_K,
}
