#!/usr/bin/env python3
"""
This file defines unit tests for the Sq enum.
"""
import unittest
from clarity.Sq import Sq


class TestColorEnum(unittest.TestCase):
    """
    This class tests the Sq enum.
    """

    def test_filerank_to_sq(self):
        """
        Tests the filerank_to_sq() function of the Sq enum.
        """
        self.assertEqual(Sq.filerank_to_sq('e1'), Sq.E1)
        self.assertEqual(Sq.filerank_to_sq('a2'), Sq.A2)
        self.assertEqual(Sq.filerank_to_sq('f3'), Sq.F3)
        self.assertEqual(Sq.filerank_to_sq('d4'), Sq.D4)

    def test_sq_to_filerank(self):
        """
        Tests the sq_to_filerank() function of the Sq enum.
        """
        self.assertEqual(Sq.sq_to_filerank(Sq.B5), 'b5')
        self.assertEqual(Sq.sq_to_filerank(Sq.C6), 'c6')
        self.assertEqual(Sq.sq_to_filerank(Sq.H7), 'h7')
        self.assertEqual(Sq.sq_to_filerank(Sq.G8), 'g8')
