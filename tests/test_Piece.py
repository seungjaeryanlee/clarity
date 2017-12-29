#!/usr/bin/env python3
"""
This file defines unit tests for the Piece enum.
"""
from clarity.Color import Color
from clarity.Piece import Piece


class TestPieceEnum:
    """
    This class tests the Piece enum.
    """

    def test_color(self):
        """
        Tests the color() function of the Piece enum.
        """
        assert Piece.color(Piece.WP) == Color.WHITE
        assert Piece.color(Piece.WN) == Color.WHITE
        assert Piece.color(Piece.WB) == Color.WHITE
        assert Piece.color(Piece.WR) == Color.WHITE
        assert Piece.color(Piece.WQ) == Color.WHITE
        assert Piece.color(Piece.WK) == Color.WHITE
        assert Piece.color(Piece.BP) == Color.BLACK
        assert Piece.color(Piece.BN) == Color.BLACK
        assert Piece.color(Piece.BB) == Color.BLACK
        assert Piece.color(Piece.BR) == Color.BLACK
        assert Piece.color(Piece.BQ) == Color.BLACK
        assert Piece.color(Piece.BK) == Color.BLACK

    def test_to_char(self):
        """
        Tests the to_char() function of the Piece enum.
        """
        assert Piece.to_char(Piece.WP) == 'P'
        assert Piece.to_char(Piece.WN) == 'N'
        assert Piece.to_char(Piece.WB) == 'B'
        assert Piece.to_char(Piece.WR) == 'R'
        assert Piece.to_char(Piece.WQ) == 'Q'
        assert Piece.to_char(Piece.WK) == 'K'
        assert Piece.to_char(Piece.BP) == 'p'
        assert Piece.to_char(Piece.BN) == 'n'
        assert Piece.to_char(Piece.BB) == 'b'
        assert Piece.to_char(Piece.BR) == 'r'
        assert Piece.to_char(Piece.BQ) == 'q'
        assert Piece.to_char(Piece.BK) == 'k'

    def test_from_char(self):
        """
        Tests the from_char() function of the Piece enum.
        """
        assert Piece.from_char('P') == Piece.WP
        assert Piece.from_char('N') == Piece.WN
        assert Piece.from_char('B') == Piece.WB
        assert Piece.from_char('R') == Piece.WR
        assert Piece.from_char('Q') == Piece.WQ
        assert Piece.from_char('K') == Piece.WK
        assert Piece.from_char('p') == Piece.BP
        assert Piece.from_char('n') == Piece.BN
        assert Piece.from_char('b') == Piece.BB
        assert Piece.from_char('r') == Piece.BR
        assert Piece.from_char('q') == Piece.BQ
        assert Piece.from_char('k') == Piece.BK
