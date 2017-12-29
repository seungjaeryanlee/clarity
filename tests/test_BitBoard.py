#!/usr/bin/env python3
"""
This file defines unit tests for the BitBoard class.
"""
from clarity.BitBoard import BitBoard


class TestBitBoardClass:
    """
    This class tests the BitBoard class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the BitBoard class.
        """
        bb = BitBoard(1)
        assert bb.num == 1

    def test_getitem(self):
        """
        Tests the __getitem__() function of the BitBoard class.
        """
        bb = BitBoard(int('01000010', 2))
        for i in range(64):
            if i == 1 or i == 6:
                assert bb[i] == 1
            else:
                assert bb[i] == 0

    def test_setitem(self):
        """
        Tests the __setitem__() function of the BitBoard class.
        """
        bb = BitBoard(int('00100100', 2))
        bb[0] = 1
        assert bb.__str__() == ('00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00100101')
        bb[63] = 1
        assert bb.__str__() == ('10000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00100101')
        bb[2] = 0
        assert bb.__str__() == ('10000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00100001')

    def test_str(self):
        """
        Tests the __str__() function of the BitBoard class.
        """
        bb = BitBoard(int('1111111100000000', 2))
        assert bb.__str__() == ('00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '11111111\n'
                                '00000000')

    def test_and(self):
        """
        Tests the __and__() function of the BitBoard class.
        """
        bb1 = BitBoard(int('11011001', 2))
        bb2 = BitBoard(int('10101001', 2))
        bb = bb1 & bb2
        assert bb.__str__() == ('00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '10001001')

    def test_or(self):
        """
        Tests the __or__() function of the BitBoard class.
        """
        bb1 = BitBoard(int('01000010', 2))
        bb2 = BitBoard(int('10000001', 2))
        bb = bb1 | bb2
        assert bb.__str__() == ('00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '00000000\n'
                                '11000011')

    def test_invert(self):
        """
        Tests the __or__() function of the BitBoard class.
        """
        bb = ~BitBoard(int('1111111111111111000000000000000000011000100001001110011110111101', 2))
        assert bb.__str__() == ('00000000\n'
                                '00000000\n'
                                '11111111\n'
                                '11111111\n'
                                '11100111\n'
                                '01111011\n'
                                '00011000\n'
                                '01000010')

    def test_eq(self):
        """
        Tests the __eq__() function of the BitBoard class.
        """
        bb1 = BitBoard(0)
        bb2 = BitBoard(0)
        assert bb1 == bb2
        assert bb1 == bb1

        bb1 = BitBoard(100)
        bb2 = BitBoard(100)
        assert bb1 == bb2
        assert bb1 == bb1

    def test_indices(self):
        """
        Tests the indices() function of the BitBoard class.
        """
        bit_str = '1110010101'
        bb = BitBoard(int(bit_str, 2))
        indices = bb.indices()
        assert 0 in indices
        assert 2 in indices
        assert 4 in indices
        assert 7 in indices
        assert 8 in indices
        assert 9 in indices
