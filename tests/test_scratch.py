"""
This file is for debugging.
"""
import pytest


from clarity.BitBoard import BitBoard
from clarity.Board import Board
from clarity.Color import Color
from clarity import constants as const
from clarity.Direction import Direction
from clarity.Move import Move
from clarity.MoveType import MoveType
from clarity.Piece import Piece
from clarity.recursion import divide, perft, negamax, _negamax_recur
from clarity.Sq import Sq


@pytest.mark.scratch
def test_scratch():
    pass
