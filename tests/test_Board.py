#!/usr/bin/env python3
"""
This file defines unit tests for the Board class.
"""
import unittest
from Board import Board
from Color import Color
from Move import Move
from MoveType import MoveType
from Piece import Piece
from Sq import Sq


class TestBoardClass(unittest.TestCase):
    """
    This class tests the Board class.
    """

    def test_init(self):
        """
        Tests the __init__() function of the Board class.
        """
        board = Board()
        self.assertEqual(board.bitboards[Piece.WP].num,
                         int('0000000000000000000000000000000000000000000000001111111100000000', 2))
        self.assertEqual(board.bitboards[Piece.WN].num,
                         int('0000000000000000000000000000000000000000000000000000000001000010', 2))
        self.assertEqual(board.bitboards[Piece.WB].num,
                         int('0000000000000000000000000000000000000000000000000000000000100100', 2))
        self.assertEqual(board.bitboards[Piece.WR].num,
                         int('0000000000000000000000000000000000000000000000000000000010000001', 2))
        self.assertEqual(board.bitboards[Piece.WQ].num,
                         int('0000000000000000000000000000000000000000000000000000000000010000', 2))
        self.assertEqual(board.bitboards[Piece.WK].num,
                         int('0000000000000000000000000000000000000000000000000000000000001000', 2))

        self.assertEqual(board.bitboards[Piece.BP].num,
                         int('0000000011111111000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BN].num,
                         int('0100001000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BB].num,
                         int('0010010000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BR].num,
                         int('1000000100000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BQ].num,
                         int('0001000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BK].num,
                         int('0000100000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.turn, Color.WHITE)
        self.assertEqual(board.ep_square, -1)
        self.assertEqual(board.wk_castling, True)
        self.assertEqual(board.wq_castling, True)
        self.assertEqual(board.bk_castling, True)
        self.assertEqual(board.bq_castling, True)
        self.assertEqual(board.half_move_clock, 0)
        self.assertEqual(board.full_move_count, 1)

        board = Board('K7/8/8/8/8/8/8/7k b - - 0 1')
        self.assertEqual(board.bitboards[Piece.WP].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.WN].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.WB].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.WR].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.WQ].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.WK].num,
                         int('1000000000000000000000000000000000000000000000000000000000000000', 2))

        self.assertEqual(board.bitboards[Piece.BP].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BN].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BB].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BR].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BQ].num,
                         int('0000000000000000000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(board.bitboards[Piece.BK].num,
                         int('0000000000000000000000000000000000000000000000000000000000000001', 2))
        self.assertEqual(board.turn, Color.BLACK)
        self.assertEqual(board.ep_square, -1)
        self.assertEqual(board.wk_castling, False)
        self.assertEqual(board.wq_castling, False)
        self.assertEqual(board.bk_castling, False)
        self.assertEqual(board.bq_castling, False)
        self.assertEqual(board.half_move_clock, 0)
        self.assertEqual(board.full_move_count, 1)

    def test_fen(self):
        """
        Tests the fen() function of the Board class
        """
        self._test_get_fen()
        self._test_set_fen()

    def _test_get_fen(self):
        """
        TODO Add more tests
        Tests the _get_fen() function of the Board class
        """
        board = Board()
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

        board.bitboards[Piece.WP][Sq.E4] = 1
        board.bitboards[Piece.WP][Sq.E2] = 0
        board.turn = Color.BLACK
        board.wk_castling = False
        board.bk_castling = False
        board.ep_square = Sq.A8
        board.half_move_clock = 13
        board.full_move_count = 20
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b Qq a8 13 20')

    def _test_set_fen(self):
        """
        TODO Add more tests
        Tests the _set_fen() function of the Board class
        """
        board = Board()
        board.fen('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        self.assertEqual(board.bitboards[Piece.WP][Sq.E2], 0)
        self.assertEqual(board.color_bb[Color.WHITE][Sq.E2], 0)
        self.assertEqual(board.bitboards[Piece.WP][Sq.E4], 1)
        self.assertEqual(board.color_bb[Color.WHITE][Sq.E4], 1)
        self.assertEqual(board.turn, Color.BLACK)
        self.assertEqual(board.wk_castling, True)
        self.assertEqual(board.wq_castling, True)
        self.assertEqual(board.bk_castling, True)
        self.assertEqual(board.bq_castling, True)
        self.assertEqual(board.ep_square, Sq.E3)
        self.assertEqual(board.half_move_clock, 0)
        self.assertEqual(board.full_move_count, 1)
        self.assertListEqual(sorted(board.piece_sq[Piece.WP]),
                             sorted([Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.E4, Sq.F2, Sq.G2, Sq.H2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WN]),
                             sorted([Sq.B1, Sq.G1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WB]),
                             sorted([Sq.C1, Sq.F1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WR]),
                             sorted([Sq.A1, Sq.H1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WQ]),
                             sorted([Sq.D1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WK]),
                             sorted([Sq.E1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BP]),
                             sorted([Sq.A7, Sq.B7, Sq.C7, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BN]),
                             sorted([Sq.B8, Sq.G8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BB]),
                             sorted([Sq.C8, Sq.F8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BR]),
                             sorted([Sq.A8, Sq.H8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BQ]),
                             sorted([Sq.D8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BK]),
                             sorted([Sq.E8]))

        board.fen('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w - c6 1 2')
        self.assertEqual(board.bitboards[Piece.BP][Sq.C7], 0)
        self.assertEqual(board.color_bb[Color.BLACK][Sq.C7], 0)
        self.assertEqual(board.bitboards[Piece.BP][Sq.C5], 1)
        self.assertEqual(board.color_bb[Color.BLACK][Sq.C5], 1)
        self.assertEqual(board.turn, Color.WHITE)
        self.assertEqual(board.wk_castling, False)
        self.assertEqual(board.wq_castling, False)
        self.assertEqual(board.bk_castling, False)
        self.assertEqual(board.bq_castling, False)
        self.assertEqual(board.ep_square, Sq.C6)
        self.assertEqual(board.half_move_clock, 1)
        self.assertEqual(board.full_move_count, 2)
        self.assertListEqual(sorted(board.piece_sq[Piece.WP]),
                             sorted([Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.E4, Sq.F2, Sq.G2, Sq.H2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WN]),
                             sorted([Sq.B1, Sq.G1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WB]),
                             sorted([Sq.C1, Sq.F1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WR]),
                             sorted([Sq.A1, Sq.H1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WQ]),
                             sorted([Sq.D1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WK]),
                             sorted([Sq.E1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BP]),
                             sorted([Sq.A7, Sq.B7, Sq.C5, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BN]),
                             sorted([Sq.B8, Sq.G8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BB]),
                             sorted([Sq.C8, Sq.F8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BR]),
                             sorted([Sq.A8, Sq.H8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BQ]),
                             sorted([Sq.D8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BK]),
                             sorted([Sq.E8]))

    def test_make_move(self):
        """
        Tests the make_move() function of the Board class
        """
        board = Board()
        move = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        capture = board.make_move(move)
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('00001000000000001111011111111111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1111111111111111000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(capture, -1)
        self.assertListEqual(sorted(board.piece_sq[Piece.WP]),
                             sorted([Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.E4, Sq.F2, Sq.G2, Sq.H2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WN]),
                             sorted([Sq.B1, Sq.G1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WB]),
                             sorted([Sq.C1, Sq.F1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WR]),
                             sorted([Sq.A1, Sq.H1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WQ]),
                             sorted([Sq.D1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WK]),
                             sorted([Sq.E1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BP]),
                             sorted([Sq.A7, Sq.B7, Sq.C7, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BN]),
                             sorted([Sq.B8, Sq.G8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BB]),
                             sorted([Sq.C8, Sq.F8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BR]),
                             sorted([Sq.A8, Sq.H8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BQ]),
                             sorted([Sq.D8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BK]),
                             sorted([Sq.E8]))

        move = Move(Sq.B8, Sq.C6, MoveType.QUIET)
        capture = board.make_move(move)
        self.assertEqual(board.fen(), 'r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('00001000000000001111011111111111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1011111111111111001000000000000000000000000000000000000000000000', 2))
        self.assertEqual(capture, -1)
        self.assertListEqual(sorted(board.piece_sq[Piece.WP]),
                             sorted([Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.E4, Sq.F2, Sq.G2, Sq.H2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WN]),
                             sorted([Sq.B1, Sq.G1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WB]),
                             sorted([Sq.C1, Sq.F1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WR]),
                             sorted([Sq.A1, Sq.H1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WQ]),
                             sorted([Sq.D1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WK]),
                             sorted([Sq.E1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BP]),
                             sorted([Sq.A7, Sq.B7, Sq.C7, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BN]),
                             sorted([Sq.C6, Sq.G8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BB]),
                             sorted([Sq.C8, Sq.F8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BR]),
                             sorted([Sq.A8, Sq.H8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BQ]),
                             sorted([Sq.D8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BK]),
                             sorted([Sq.E8]))

        move = Move(Sq.E1, Sq.E2, MoveType.QUIET)
        capture = board.make_move(move)
        self.assertEqual(board.fen(), 'r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPPKPPP/RNBQ1BNR b kq - 2 2')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('00001000000000001111111111110111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1011111111111111001000000000000000000000000000000000000000000000', 2))
        self.assertEqual(capture, -1)
        self.assertListEqual(sorted(board.piece_sq[Piece.WP]),
                             sorted([Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.E4, Sq.F2, Sq.G2, Sq.H2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WN]),
                             sorted([Sq.B1, Sq.G1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WB]),
                             sorted([Sq.C1, Sq.F1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WR]),
                             sorted([Sq.A1, Sq.H1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WQ]),
                             sorted([Sq.D1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WK]),
                             sorted([Sq.E2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BP]),
                             sorted([Sq.A7, Sq.B7, Sq.C7, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BN]),
                             sorted([Sq.C6, Sq.G8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BB]),
                             sorted([Sq.C8, Sq.F8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BR]),
                             sorted([Sq.A8, Sq.H8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BQ]),
                             sorted([Sq.D8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BK]),
                             sorted([Sq.E8]))

        board.fen('rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w - - 0 2')
        move = Move(Sq.E4, Sq.D5, MoveType.CAPTURE)
        capture = board.make_move(move)
        self.assertEqual(board.fen(), 'rnbqkbnr/ppp1pppp/8/3P4/8/8/PPPP1PPP/RNBQKBNR b - - 0 2')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('0001000000000000000000001111011111111111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1111111111101111000000000000000000000000000000000000000000000000', 2))
        self.assertEqual(capture, Piece.BP)
        self.assertListEqual(sorted(board.piece_sq[Piece.WP]),
                             sorted([Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.D5, Sq.F2, Sq.G2, Sq.H2]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WN]),
                             sorted([Sq.B1, Sq.G1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WB]),
                             sorted([Sq.C1, Sq.F1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WR]),
                             sorted([Sq.A1, Sq.H1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WQ]),
                             sorted([Sq.D1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.WK]),
                             sorted([Sq.E1]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BP]),
                             sorted([Sq.A7, Sq.B7, Sq.C7, Sq.E7, Sq.F7, Sq.G7, Sq.H7]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BN]),
                             sorted([Sq.B8, Sq.G8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BB]),
                             sorted([Sq.C8, Sq.F8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BR]),
                             sorted([Sq.A8, Sq.H8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BQ]),
                             sorted([Sq.D8]))
        self.assertListEqual(sorted(board.piece_sq[Piece.BK]),
                             sorted([Sq.E8]))

    def test_move_gen(self):
        """
        # TODO add more specific tests comparing individual moves using Counter()
        Tests the move_gen() function of the Board class
        """
        board = Board()
        moves = board.move_gen()
        self.assertEqual(len(moves), 20)

        # From https://chessprogramming.wikispaces.com/Perft+Results
        board.fen('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1')
        moves = board.move_gen()
        self.assertEqual(len(moves), 48)

        board.fen('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1')
        moves = board.move_gen()
        self.assertEqual(len(moves), 14)

        board.fen('r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1')
        moves = board.move_gen()
        self.assertEqual(len(moves), 6)

        board.fen('rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8')
        moves = board.move_gen()
        self.assertEqual(len(moves), 44)

        board.fen('r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10')
        moves = board.move_gen()
        self.assertEqual(len(moves), 1)

    def test_pawn_move_gen(self):
        """
        TODO write tests
        Tests the pawn_move_gen() function of the Board class
        """
        pass

    def test_knight_move_gen(self):
        """
        TODO write tests
        Tests the knight_move_gen() function of the Board class
        """
        pass

    def test_bishop_move_gen(self):
        """
        TODO write tests
        Tests the pawn_move_gen() function of the Board class
        """
        pass

    def test_rook_move_gen(self):
        """
        TODO write tests
        Tests the knight_move_gen() function of the Board class
        """
        pass

    def test_queen_move_gen(self):
        """
        TODO write tests
        Tests the pawn_move_gen() function of the Board class
        """
        pass

    def test_king_move_gen(self):
        """
        TODO write tests
        Tests the knight_move_gen() function of the Board class
        """
        pass
