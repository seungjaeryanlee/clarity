#!/usr/bin/env python3
"""
This file profiles the code to provide analysis of most time-intensive functions in Clarity.
Note that this file will contain PyCharm warnings on imports. Please disregard them.
"""
import cProfile

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clarity.Board import Board
from clarity.recursion import perft, negamax

cProfile.run('perft(Board(), 2)', filename='perft.prof')
cProfile.run('negamax(Board(), 3)', filename='negamax.prof')
