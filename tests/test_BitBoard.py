#!/usr/bin/env python3
"""
This file defines unit tests for the BitBoard class.
"""
import unittest
from BitBoard import BitBoard


class TestBitBoardClass(unittest.TestCase):
    """
    This class tests the BitBoard class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the BitBoard class.
        """
        bb = BitBoard(1)
        self.assertEqual(bb.num, 1)

    def test_getitem(self):
        """
        Tests the __getitem__() function of the BitBoard class.
        """
        bb = BitBoard(int('01000010', 2))
        for i in range(64):
            if i == 1 or i == 6:
                self.assertEqual(bb[i], 1)
            else:
                self.assertEqual(bb[i], 0)

    def test_setitem(self):
        """
        Tests the __setitem__() function of the BitBoard class.
        """
        bb = BitBoard(int('00100100', 2))
        bb[0] = 1
        self.assertEqual(bb.__str__(), '00000000\n00000000\n00000000\n00000000\n00000000\n00000000\n00000000\n00100101')
        bb[63] = 1
        self.assertEqual(bb.__str__(), '10000000\n00000000\n00000000\n00000000\n00000000\n00000000\n00000000\n00100101')
        bb[2] = 0
        self.assertEqual(bb.__str__(), '10000000\n00000000\n00000000\n00000000\n00000000\n00000000\n00000000\n00100001')

    def test_str(self):
        """
        Tests the __str__() function of the BitBoard class.
        """
        bb = BitBoard(int('1111111100000000', 2))
        self.assertEqual(bb.__str__(), '00000000\n00000000\n00000000\n00000000\n00000000\n00000000\n11111111\n00000000')
