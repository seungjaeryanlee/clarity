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
        command = sys.stdin.readline().strip()

        if command == 'uci':
            print('id name Clarity')
            print('id author Seung Jae (Ryan) Lee')
            print('uciok')

        if command == 'isready':
            print('readyok')


# only runs when this module is called directly
if __name__ == '__main__':
    uci()
