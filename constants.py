r"""
This file defines the constants used in Clarity.
"""
from BitBoard import BitBoard
from Piece import Piece


# Attack bitboards
# TODO fill data
ATTACK_WP = [BitBoard(0)] * 64
ATTACK_BP = [BitBoard(0)] * 64

ATTACK_N_BN = [BitBoard(0)] * 64

ATTACK_B_UL = [BitBoard(0)] * 64
ATTACK_B_UR = [BitBoard(0)] * 64
ATTACK_B_DL = [BitBoard(0)] * 64
ATTACK_B_DR = [BitBoard(0)] * 64

ATTACK_R_U = [BitBoard(0)] * 64
ATTACK_R_D = [BitBoard(0)] * 64
ATTACK_R_L = [BitBoard(0)] * 64
ATTACK_R_R = [BitBoard(0)] * 64

ATTACK_K = [BitBoard(0)] * 64

# TODO create Direction enum for bishop, rook, and queen
ATTACK = {
    Piece.WP: ATTACK_WP,
    Piece.WN: ATTACK_N_BN,
    Piece.WB: [ATTACK_B_UL, ATTACK_B_UR, ATTACK_B_DL, ATTACK_B_DR],
    Piece.WR: [ATTACK_R_U, ATTACK_R_D, ATTACK_R_L,  ATTACK_R_R],
    Piece.WK: ATTACK_K,
    Piece.BP: ATTACK_BP,
    Piece.BN: ATTACK_N_BN,
    Piece.BB: [ATTACK_B_UL, ATTACK_B_UR, ATTACK_B_DL, ATTACK_B_DR],
    Piece.BR: [ATTACK_R_U, ATTACK_R_D, ATTACK_R_L, ATTACK_R_R],
    Piece.BK: ATTACK_K,
}
