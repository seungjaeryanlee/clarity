#!/usr/bin/env python3
"""
This file defines unit tests for the recursion module.
"""
from clarity.Board import Board
from clarity.recursion import perft, negamax, _negamax_recur


class TestRecursion:
    """
    This class tests the Color enum.
    """

    def test_perft(self):
        """
        Tests the perft() function of the recursion module.
        """
        # Perft results from https://chessprogramming.wikispaces.com/Perft+Results
        board = Board()
        assert perft(board, 1) == 20
        assert perft(board, 2) == 400

        board = Board('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1')
        assert perft(board, 1) == 48
        assert perft(board, 2) == 2039

        board = Board('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1')
        assert perft(board, 1) == 14
        assert perft(board, 2) == 191

        board = Board('r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1')
        assert perft(board, 1) == 6
        assert perft(board, 2) == 264

        board = Board('rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8')
        assert perft(board, 1) == 44
        assert perft(board, 2) == 1486

        board = Board('r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10')
        assert perft(board, 1) == 1
        assert perft(board, 2) == 46

    def test_negamax(self):
        """
        Tests the negamax() function of the recursion module.
        """
        # TODO add more tests

        # test that the best move negamax() returns gives the best score from _negamax_recur()
        board = Board()
        best_move = negamax(board, 1)
        best_score = _negamax_recur(board, 1)
        board.make_move(best_move)
        assert board.eval() == -best_score

        # test that _negamax_recur() gives the best score
        board = Board()
        moves = board.move_gen()
        best_score = _negamax_recur(board, 1)
        for move in moves:
            captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
            assert best_score >= -board.eval()
            board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
