#!/usr/bin/env python3
"""
This file defines the BitBoard class.
"""
import numpy as np
import textwrap


# used in BitBoard.indices()
EIGHT_ONES = np.uint64(0xFF)
UINT64_PADDING = [np.uint64(0), np.uint64(8), np.uint64(16), np.uint64(24),
                  np.uint64(32), np.uint64(40), np.uint64(48), np.uint64(56)]
UINT64_ONE = np.uint64(1)

# Added lookup table for fast BitBoard.indices()
row_to_indices = [
    [],  # 0: 0
    [0],  # 1: 1
    [1],  # 2: 10
    [0, 1],  # 3: 11
    [2],  # 4: 100
    [0, 2],  # 5: 101
    [1, 2],  # 6: 110
    [0, 1, 2],  # 7: 111
    [3],  # 8: 1000
    [0, 3],  # 9: 1001
    [1, 3],  # 10: 1010
    [0, 1, 3],  # 11: 1011
    [2, 3],  # 12: 1100
    [0, 2, 3],  # 13: 1101
    [1, 2, 3],  # 14: 1110
    [0, 1, 2, 3],  # 15: 1111
    [4],  # 16: 10000
    [0, 4],  # 17: 10001
    [1, 4],  # 18: 10010
    [0, 1, 4],  # 19: 10011
    [2, 4],  # 20: 10100
    [0, 2, 4],  # 21: 10101
    [1, 2, 4],  # 22: 10110
    [0, 1, 2, 4],  # 23: 10111
    [3, 4],  # 24: 11000
    [0, 3, 4],  # 25: 11001
    [1, 3, 4],  # 26: 11010
    [0, 1, 3, 4],  # 27: 11011
    [2, 3, 4],  # 28: 11100
    [0, 2, 3, 4],  # 29: 11101
    [1, 2, 3, 4],  # 30: 11110
    [0, 1, 2, 3, 4],  # 31: 11111
    [5],  # 32: 100000
    [0, 5],  # 33: 100001
    [1, 5],  # 34: 100010
    [0, 1, 5],  # 35: 100011
    [2, 5],  # 36: 100100
    [0, 2, 5],  # 37: 100101
    [1, 2, 5],  # 38: 100110
    [0, 1, 2, 5],  # 39: 100111
    [3, 5],  # 40: 101000
    [0, 3, 5],  # 41: 101001
    [1, 3, 5],  # 42: 101010
    [0, 1, 3, 5],  # 43: 101011
    [2, 3, 5],  # 44: 101100
    [0, 2, 3, 5],  # 45: 101101
    [1, 2, 3, 5],  # 46: 101110
    [0, 1, 2, 3, 5],  # 47: 101111
    [4, 5],  # 48: 110000
    [0, 4, 5],  # 49: 110001
    [1, 4, 5],  # 50: 110010
    [0, 1, 4, 5],  # 51: 110011
    [2, 4, 5],  # 52: 110100
    [0, 2, 4, 5],  # 53: 110101
    [1, 2, 4, 5],  # 54: 110110
    [0, 1, 2, 4, 5],  # 55: 110111
    [3, 4, 5],  # 56: 111000
    [0, 3, 4, 5],  # 57: 111001
    [1, 3, 4, 5],  # 58: 111010
    [0, 1, 3, 4, 5],  # 59: 111011
    [2, 3, 4, 5],  # 60: 111100
    [0, 2, 3, 4, 5],  # 61: 111101
    [1, 2, 3, 4, 5],  # 62: 111110
    [0, 1, 2, 3, 4, 5],  # 63: 111111
    [6],  # 64: 1000000
    [0, 6],  # 65: 1000001
    [1, 6],  # 66: 1000010
    [0, 1, 6],  # 67: 1000011
    [2, 6],  # 68: 1000100
    [0, 2, 6],  # 69: 1000101
    [1, 2, 6],  # 70: 1000110
    [0, 1, 2, 6],  # 71: 1000111
    [3, 6],  # 72: 1001000
    [0, 3, 6],  # 73: 1001001
    [1, 3, 6],  # 74: 1001010
    [0, 1, 3, 6],  # 75: 1001011
    [2, 3, 6],  # 76: 1001100
    [0, 2, 3, 6],  # 77: 1001101
    [1, 2, 3, 6],  # 78: 1001110
    [0, 1, 2, 3, 6],  # 79: 1001111
    [4, 6],  # 80: 1010000
    [0, 4, 6],  # 81: 1010001
    [1, 4, 6],  # 82: 1010010
    [0, 1, 4, 6],  # 83: 1010011
    [2, 4, 6],  # 84: 1010100
    [0, 2, 4, 6],  # 85: 1010101
    [1, 2, 4, 6],  # 86: 1010110
    [0, 1, 2, 4, 6],  # 87: 1010111
    [3, 4, 6],  # 88: 1011000
    [0, 3, 4, 6],  # 89: 1011001
    [1, 3, 4, 6],  # 90: 1011010
    [0, 1, 3, 4, 6],  # 91: 1011011
    [2, 3, 4, 6],  # 92: 1011100
    [0, 2, 3, 4, 6],  # 93: 1011101
    [1, 2, 3, 4, 6],  # 94: 1011110
    [0, 1, 2, 3, 4, 6],  # 95: 1011111
    [5, 6],  # 96: 1100000
    [0, 5, 6],  # 97: 1100001
    [1, 5, 6],  # 98: 1100010
    [0, 1, 5, 6],  # 99: 1100011
    [2, 5, 6],  # 100: 1100100
    [0, 2, 5, 6],  # 101: 1100101
    [1, 2, 5, 6],  # 102: 1100110
    [0, 1, 2, 5, 6],  # 103: 1100111
    [3, 5, 6],  # 104: 1101000
    [0, 3, 5, 6],  # 105: 1101001
    [1, 3, 5, 6],  # 106: 1101010
    [0, 1, 3, 5, 6],  # 107: 1101011
    [2, 3, 5, 6],  # 108: 1101100
    [0, 2, 3, 5, 6],  # 109: 1101101
    [1, 2, 3, 5, 6],  # 110: 1101110
    [0, 1, 2, 3, 5, 6],  # 111: 1101111
    [4, 5, 6],  # 112: 1110000
    [0, 4, 5, 6],  # 113: 1110001
    [1, 4, 5, 6],  # 114: 1110010
    [0, 1, 4, 5, 6],  # 115: 1110011
    [2, 4, 5, 6],  # 116: 1110100
    [0, 2, 4, 5, 6],  # 117: 1110101
    [1, 2, 4, 5, 6],  # 118: 1110110
    [0, 1, 2, 4, 5, 6],  # 119: 1110111
    [3, 4, 5, 6],  # 120: 1111000
    [0, 3, 4, 5, 6],  # 121: 1111001
    [1, 3, 4, 5, 6],  # 122: 1111010
    [0, 1, 3, 4, 5, 6],  # 123: 1111011
    [2, 3, 4, 5, 6],  # 124: 1111100
    [0, 2, 3, 4, 5, 6],  # 125: 1111101
    [1, 2, 3, 4, 5, 6],  # 126: 1111110
    [0, 1, 2, 3, 4, 5, 6],  # 127: 1111111
    [7],  # 128: 10000000
    [0, 7],  # 129: 10000001
    [1, 7],  # 130: 10000010
    [0, 1, 7],  # 131: 10000011
    [2, 7],  # 132: 10000100
    [0, 2, 7],  # 133: 10000101
    [1, 2, 7],  # 134: 10000110
    [0, 1, 2, 7],  # 135: 10000111
    [3, 7],  # 136: 10001000
    [0, 3, 7],  # 137: 10001001
    [1, 3, 7],  # 138: 10001010
    [0, 1, 3, 7],  # 139: 10001011
    [2, 3, 7],  # 140: 10001100
    [0, 2, 3, 7],  # 141: 10001101
    [1, 2, 3, 7],  # 142: 10001110
    [0, 1, 2, 3, 7],  # 143: 10001111
    [4, 7],  # 144: 10010000
    [0, 4, 7],  # 145: 10010001
    [1, 4, 7],  # 146: 10010010
    [0, 1, 4, 7],  # 147: 10010011
    [2, 4, 7],  # 148: 10010100
    [0, 2, 4, 7],  # 149: 10010101
    [1, 2, 4, 7],  # 150: 10010110
    [0, 1, 2, 4, 7],  # 151: 10010111
    [3, 4, 7],  # 152: 10011000
    [0, 3, 4, 7],  # 153: 10011001
    [1, 3, 4, 7],  # 154: 10011010
    [0, 1, 3, 4, 7],  # 155: 10011011
    [2, 3, 4, 7],  # 156: 10011100
    [0, 2, 3, 4, 7],  # 157: 10011101
    [1, 2, 3, 4, 7],  # 158: 10011110
    [0, 1, 2, 3, 4, 7],  # 159: 10011111
    [5, 7],  # 160: 10100000
    [0, 5, 7],  # 161: 10100001
    [1, 5, 7],  # 162: 10100010
    [0, 1, 5, 7],  # 163: 10100011
    [2, 5, 7],  # 164: 10100100
    [0, 2, 5, 7],  # 165: 10100101
    [1, 2, 5, 7],  # 166: 10100110
    [0, 1, 2, 5, 7],  # 167: 10100111
    [3, 5, 7],  # 168: 10101000
    [0, 3, 5, 7],  # 169: 10101001
    [1, 3, 5, 7],  # 170: 10101010
    [0, 1, 3, 5, 7],  # 171: 10101011
    [2, 3, 5, 7],  # 172: 10101100
    [0, 2, 3, 5, 7],  # 173: 10101101
    [1, 2, 3, 5, 7],  # 174: 10101110
    [0, 1, 2, 3, 5, 7],  # 175: 10101111
    [4, 5, 7],  # 176: 10110000
    [0, 4, 5, 7],  # 177: 10110001
    [1, 4, 5, 7],  # 178: 10110010
    [0, 1, 4, 5, 7],  # 179: 10110011
    [2, 4, 5, 7],  # 180: 10110100
    [0, 2, 4, 5, 7],  # 181: 10110101
    [1, 2, 4, 5, 7],  # 182: 10110110
    [0, 1, 2, 4, 5, 7],  # 183: 10110111
    [3, 4, 5, 7],  # 184: 10111000
    [0, 3, 4, 5, 7],  # 185: 10111001
    [1, 3, 4, 5, 7],  # 186: 10111010
    [0, 1, 3, 4, 5, 7],  # 187: 10111011
    [2, 3, 4, 5, 7],  # 188: 10111100
    [0, 2, 3, 4, 5, 7],  # 189: 10111101
    [1, 2, 3, 4, 5, 7],  # 190: 10111110
    [0, 1, 2, 3, 4, 5, 7],  # 191: 10111111
    [6, 7],  # 192: 11000000
    [0, 6, 7],  # 193: 11000001
    [1, 6, 7],  # 194: 11000010
    [0, 1, 6, 7],  # 195: 11000011
    [2, 6, 7],  # 196: 11000100
    [0, 2, 6, 7],  # 197: 11000101
    [1, 2, 6, 7],  # 198: 11000110
    [0, 1, 2, 6, 7],  # 199: 11000111
    [3, 6, 7],  # 200: 11001000
    [0, 3, 6, 7],  # 201: 11001001
    [1, 3, 6, 7],  # 202: 11001010
    [0, 1, 3, 6, 7],  # 203: 11001011
    [2, 3, 6, 7],  # 204: 11001100
    [0, 2, 3, 6, 7],  # 205: 11001101
    [1, 2, 3, 6, 7],  # 206: 11001110
    [0, 1, 2, 3, 6, 7],  # 207: 11001111
    [4, 6, 7],  # 208: 11010000
    [0, 4, 6, 7],  # 209: 11010001
    [1, 4, 6, 7],  # 210: 11010010
    [0, 1, 4, 6, 7],  # 211: 11010011
    [2, 4, 6, 7],  # 212: 11010100
    [0, 2, 4, 6, 7],  # 213: 11010101
    [1, 2, 4, 6, 7],  # 214: 11010110
    [0, 1, 2, 4, 6, 7],  # 215: 11010111
    [3, 4, 6, 7],  # 216: 11011000
    [0, 3, 4, 6, 7],  # 217: 11011001
    [1, 3, 4, 6, 7],  # 218: 11011010
    [0, 1, 3, 4, 6, 7],  # 219: 11011011
    [2, 3, 4, 6, 7],  # 220: 11011100
    [0, 2, 3, 4, 6, 7],  # 221: 11011101
    [1, 2, 3, 4, 6, 7],  # 222: 11011110
    [0, 1, 2, 3, 4, 6, 7],  # 223: 11011111
    [5, 6, 7],  # 224: 11100000
    [0, 5, 6, 7],  # 225: 11100001
    [1, 5, 6, 7],  # 226: 11100010
    [0, 1, 5, 6, 7],  # 227: 11100011
    [2, 5, 6, 7],  # 228: 11100100
    [0, 2, 5, 6, 7],  # 229: 11100101
    [1, 2, 5, 6, 7],  # 230: 11100110
    [0, 1, 2, 5, 6, 7],  # 231: 11100111
    [3, 5, 6, 7],  # 232: 11101000
    [0, 3, 5, 6, 7],  # 233: 11101001
    [1, 3, 5, 6, 7],  # 234: 11101010
    [0, 1, 3, 5, 6, 7],  # 235: 11101011
    [2, 3, 5, 6, 7],  # 236: 11101100
    [0, 2, 3, 5, 6, 7],  # 237: 11101101
    [1, 2, 3, 5, 6, 7],  # 238: 11101110
    [0, 1, 2, 3, 5, 6, 7],  # 239: 11101111
    [4, 5, 6, 7],  # 240: 11110000
    [0, 4, 5, 6, 7],  # 241: 11110001
    [1, 4, 5, 6, 7],  # 242: 11110010
    [0, 1, 4, 5, 6, 7],  # 243: 11110011
    [2, 4, 5, 6, 7],  # 244: 11110100
    [0, 2, 4, 5, 6, 7],  # 245: 11110101
    [1, 2, 4, 5, 6, 7],  # 246: 11110110
    [0, 1, 2, 4, 5, 6, 7],  # 247: 11110111
    [3, 4, 5, 6, 7],  # 248: 11111000
    [0, 3, 4, 5, 6, 7],  # 249: 11111001
    [1, 3, 4, 5, 6, 7],  # 250: 11111010
    [0, 1, 3, 4, 5, 6, 7],  # 251: 11111011
    [2, 3, 4, 5, 6, 7],  # 252: 11111100
    [0, 2, 3, 4, 5, 6, 7],  # 253: 11111101
    [1, 2, 3, 4, 5, 6, 7],  # 254: 11111110
    [0, 1, 2, 3, 4, 5, 6, 7],  # 255: 11111111
]


