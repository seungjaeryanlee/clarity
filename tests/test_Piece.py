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
