#!/usr/bin/env python3
"""
This file defines the Direction enum.
"""
from enum import Enum


class Direction(Enum):
    """
    This enum contains values for each direction.
    """

    U = 1
    UR = 2
    R = 3
    DR = 4
    D = 5
    DL = 6
    L = 7
    UL = 8


# only runs when this module is called directly
if __name__ == '__main__':
    for direction in Direction:
        print(direction)