class BitBoard:
    """
    This class is used to encapsulate a 64-bit integer to use as a chessboard of bits.
    """

    def __init__(self, uint64_number):
        """
        Run when a BitBoard object is created.

        Parameters
        ----------
        uint64_number : int or numpy.uint64
                        a 64-bit unsigned integer to initialize the BitBoard to.
        """
        # a 64-bit integer that represents the bitboard
        self.num = np.uint64(uint64_number)

    def __getitem__(self, n):
        """
        Allows using [] operator for a BitBoard object to retrieve nth bit from the right.

        Parameters
        ----------
        n : int
            the index of the bit to retrieve, counting from right to left.

        Returns
        -------
        int
            the bit from the right.
        """
        return (self.num >> np.uint64(n)) & UINT64_ONE

    def __setitem__(self, n, bit):
        """
        Allows using [] operator for a BitBoard object to set the nth bit from the right.

        Parameters
        ----------
        n : int
            the index of the bit to set, counting from right to left.
        bit : int
            the value to set the nth bit to. Should be 0 or 1.
        """
        self.num ^= (np.uint64(-bit) ^ self.num) & (UINT64_ONE << np.uint64(n))

    def __str__(self):
        """
        Overrides default function to a string showing a 8x8 chessboard with bits.

        Returns
        -------
        str
            a string of 64 bits with line breaks for every 8 bits.
        """
        return textwrap.fill('{:064b}'.format(self.num), 8)

    def __and__(self, other):
        """
        Allows using the AND operator (&) for two BitBoard objects. Returns the result of a bitwise and (&) of self
        and other.

        Parameters
        ----------
        other : BitBoard
            a BitBoard object to AND with self

        Returns
        -------
        BitBoard
            the result of a bitwise and (&) of self and other
        """
        return BitBoard(self.num & other.num)

    def __or__(self, other):
        """
        Allows using the OR operator (|) for two BitBoard objects. Returns the result of a bitwise or (|) of self and
        other.

        Parameters
        ----------
        other : BitBoard
            a BitBoard object to OR with self

        Returns
        -------
        BitBoard
            the result of a bitwise or (|) of self and other.
        """
        return BitBoard(self.num | other.num)

    def __invert__(self):
        """
        Allows using the NOT operator (~) on a BitBoard object. Returns the inverse of the encapsulated 64-bit unsigned
        integer.

        Returns
        -------
        BitBoard
            the inverse of the encapsulated 64-bit unsigned integer
        """
        return BitBoard(~self.num)

    def __eq__(self, other):
        """
        Allows using the equality operator (==) on a BitBoard object. Returns True if self and other have the same
        number, False otherwise.

        Parameters
        ----------
        other : BitBoard
            a BitBoard object to check equality against

        Returns
        -------
        bool
            True if self and other have the same number, False otherwise.
        """
        # TODO considering allowing other to be either Int or BitBoard type
        return self.num == other.num

    def indices(self):
        """
        Returns the indices of bits with value 1.

        Returns
        -------
        list of int
            the indices of bits with value 1
        """

        # We used lookup tables here. Read more about other methods here:
        # https://chessprogramming.wikispaces.com/Bitboard+Serialization

        if self.num == 0:
            return []

        bits = []

        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            row = (self.num >> UINT64_PADDING[i]) & EIGHT_ONES
            indices = row_to_indices[row]
            for index in indices:
                bits.append(index + i*8)

        return bits


# only runs when this module is called directly
if __name__ == '__main__':
    bb = BitBoard(1)
    print(bb[0])
    print(bb[1])
    print(bb)
