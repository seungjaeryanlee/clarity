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

    def test_str(self):
        """
        Tests the __str__() function of the Board class
        """
        board = Board()
        self.assertEqual(str(board), 'rnbqkbnr\n'
                                     'pppppppp\n'
                                     '--------\n'
                                     '--------\n'
                                     '--------\n'
                                     '--------\n'
                                     'PPPPPPPP\n'
                                     'RNBQKBNR')

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

    def test_find_checks(self):
        """
        TODO write tests
        Tests the find_checks() function of the Board class
        """
        pass

    def test_find_pawn_check(self):
        """
        TODO write tests
        Tests the _find_pawn_checks() function of the Board class
        """
        # normal
        board = Board('7k/8/8/8/6p1/7K/8/8 w - - 0 1')
        pawn_sqs = board._find_pawn_checks()
        self.assertEqual(len(pawn_sqs), 1)
        self.assertListEqual(sorted(pawn_sqs), sorted([Sq.G4]))

        # no check
        board = Board('7k/8/8/8/p6p/7K/8/8 w - - 0 1')
        pawn_sqs = board._find_pawn_checks()
        self.assertEqual(len(pawn_sqs), 0)

        # double check
        board = Board('7K/8/8/8/8/4k3/3P1P2/8 b - - 0 1')
        pawn_sqs = board._find_pawn_checks()
        self.assertEqual(len(pawn_sqs), 2)
        self.assertListEqual(sorted(pawn_sqs), sorted([Sq.D2, Sq.F2]))

        # pawn on 2nd/7th row (promotion)
        board = Board('7k/8/8/8/8/8/3p4/4K3 w - - 0 1')
        pawn_sqs = board._find_pawn_checks()
        self.assertEqual(len(pawn_sqs), 1)
        self.assertListEqual(sorted(pawn_sqs), sorted([Sq.D2]))

    def test_pawn_move_gen(self):
        """
        Tests the pawn_move_gen() function of the Board class
        """
        # test on starting position
        board = Board()
        pawn_moves = board._pawn_move_gen()
        self.assertEqual(len(pawn_moves), 16)
        self.assertListEqual(sorted(pawn_moves), sorted([Move(Sq.A2, Sq.A3, MoveType.QUIET),
                                                         Move(Sq.A2, Sq.A4, MoveType.DOUBLE),
                                                         Move(Sq.B2, Sq.B3, MoveType.QUIET),
                                                         Move(Sq.B2, Sq.B4, MoveType.DOUBLE),
                                                         Move(Sq.C2, Sq.C3, MoveType.QUIET),
                                                         Move(Sq.C2, Sq.C4, MoveType.DOUBLE),
                                                         Move(Sq.D2, Sq.D3, MoveType.QUIET),
                                                         Move(Sq.D2, Sq.D4, MoveType.DOUBLE),
                                                         Move(Sq.E2, Sq.E3, MoveType.QUIET),
                                                         Move(Sq.E2, Sq.E4, MoveType.DOUBLE),
                                                         Move(Sq.F2, Sq.F3, MoveType.QUIET),
                                                         Move(Sq.F2, Sq.F4, MoveType.DOUBLE),
                                                         Move(Sq.G2, Sq.G3, MoveType.QUIET),
                                                         Move(Sq.G2, Sq.G4, MoveType.DOUBLE),
                                                         Move(Sq.H2, Sq.H3, MoveType.QUIET),
                                                         Move(Sq.H2, Sq.H4, MoveType.DOUBLE)]))

        # test for capture
        board = Board('7k/8/8/3p4/4P3/8/8/K7 w - - 0 1')
        pawn_moves = board._pawn_move_gen()
        self.assertEqual(len(pawn_moves), 2)
        self.assertListEqual(sorted(pawn_moves), sorted([Move(Sq.E4, Sq.E5, MoveType.QUIET),
                                                         Move(Sq.E4, Sq.D5, MoveType.CAPTURE)]))

        # test for promotions
        board = Board('k6K/8/8/8/8/8/7p/6N1 b - - 0 1')
        pawn_moves = board._pawn_move_gen()
        self.assertEqual(len(pawn_moves), 8)
        self.assertListEqual(sorted(pawn_moves), sorted([Move(Sq.H2, Sq.H1, MoveType.N_PROMO),
                                                         Move(Sq.H2, Sq.H1, MoveType.B_PROMO),
                                                         Move(Sq.H2, Sq.H1, MoveType.R_PROMO),
                                                         Move(Sq.H2, Sq.H1, MoveType.Q_PROMO),
                                                         Move(Sq.H2, Sq.G1, MoveType.N_PROMO_CAPTURE),
                                                         Move(Sq.H2, Sq.G1, MoveType.B_PROMO_CAPTURE),
                                                         Move(Sq.H2, Sq.G1, MoveType.R_PROMO_CAPTURE),
                                                         Move(Sq.H2, Sq.G1, MoveType.Q_PROMO_CAPTURE)]))

        # test for en passant capture
        board = Board('k7/8/8/8/3pP3/8/8/7K b - e3 0 1')
        pawn_moves = board._pawn_move_gen()
        self.assertEqual(len(pawn_moves), 2)
        self.assertListEqual(sorted(pawn_moves), sorted([Move(Sq.D4, Sq.D3, MoveType.QUIET),
                                                         Move(Sq.D4, Sq.E3, MoveType.EP_CAPTURE)]))

    def test_knight_move_gen(self):
        """
        Tests the knight_move_gen() function of the Board class
        """
        board = Board()
        knight_moves = board._knight_move_gen()
        self.assertEqual(len(knight_moves), 4)
        self.assertListEqual(sorted(knight_moves), sorted([Move(Sq.B1, Sq.A3, MoveType.QUIET),
                                                           Move(Sq.B1, Sq.C3, MoveType.QUIET),
                                                           Move(Sq.G1, Sq.F3, MoveType.QUIET),
                                                           Move(Sq.G1, Sq.H3, MoveType.QUIET)]))

        board = Board('K6k/8/8/8/8/6p1/8/7N w - - 0 1')
        knight_moves = board._knight_move_gen()
        self.assertEqual(len(knight_moves), 2)
        self.assertListEqual(sorted(knight_moves), sorted([Move(Sq.H1, Sq.G3, MoveType.CAPTURE),
                                                           Move(Sq.H1, Sq.F2, MoveType.QUIET)]))

        board = Board('K7/8/8/6R1/4n3/8/4n3/2k5 b - - 0 1')
        knight_moves = board._knight_move_gen()
        self.assertEqual(len(knight_moves), 13)
        self.assertListEqual(sorted(knight_moves), sorted([Move(Sq.E2, Sq.C3, MoveType.QUIET),
                                                           Move(Sq.E2, Sq.D4, MoveType.QUIET),
                                                           Move(Sq.E2, Sq.F4, MoveType.QUIET),
                                                           Move(Sq.E2, Sq.G3, MoveType.QUIET),
                                                           Move(Sq.E2, Sq.G1, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.D2, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.C3, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.C5, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.D6, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.F6, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.G5, MoveType.CAPTURE),
                                                           Move(Sq.E4, Sq.G3, MoveType.QUIET),
                                                           Move(Sq.E4, Sq.F2, MoveType.QUIET)]))
        pass

    def test_bishop_move_gen(self):
        """
        Tests the bishop_move_gen() function of the Board class
        """
        board = Board()
        bishop_moves = board._bishop_move_gen()
        self.assertEqual(len(bishop_moves), 0)

        board = Board('K6k/8/8/8/8/6p1/8/7B w - - 0 1')
        bishop_moves = board._bishop_move_gen()
        self.assertEqual(len(bishop_moves), 6)
        self.assertListEqual(sorted(bishop_moves), sorted([Move(Sq.H1, Sq.G2, MoveType.QUIET),
                                                           Move(Sq.H1, Sq.F3, MoveType.QUIET),
                                                           Move(Sq.H1, Sq.E4, MoveType.QUIET),
                                                           Move(Sq.H1, Sq.D5, MoveType.QUIET),
                                                           Move(Sq.H1, Sq.C6, MoveType.QUIET),
                                                           Move(Sq.H1, Sq.B7, MoveType.QUIET)]))

        board = Board('k6K/8/2N5/8/8/5b2/8/7b b - - 0 1')
        bishop_moves = board._bishop_move_gen()
        self.assertEqual(len(bishop_moves), 9)
        self.assertListEqual(sorted(bishop_moves), sorted([Move(Sq.H1, Sq.G2, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.G2, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.E2, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.D1, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.G4, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.H5, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.E4, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.D5, MoveType.QUIET),
                                                           Move(Sq.F3, Sq.C6, MoveType.CAPTURE)]))
        pass

    def test_rook_move_gen(self):
        """
        Tests the rook_move_gen() function of the Board class
        """
        board = Board()
        rook_moves = board._rook_move_gen()
        self.assertEqual(len(rook_moves), 0)

        board = Board('K5k1/8/8/8/8/8/8/7R w - - 0 1')
        rook_moves = board._rook_move_gen()
        self.assertEqual(len(rook_moves), 14)
        self.assertListEqual(sorted(rook_moves), sorted([Move(Sq.H1, Sq.H2, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H3, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H4, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H5, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H6, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H7, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H8, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.G1, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.F1, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.E1, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.D1, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.C1, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.B1, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.A1, MoveType.QUIET)]))

        board = Board('K6k/8/8/8/8/8/8/2N2r1r b - - 0 1')
        rook_moves = board._rook_move_gen()
        self.assertEqual(len(rook_moves), 18)
        self.assertListEqual(sorted(rook_moves), sorted([Move(Sq.H1, Sq.H2, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H3, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H4, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H5, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H6, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.H7, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.G1, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F2, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F3, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F4, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F5, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F6, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F7, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.F8, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.G1, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.E1, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.D1, MoveType.QUIET),
                                                         Move(Sq.F1, Sq.C1, MoveType.CAPTURE)]))

    def test_queen_move_gen(self):
        """
        Tests the queen_move_gen() function of the Board class
        """
        board = Board()
        queen_moves = board._queen_move_gen()
        self.assertEqual(len(queen_moves), 0)

        board = Board('K5k1/8/8/8/8/8/8/6rQ w - - 0 1')
        queen_moves = board._queen_move_gen()
        self.assertEqual(len(queen_moves), 14)
        self.assertListEqual(sorted(queen_moves), sorted([Move(Sq.H1, Sq.H2, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H3, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H4, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H5, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H6, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H7, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H8, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.G2, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.F3, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.E4, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.D5, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.C6, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.B7, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.G1, MoveType.CAPTURE)]))

        board = Board('k3K2N/8/8/8/3p4/5b2/8/4R1qq b - - 0 1')
        queen_moves = board._queen_move_gen()
        self.assertEqual(len(queen_moves), 20)
        self.assertListEqual(sorted(queen_moves), sorted([Move(Sq.H1, Sq.H2, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H3, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H4, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H5, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H6, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H7, MoveType.QUIET),
                                                          Move(Sq.H1, Sq.H8, MoveType.CAPTURE),
                                                          Move(Sq.H1, Sq.G2, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G2, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G3, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G4, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G5, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G6, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G7, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.G8, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.F1, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.E1, MoveType.CAPTURE),
                                                          Move(Sq.G1, Sq.F2, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.E3, MoveType.QUIET),
                                                          Move(Sq.G1, Sq.H2, MoveType.QUIET)]))

    def test_king_move_gen(self):
        """
        Tests the king_move_gen() function of the Board class
        """
        board = Board()
        king_moves = board._king_move_gen()
        self.assertEqual(len(king_moves), 0)

        board = Board('k7/8/8/8/8/6p1/8/6nK w - - 0 1')
        king_moves = board._king_move_gen()
        self.assertEqual(len(king_moves), 3)
        self.assertListEqual(sorted(king_moves), sorted([Move(Sq.H1, Sq.H2, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.G2, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.G1, MoveType.CAPTURE)]))

        board = Board('8/8/8/3kb3/3N4/8/8/6nK b - - 0 1')
        king_moves = board._king_move_gen()
        self.assertEqual(len(king_moves), 7)
        self.assertListEqual(sorted(king_moves), sorted([Move(Sq.D5, Sq.C4, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.C5, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.C6, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.D6, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.E6, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.E4, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.D4, MoveType.CAPTURE)]))
