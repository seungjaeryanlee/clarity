#!/usr/bin/env python3
"""
This file defines unit tests for the Board class.
"""
import unittest
from Board import Board
from Color import Color
from Piece import Piece


class TestBoardClass(unittest.TestCase):
    """
    This class tests the Board class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the Board class.
        """
        board = Board()
        self.assertEqual(board.bitboards[Piece.WP].num,
                         int('0000000000000000000000000000000000000000000000001111111100000000', 2))
        self.assertEqual(board.bitboards[Piece.WN].num,
                         int('0000000000000000000000000000000000000000000000000000000001000010', 2))
        self.assertEqual(board.bitboards[Piece.WB].num,
                         int('0000000000000000000000000000000000000000000000000000000000100100', 2))
        self.assertEqual(board.bitboards[Piece.WR].num,
                         int('0000000000000000000000000000000000000000000000000000000010000001', 2))
        self.assertEqual(board.bitboards[Piece.WQ].num,
                         int('0000000000000000000000000000000000000000000000000000000000010000', 2))
        self.assertEqual(board.bitboards[Piece.WK].num,
                         int('0000000000000000000000000000000000000000000000000000000000001000', 2))

        self.assertEqual(board.bitboards[Piece.BP].num,
                         int('0000000011111111000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BN].num,
                         int('0100001000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BB].num,
                         int('0010010000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BR].num,
                         int('1000000100000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BQ].num,
                         int('0001000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BK].num,
                         int('0000100000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.turn, Color.WHITE)
        self.assertEqual(board.ep_square, -1)
        self.assertEqual(board.wk_castling, True)
        self.assertEqual(board.wq_castling, True)
        self.assertEqual(board.bk_castling, True)
        self.assertEqual(board.bq_castling, True)
        self.assertEqual(board.half_move_clock, 0)
        self.assertEqual(board.full_move_count, 1)