#!/usr/bin/env python3
"""
This file defines unit tests for the Board class.
"""
import unittest
from Board import Board
from Color import Color
from Move import Move
from Piece import Piece
from Sq import Sq


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

    def test_fen(self):
        """
        Tests the fen() function of the Board class
        """
        self._test_get_fen()
        self._test_set_fen()

    def _test_get_fen(self):
        """
        Tests the _get_fen() function of the Board class
        """
        board = Board()
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

        board.bitboards[Piece.WP][Sq.E4] = 1
        board.bitboards[Piece.WP][Sq.E2] = 0
        board.turn = Color.BLACK
        board.wk_castling = False
        board.bk_castling = False
        board.ep_square = Sq.A8
        board.half_move_clock = 13
        board.full_move_count = 20
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b Qq a8 13 20')

    def _test_set_fen(self):
        """
        Tests the _set_fen() function of the Board class
        """
        board = Board()
        board.fen('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        self.assertEqual(board.bitboards[Piece.WP][Sq.E2], 0)
        self.assertEqual(board.bitboards[Piece.WP][Sq.E4], 1)
        self.assertEqual(board.turn, Color.BLACK)
        self.assertEqual(board.wk_castling, True)
        self.assertEqual(board.wq_castling, True)
        self.assertEqual(board.bk_castling, True)
        self.assertEqual(board.bq_castling, True)
        self.assertEqual(board.ep_square, Sq.E3)
        self.assertEqual(board.half_move_clock, 0)
        self.assertEqual(board.full_move_count, 1)

        board.fen('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w - c6 1 2')
        self.assertEqual(board.bitboards[Piece.BP][Sq.C7], 0)
        self.assertEqual(board.bitboards[Piece.BP][Sq.C5], 1)
        self.assertEqual(board.turn, Color.WHITE)
        self.assertEqual(board.wk_castling, False)
        self.assertEqual(board.wq_castling, False)
        self.assertEqual(board.bk_castling, False)
        self.assertEqual(board.bq_castling, False)
        self.assertEqual(board.ep_square, Sq.C6)
        self.assertEqual(board.half_move_clock, 1)
        self.assertEqual(board.full_move_count, 2)

    def test_make_move(self):
        """
        Tests the make_move() function of the Board class
        """
        board = Board()
        move = Move(Sq.E2, Sq.E4, 0)
        board.make_move(move)
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')

