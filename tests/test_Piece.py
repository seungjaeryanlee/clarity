#!/usr/bin/env python3
"""
This file defines unit tests for the Piece enum.
"""
import unittest
from Color import Color
from Piece import Piece


class TestPieceEnum(unittest.TestCase):
    """
    This class tests the Piece enum.
    """

    def test_color(self):
        """
        Tests the color() function of the Piece enum.
        """
        self.assertEqual(Piece.color(Piece.WP), Color.WHITE)
        self.assertEqual(Piece.color(Piece.WN), Color.WHITE)
        self.assertEqual(Piece.color(Piece.WB), Color.WHITE)
        self.assertEqual(Piece.color(Piece.WR), Color.WHITE)
        self.assertEqual(Piece.color(Piece.WQ), Color.WHITE)
        self.assertEqual(Piece.color(Piece.WK), Color.WHITE)
        self.assertEqual(Piece.color(Piece.BP), Color.BLACK)
        self.assertEqual(Piece.color(Piece.BN), Color.BLACK)
        self.assertEqual(Piece.color(Piece.BB), Color.BLACK)
        self.assertEqual(Piece.color(Piece.BR), Color.BLACK)
        self.assertEqual(Piece.color(Piece.BQ), Color.BLACK)
        self.assertEqual(Piece.color(Piece.BK), Color.BLACK)

    def test_to_char(self):
        """
        Tests the to_char() function of the Piece enum.
        """

        self.assertEqual(Piece.to_char(Piece.WP), 'P')
        self.assertEqual(Piece.to_char(Piece.WN), 'N')
        self.assertEqual(Piece.to_char(Piece.WB), 'B')
        self.assertEqual(Piece.to_char(Piece.WR), 'R')
        self.assertEqual(Piece.to_char(Piece.WQ), 'Q')
        self.assertEqual(Piece.to_char(Piece.WK), 'K')
        self.assertEqual(Piece.to_char(Piece.BP), 'p')
        self.assertEqual(Piece.to_char(Piece.BN), 'n')
        self.assertEqual(Piece.to_char(Piece.BB), 'b')
        self.assertEqual(Piece.to_char(Piece.BR), 'r')
        self.assertEqual(Piece.to_char(Piece.BQ), 'q')
        self.assertEqual(Piece.to_char(Piece.BK), 'k')
