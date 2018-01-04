#!/usr/bin/env python3
"""
This file defines unit tests for the recursion module.
"""
from clarity.Board import Board
from clarity.Move import Move
from clarity.MoveType import MoveType
from clarity.recursion import divide, perft, negamax, _negamax_recur
from clarity.Sq import Sq


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
        assert perft(board, 1) == 46
        assert perft(board, 2) == 2079

        # Perft from https://www.chessprogramming.net/perfect-perft/
        board = Board('3k4/3p4/8/K1P4r/8/8/8/8 b - - 0 1')
        assert perft(board, 1) == 18
        assert perft(board, 2) == 92
        assert perft(board, 3) == 1670
        assert perft(board, 4) == 10138

        board = Board('8/8/4k3/8/2p5/8/B2P2K1/8 w - - 0 1')
        assert perft(board, 1) == 13
        assert perft(board, 2) == 102
        assert perft(board, 3) == 1266
        assert perft(board, 4) == 10276

    def test_perft_mate(self):
        """
        Tests the perft() function of the recursion module where terminal node exists.
        """
        board = Board('k7/ppp5/8/8/8/8/8/K6R w - - 0 1')
        assert perft(board, 1) == 16
        assert perft(board, 2) == 105
        assert perft(board, 3) == 1747
        assert perft(board, 4) == 11314

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

    def test_negamax_mate(self):
        """
        Tests the negamax() function of the recursion module with mate in X positions.
        """
        board = Board('k7/ppp5/8/8/8/8/8/K6R w - - 0 1')
        best_move = negamax(board, 1)
        assert best_move == Move(Sq.H1, Sq.H8, MoveType.QUIET)

        board = Board('q6k/8/8/8/8/8/5PPP/7K b - - 0 1')
        best_move = negamax(board, 1)
        assert best_move == Move(Sq.A8, Sq.A1, MoveType.QUIET)
