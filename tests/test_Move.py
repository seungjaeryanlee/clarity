#!/usr/bin/env python3
"""
This file defines unit tests for the Move class.
"""
import unittest
from clarity.Move import Move
from clarity.MoveType import MoveType
from clarity.Sq import Sq


class TestMoveClass(unittest.TestCase):
    """
    This class tests the Move class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the Move class.
        """
        move = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        expected = int('{:06b}'.format(Sq.E2) + '{:06b}'.format(Sq.E4) + '{:04b}'.format(MoveType.DOUBLE), 2)
        self.assertEqual(move.num, expected)

        move = Move(Sq.E7, Sq.E6, MoveType.QUIET)
        expected = int('{:06b}'.format(Sq.E7) + '{:06b}'.format(Sq.E6) + '{:04b}'.format(MoveType.QUIET), 2)
        self.assertEqual(move.num, expected)

    def test_lt(self):
        """
        Tests the lt() function of the Move class.
        """
        # Sq.E2 < Sq.E7
        move1 = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        move2 = Move(Sq.E7, Sq.E6, MoveType.QUIET)
        self.assertLess(move1, move2)
        self.assertListEqual(sorted([move1, move2]), [move1, move2])
        self.assertListEqual(sorted([move2, move1]), [move1, move2])

        # Sq.H4 < Sq.F4
        move1 = Move(Sq.G2, Sq.H4, MoveType.QUIET)
        move2 = Move(Sq.G2, Sq.F4, MoveType.QUIET)
        self.assertLess(move1, move2)
        self.assertListEqual(sorted([move1, move2]), [move1, move2])
        self.assertListEqual(sorted([move2, move1]), [move1, move2])

        # MoveType.N_PROMO < MoveType.Q_PROMO
        move1 = Move(Sq.G2, Sq.H4, MoveType.N_PROMO)
        move2 = Move(Sq.G2, Sq.F4, MoveType.Q_PROMO)
        self.assertLess(move1, move2)
        self.assertListEqual(sorted([move1, move2]), [move1, move2])
        self.assertListEqual(sorted([move2, move1]), [move1, move2])

    def test_eq(self):
        """
        Tests the eq() function of the Move class.
        """
        move1 = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        move2 = Move(Sq.E7, Sq.E6, MoveType.QUIET)
        self.assertNotEqual(move1, move2)

        move1 = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        move2 = Move(Sq.E2, Sq.E3, MoveType.QUIET)
        self.assertNotEqual(move1, move2)

        move1 = Move(Sq.G7, Sq.G8, MoveType.N_PROMO)
        move2 = Move(Sq.G7, Sq.G8, MoveType.Q_PROMO)
        self.assertNotEqual(move1, move2)

        move1 = Move(Sq.D2, Sq.D4, MoveType.DOUBLE)
        move2 = Move(Sq.D2, Sq.D4, MoveType.DOUBLE)
        move3 = move1
        self.assertEqual(move1, move3)
        self.assertEqual(move1, move2)

    def test_repr(self):
        """
        Tests the repr() function of the Move class.
        """
        move = Move(Sq.E7, Sq.E8, MoveType.N_PROMO)
        self.assertEqual(repr(move), 'Sq.E7 Sq.E8 MoveType.N_PROMO')

        move = Move(Sq.A2, Sq.A3, MoveType.QUIET)
        self.assertEqual(repr(move), 'Sq.A2 Sq.A3 MoveType.QUIET')

    def test_str(self):
        """
        Tests the str() function of the Move class.
        """
        move = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        self.assertEqual(str(move), 'Sq.E2 Sq.E4 MoveType.DOUBLE')

        move = Move(Sq.D2, Sq.D3, MoveType.QUIET)
        self.assertEqual(str(move), 'Sq.D2 Sq.D3 MoveType.QUIET')

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
