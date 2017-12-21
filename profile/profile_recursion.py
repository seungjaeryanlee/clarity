"""
This file profiles the code to provide analysis of most time-intensive functions in Clarity.
Note that this file will contain PyCharm warnings on imports. Please disregard them.
"""
import cProfile

# TODO check if there is a better method for this
import sys
sys.path.append('../clarity')
from clarity.Board import Board
from clarity.recursion import perft

cProfile.run('perft(Board(), 2)', filename='perft.prof')
