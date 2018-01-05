#!/usr/bin/env python3
"""
This script runs Clarity Chess in UCI (Universal Chess Interface) mode.
"""
import sys


def uci():
    """
    Runs Clarity in UCI mode
    """
    while True:
        line = sys.stdin.readline().strip()
        command = line.split(' ')[0]
        options = line.split(' ')[1:]

        if command == 'uci':
            print('id name Clarity')
            print('id author Seung Jae (Ryan) Lee')
            print('uciok')

        if command == 'isready':
            print('readyok')

        if command == 'quit':
            return


# only runs when this module is called directly
if __name__ == '__main__':
    uci()
