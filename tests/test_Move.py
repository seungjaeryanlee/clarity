#!/usr/bin/env python3
"""
This file defines unit tests for the Move class.
"""
import unittest
from Move import Move
from MoveType import MoveType
from Sq import Sq


class TestMoveClass(unittest.TestCase):
    """
    This class tests the Move class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the Move class.
        """
        move = Move(Sq.E2, Sq.E4, MoveType.CAPTURE)
        expected = int('{:06b}'.format(Sq.E2) + '{:06b}'.format(Sq.E4) + '{:04b}'.format(1), 2)
        self.assertEqual(move.num, expected)

        move = Move(Sq.E7, Sq.E6, MoveType.QUIET)
        expected = int('{:06b}'.format(Sq.E7) + '{:06b}'.format(Sq.E6) + '{:04b}'.format(0), 2)
        self.assertEqual(move.num, expected)

    def test_init_sq(self):
        """
        Tests the init_sq() function of the Move class.
        """
        move = Move(Sq.G1, Sq.F3, MoveType.QUIET)
        self.assertEqual(move.init_sq(), Sq.G1)

        move = Move(Sq.B7, Sq.C6, MoveType.QUIET)
        self.assertEqual(move.init_sq(), Sq.B7)

    def test_dest_sq(self):
        """
        Tests the dest_sq() function of the Move class.
        """
        move = Move(Sq.G1, Sq.F3, MoveType.QUIET)
        self.assertEqual(move.dest_sq(), Sq.F3)

        move = Move(Sq.B7, Sq.C6, MoveType.QUIET)
        self.assertEqual(move.dest_sq(), Sq.C6)

    def test_move_type(self):
        """
        Tests the move_type() function of the Move class.
        """
        move = Move(Sq.D2, Sq.D3, MoveType.QUIET)
        self.assertEqual(move.move_type(), MoveType.QUIET)

        move = Move(Sq.E2, Sq.E4, MoveType.CAPTURE)
        self.assertEqual(move.move_type(), MoveType.CAPTURE)

        move = Move(Sq.E1, Sq.G1, MoveType.K_CASTLE)
        self.assertEqual(move.move_type(), MoveType.K_CASTLE)

        move = Move(Sq.E1, Sq.C1, MoveType.Q_CASTLE)
        self.assertEqual(move.move_type(), MoveType.Q_CASTLE)
