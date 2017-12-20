#!/usr/bin/env python3
"""
This file defines the Sq enum.
"""
from enum import IntEnum


class Sq(IntEnum):
    """
    This enum translates filerank name of the chess square to a index of the bitboard.
    """

    A8 = 63
    B8 = 62
    C8 = 61
    D8 = 60
    E8 = 59
    F8 = 58
    G8 = 57
    H8 = 56
    A7 = 55
    B7 = 54
    C7 = 53
    D7 = 52
    E7 = 51
    F7 = 50
    G7 = 49
    H7 = 48
    A6 = 47
    B6 = 46
    C6 = 45
    D6 = 44
    E6 = 43
    F6 = 42
    G6 = 41
    H6 = 40
    A5 = 39
    B5 = 38
    C5 = 37
    D5 = 36
    E5 = 35
    F5 = 34
    G5 = 33
    H5 = 32
    A4 = 31
    B4 = 30
    C4 = 29
    D4 = 28
    E4 = 27
    F4 = 26
    G4 = 25
    H4 = 24
    A3 = 23
    B3 = 22
    C3 = 21
    D3 = 20
    E3 = 19
    F3 = 18
    G3 = 17
    H3 = 16
    A2 = 15
    B2 = 14
    C2 = 13
    D2 = 12
    E2 = 11
    F2 = 10
    G2 = 9
    H2 = 8
    A1 = 7
    B1 = 6
    C1 = 5
    D1 = 4
    E1 = 3
    F1 = 2
    G1 = 1
    H1 = 0

    @staticmethod
    def filerank_to_sq(filerank):
        """
        Returns the Sq value of the given filerank string.

        Parameters
        ----------
        filerank : str
            a filerank format [a-h][1-8] string

        Returns
        -------
        Sq
            the Sq index value of the given filerank string
        """
        # TODO validate filerank
        return Sq(8 * (int(filerank[1]) - 1) + (ord('h') - ord(filerank[0])))

    @staticmethod
    def sq_to_filerank(sq):
        """
        Returns the filerank string of the given Sq value.

        Parameters
        ----------
        sq : Sq
            the Sq value to convert to filerank notation

        Returns
        -------
        str
            the filerank string ([a-h][1-8]) of the given Sq value
        """
        # TODO validate sq
        return chr(ord('h') - int(sq % 8)) + str(int(sq / 8) + 1)


# only runs when this module is called directly
if __name__ == '__main__':
    print('E4: ' + str(Sq.filerank_to_sq('e4')))
    print('F6: ' + str(Sq.filerank_to_sq('f6')))

    print('D4: ' + str(Sq.sq_to_filerank(Sq.D4)))
    print('F3: ' + str(Sq.sq_to_filerank(Sq.F3)))
