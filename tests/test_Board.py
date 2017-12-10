#!/usr/bin/env python3
"""
This file defines unit tests for the Board class.
"""
import unittest
from Board import Board


class TestBoardClass(unittest.TestCase):
    """
    This class tests the Board class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the Board class.
        """
        board = Board()
        self.assertEqual(board.wp.board, int('0000000000000000000000000000000000000000000000001111111100000000', 2))
        self.assertEqual(board.wn.board, int('0000000000000000000000000000000000000000000000000000000001000010', 2))
        self.assertEqual(board.wb.board, int('0000000000000000000000000000000000000000000000000000000000100100', 2))
        self.assertEqual(board.wr.board, int('0000000000000000000000000000000000000000000000000000000010000001', 2))
        self.assertEqual(board.wq.board, int('0000000000000000000000000000000000000000000000000000000000010000', 2))
        self.assertEqual(board.wk.board, int('0000000000000000000000000000000000000000000000000000000000001000', 2))

        self.assertEqual(board.bp.board, int('0000000011111111000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bn.board, int('0100001000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bb.board, int('0010010000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.br.board, int('1000000100000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bq.board, int('0001000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bk.board, int('0000100000000000000000000000000000000000000000000000000000000000', 2))
