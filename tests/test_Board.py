#!/usr/bin/env python3
"""
This file defines unit tests for the Board class.
"""
import unittest
from clarity import constants as const
from clarity.BitBoard import BitBoard
from clarity.Board import Board
from clarity.Color import Color
from clarity.Direction import Direction
from clarity.Move import Move
from clarity.MoveType import MoveType
from clarity.Piece import Piece
from clarity.Sq import Sq


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
        self.assertEqual(board.castling[Piece.WK], True)
        self.assertEqual(board.castling[Piece.WQ], True)
        self.assertEqual(board.castling[Piece.BK], True)
        self.assertEqual(board.castling[Piece.BQ], True)
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
        self.assertEqual(board.castling[Piece.WK], False)
        self.assertEqual(board.castling[Piece.WQ], False)
        self.assertEqual(board.castling[Piece.BK], False)
        self.assertEqual(board.castling[Piece.BQ], False)
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
        board.castling[Piece.WK] = False
        board.castling[Piece.BK] = False
        board.ep_square = Sq.A8
        board.half_move_clock = 13
        board.full_move_count = 20
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b Qq a8 13 20')

    def _test_set_fen(self):
        """
        Tests the _set_fen() function of the Board class
        """
        board = Board()
        board.fen('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        self.assertEqual(board.bitboards[Piece.WP][Sq.E2], 0)
        self.assertEqual(board.color_bb[Color.WHITE][Sq.E2], 0)
        self.assertEqual(board.bitboards[Piece.WP][Sq.E4], 1)
        self.assertEqual(board.color_bb[Color.WHITE][Sq.E4], 1)
        self.assertEqual(board.turn, Color.BLACK)
        self.assertEqual(board.castling[Piece.WK], True)
        self.assertEqual(board.castling[Piece.WQ], True)
        self.assertEqual(board.castling[Piece.BK], True)
        self.assertEqual(board.castling[Piece.BQ], True)
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
        self.assertEqual(board.castling[Piece.WK], False)
        self.assertEqual(board.castling[Piece.WQ], False)
        self.assertEqual(board.castling[Piece.BK], False)
        self.assertEqual(board.castling[Piece.BQ], False)
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

        board.fen('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 10 30')
        assert board.turn == Color.WHITE
        assert not board.castling[Piece.WK]
        assert not board.castling[Piece.WQ]
        assert not board.castling[Piece.BK]
        assert not board.castling[Piece.BQ]
        assert board.ep_square == -1
        assert board.half_move_clock == 10
        assert board.full_move_count == 30
        assert sorted(board.piece_sq[Piece.WP]) == sorted([Sq.B5, Sq.E2, Sq.G2])
        assert sorted(board.piece_sq[Piece.WP]) == sorted([Sq.B5, Sq.E2, Sq.G2])
        assert len(board.piece_sq[Piece.WN]) == 0
        assert len(board.piece_sq[Piece.WB]) == 0
        assert sorted(board.piece_sq[Piece.WR]) == sorted([Sq.B4])
        assert len(board.piece_sq[Piece.WQ]) == 0
        assert sorted(board.piece_sq[Piece.WK]) == sorted([Sq.A5])
        assert sorted(board.piece_sq[Piece.BP]) == sorted([Sq.C7, Sq.D6, Sq.F4])
        assert len(board.piece_sq[Piece.BN]) == 0
        assert len(board.piece_sq[Piece.BB]) == 0
        assert sorted(board.piece_sq[Piece.BR]) == sorted([Sq.H5])
        assert len(board.piece_sq[Piece.BQ]) == 0
        assert sorted(board.piece_sq[Piece.BK]) == sorted([Sq.H4])

    def test_get_piece_on_sq(self):
        """
        Tests the _get_piece_on_sq() function of the Board class
        """
        board = Board()
        self.assertEqual(board._get_piece_on_sq(Sq.A1), Piece.WR)
        self.assertEqual(board._get_piece_on_sq(Sq.B1), Piece.WN)
        self.assertEqual(board._get_piece_on_sq(Sq.C1), Piece.WB)
        self.assertEqual(board._get_piece_on_sq(Sq.D1), Piece.WQ)
        self.assertEqual(board._get_piece_on_sq(Sq.E1), Piece.WK)
        self.assertEqual(board._get_piece_on_sq(Sq.F1), Piece.WB)
        self.assertEqual(board._get_piece_on_sq(Sq.G1), Piece.WN)
        self.assertEqual(board._get_piece_on_sq(Sq.H1), Piece.WR)
        self.assertEqual(board._get_piece_on_sq(Sq.A8), Piece.BR)
        self.assertEqual(board._get_piece_on_sq(Sq.B8), Piece.BN)
        self.assertEqual(board._get_piece_on_sq(Sq.C8), Piece.BB)
        self.assertEqual(board._get_piece_on_sq(Sq.D8), Piece.BQ)
        self.assertEqual(board._get_piece_on_sq(Sq.E8), Piece.BK)
        self.assertEqual(board._get_piece_on_sq(Sq.F8), Piece.BB)
        self.assertEqual(board._get_piece_on_sq(Sq.G8), Piece.BN)
        self.assertEqual(board._get_piece_on_sq(Sq.H8), Piece.BR)
        self.assertEqual(board._get_piece_on_sq(Sq.A2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.B2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.C2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.D2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.E2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.F2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.G2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.H2), Piece.WP)
        self.assertEqual(board._get_piece_on_sq(Sq.A7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.B7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.C7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.D7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.E7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.F7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.G7), Piece.BP)
        self.assertEqual(board._get_piece_on_sq(Sq.H7), Piece.BP)

    def test_get_sqs_between(self):
        """
        Tests the _get_sqs_between() function of the Board class
        """
        # horizontal direction
        self.assertEqual(sorted(Board._get_sqs_between(Sq.A1, Sq.A8).indices()),
                         sorted([Sq.A2, Sq.A3, Sq.A4, Sq.A5, Sq.A6, Sq.A7]))

        # vertical direction
        self.assertEqual(sorted(Board._get_sqs_between(Sq.C3, Sq.C5).indices()),
                         sorted([Sq.C4]))

        # diagonal (UL-DR) direction
        self.assertEqual(sorted(Board._get_sqs_between(Sq.B7, Sq.G2).indices()),
                         sorted([Sq.C6, Sq.D5, Sq.E4, Sq.F3]))

        # diagonal (UR-DL) direction
        self.assertEqual(sorted(Board._get_sqs_between(Sq.D2, Sq.F4).indices()),
                         sorted([Sq.E3]))

    def test_make_move(self):
        """
        Tests the make_move() function of the Board class
        """
        board = Board()
        move = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        captured_piece, castling, ep_square, half_move_clock, = board.make_move(move)
        self.assertEqual(captured_piece, -1)
        self.assertEqual(castling[Piece.WK], True)
        self.assertEqual(castling[Piece.WQ], True)
        self.assertEqual(castling[Piece.BK], True)
        self.assertEqual(castling[Piece.BQ], True)
        self.assertEqual(ep_square, -1)
        self.assertEqual(half_move_clock, 0)
        self.assertEqual(board.fen(), 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('00001000000000001111011111111111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1111111111111111000000000000000000000000000000000000000000000000', 2))
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
        captured_piece, castling, ep_square, half_move_clock, = board.make_move(move)
        self.assertEqual(captured_piece, -1)
        self.assertEqual(castling[Piece.WK], True)
        self.assertEqual(castling[Piece.WQ], True)
        self.assertEqual(castling[Piece.BK], True)
        self.assertEqual(castling[Piece.BQ], True)
        self.assertEqual(ep_square, Sq.E3)
        self.assertEqual(half_move_clock, 0)
        self.assertEqual(board.fen(), 'r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('00001000000000001111011111111111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1011111111111111001000000000000000000000000000000000000000000000', 2))
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
        captured_piece, castling, ep_square, half_move_clock, = board.make_move(move)
        self.assertEqual(captured_piece, -1)
        self.assertEqual(castling[Piece.WK], True)
        self.assertEqual(castling[Piece.WQ], True)
        self.assertEqual(castling[Piece.BK], True)
        self.assertEqual(castling[Piece.BQ], True)
        self.assertEqual(ep_square, -1)
        self.assertEqual(half_move_clock, 1)
        self.assertEqual(board.fen(), 'r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPPKPPP/RNBQ1BNR b kq - 2 2')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('00001000000000001111111111110111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1011111111111111001000000000000000000000000000000000000000000000', 2))
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
        captured_piece, castling, ep_square, half_move_clock, = board.make_move(move)
        self.assertEqual(captured_piece, Piece.BP)
        self.assertEqual(castling[Piece.WK], False)
        self.assertEqual(castling[Piece.WQ], False)
        self.assertEqual(castling[Piece.BK], False)
        self.assertEqual(castling[Piece.BQ], False)
        self.assertEqual(ep_square, -1)
        self.assertEqual(half_move_clock, 0)
        self.assertEqual(board.fen(), 'rnbqkbnr/ppp1pppp/8/3P4/8/8/PPPP1PPP/RNBQKBNR b - - 0 2')
        self.assertEqual(board.color_bb[Color.WHITE].num, int('0001000000000000000000001111011111111111', 2))
        self.assertEqual(board.color_bb[Color.BLACK].num,
                         int('1111111111101111000000000000000000000000000000000000000000000000', 2))
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

        # MoveType.N_PROMO
        board.fen('k7/7P/8/8/8/8/8/n6K w - - 0 1')
        move = Move(Sq.H7, Sq.H8, MoveType.N_PROMO)
        captured_piece, castling, ep_square, half_move_clock, = board.make_move(move)
        assert captured_piece == -1
        assert not castling[Piece.WK]
        assert not castling[Piece.WQ]
        assert not castling[Piece.BK]
        assert not castling[Piece.BQ]
        assert ep_square == -1
        assert half_move_clock == 0
        assert board.fen() == 'k6N/8/8/8/8/8/8/n6K b - - 0 1'
        assert board.color_bb[Color.WHITE].num == int('00000001'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000001', 2)
        assert board.color_bb[Color.BLACK].num == int('10000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '10000000', 2)
        assert len(board.piece_sq[Piece.WP]) == 0
        assert sorted(board.piece_sq[Piece.WN]) == sorted([Sq.H8])
        assert len(board.piece_sq[Piece.WB]) == 0
        assert len(board.piece_sq[Piece.WR]) == 0
        assert len(board.piece_sq[Piece.WQ]) == 0
        assert sorted(board.piece_sq[Piece.WK]) == sorted([Sq.H1])
        assert len(board.piece_sq[Piece.BP]) == 0
        assert sorted(board.piece_sq[Piece.BN]) == sorted([Sq.A1])
        assert len(board.piece_sq[Piece.BB]) == 0
        assert len(board.piece_sq[Piece.BR]) == 0
        assert len(board.piece_sq[Piece.BQ]) == 0
        assert sorted(board.piece_sq[Piece.BK]) == sorted([Sq.A8])

        # MoveType.N_PROMO_CAPTURE
        board.fen('k5n1/7P/8/8/8/8/8/n6K w - - 0 1')
        move = Move(Sq.H7, Sq.G8, MoveType.N_PROMO_CAPTURE)
        captured_piece, castling, ep_square, half_move_clock, = board.make_move(move)
        assert captured_piece == Piece.BN
        assert not castling[Piece.WK]
        assert not castling[Piece.WQ]
        assert not castling[Piece.BK]
        assert not castling[Piece.BQ]
        assert ep_square == -1
        assert half_move_clock == 0
        assert board.fen() == 'k5N1/8/8/8/8/8/8/n6K b - - 0 1'
        assert board.color_bb[Color.WHITE].num == int('00000010'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000001', 2)
        assert board.color_bb[Color.BLACK].num == int('10000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '00000000'
                                                      '10000000', 2)
        assert len(board.piece_sq[Piece.WP]) == 0
        assert sorted(board.piece_sq[Piece.WN]) == sorted([Sq.G8])
        assert len(board.piece_sq[Piece.WB]) == 0
        assert len(board.piece_sq[Piece.WR]) == 0
        assert len(board.piece_sq[Piece.WQ]) == 0
        assert sorted(board.piece_sq[Piece.WK]) == sorted([Sq.H1])
        assert len(board.piece_sq[Piece.BP]) == 0
        assert sorted(board.piece_sq[Piece.BN]) == sorted([Sq.A1])
        assert len(board.piece_sq[Piece.BB]) == 0
        assert len(board.piece_sq[Piece.BR]) == 0
        assert len(board.piece_sq[Piece.BQ]) == 0
        assert sorted(board.piece_sq[Piece.BK]) == sorted([Sq.A8])

        # TODO add more tests (X_PROMO, X_PROMO_CAPTURE, EP_CAPTURE, X_CASTLE)


    def test_undo_move(self):
        """
        Tests the undo_move() function of the Board class
        """
        # make and undo a quiet move
        board = Board()
        move = Move(Sq.D2, Sq.D3, MoveType.QUIET)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == Board().fen()

        # make and undo a double pawn push move
        board = Board()
        move = Move(Sq.E2, Sq.E4, MoveType.DOUBLE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == Board().fen()

        # make and undo a kingside castling
        board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq - 0 1')
        move = Move(Sq.E1, Sq.G1, MoveType.K_CASTLE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq - 0 1'

        # make and undo a queenside castling
        board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq - 0 1')
        move = Move(Sq.E1, Sq.C1, MoveType.Q_CASTLE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq - 0 1'

        # make and undo a capture
        board = Board('rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w - - 0 2')
        move = Move(Sq.E4, Sq.D5, MoveType.CAPTURE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w - - 0 2'

        # make and undo an en passant capture
        board = Board('rnbqkbnr/ppp1pppp/8/8/3pP3/8/PPPP1PPP/RNBQKBNR b - e3 0 1')
        move = Move(Sq.D4, Sq.E3, MoveType.EP_CAPTURE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'rnbqkbnr/ppp1pppp/8/8/3pP3/8/PPPP1PPP/RNBQKBNR b - e3 0 1'

        # make and undo a promotion to knight
        board = Board('k7/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.H8, MoveType.N_PROMO)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k7/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion to bishop
        board = Board('k7/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.H8, MoveType.B_PROMO)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k7/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion to rook
        board = Board('k7/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.H8, MoveType.R_PROMO)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k7/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion to queen
        board = Board('k7/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.H8, MoveType.Q_PROMO)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k7/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion capture to knight
        board = Board('k5p1/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.G8, MoveType.N_PROMO_CAPTURE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k5p1/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion capture to bishop
        board = Board('k5p1/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.G8, MoveType.B_PROMO_CAPTURE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k5p1/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion capture to rook
        board = Board('k5p1/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.G8, MoveType.R_PROMO_CAPTURE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k5p1/7P/8/pp6/8/8/8/7K w - - 0 10'

        # make and undo a promotion capture to queen
        board = Board('k5p1/7P/8/pp6/8/8/8/7K w - - 0 10')
        move = Move(Sq.H7, Sq.G8, MoveType.Q_PROMO_CAPTURE)
        captured_piece, castling, ep_square, half_move_clock = board.make_move(move)
        board.undo_move(move, captured_piece, castling, ep_square, half_move_clock)
        assert board.fen() == 'k5p1/7P/8/pp6/8/8/8/7K w - - 0 10'

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
        print(board)
        self.assertEqual(len(moves), 6)

        board.fen('rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8')
        moves = board.move_gen()
        self.assertEqual(len(moves), 44)

        board.fen('r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10')
        moves = board.move_gen()
        self.assertEqual(len(moves), 46)

    def test_get_target_noncapture_moves(self):
        """
        Tests the get_target_noncapture_moves() function of the Board class
        """
        # no target
        board = Board()
        target_bb = BitBoard(0)
        moves = board.get_target_noncapture_moves(target_bb)
        assert len(moves) == 0

        # one target square, one move - pawn quiet move
        board = Board('k7/pp6/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
        target_bb = BitBoard(0)
        target_bb[Sq.G3] = 1
        moves = board.get_target_noncapture_moves(target_bb)
        assert len(moves) == 1
        assert sorted(moves) == sorted([Move(Sq.G2, Sq.G3, MoveType.QUIET)])

        # one target square, one move - pawn double pawn push
        board = Board('k7/pp6/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
        target_bb = BitBoard(0)
        target_bb[Sq.H4] = 1
        moves = board.get_target_noncapture_moves(target_bb)
        assert len(moves) == 1
        assert sorted(moves) == sorted([Move(Sq.H2, Sq.H4, MoveType.DOUBLE)])

        # one target square, two moves - pawn quiet move and knight
        board = Board('k7/pp6/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
        target_bb = BitBoard(0)
        target_bb[Sq.H3] = 1
        moves = board.get_target_noncapture_moves(target_bb)
        assert len(moves) == 2
        assert sorted(moves) == sorted([Move(Sq.H2, Sq.H3, MoveType.QUIET), Move(Sq.G1, Sq.H3, MoveType.QUIET)])

        # two target squares, three moves
        board = Board('k7/pp6/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
        target_bb = BitBoard(0)
        target_bb[Sq.H3] = 1
        target_bb[Sq.E4] = 1
        moves = board.get_target_noncapture_moves(target_bb)
        assert len(moves) == 3
        assert sorted(moves) == sorted([Move(Sq.E2, Sq.E4, MoveType.DOUBLE),
                                        Move(Sq.H2, Sq.H3, MoveType.QUIET),
                                        Move(Sq.G1, Sq.H3, MoveType.QUIET)])

    def test_get_attacking_sqs(self):
        """
        Tests the get_attacking_sqs() function of the Board class
        """
        # no checks
        board = Board()
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        check_sqs = board.get_attacking_sqs(king_sq)
        self.assertEqual(len(check_sqs), 0)

        # single check
        board = Board('4K2k/8/5B2/8/8/8/8/1n6 b - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        check_sqs = board.get_attacking_sqs(king_sq)
        self.assertEqual(len(check_sqs), 1)
        self.assertListEqual(sorted(check_sqs), sorted([Sq.F6]))

        # multiple checks
        board = Board('7k/8/8/8/7r/8/5n2/7K w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        check_sqs = board.get_attacking_sqs(king_sq)
        self.assertEqual(len(check_sqs), 2)
        self.assertListEqual(sorted(check_sqs), sorted([Sq.H4, Sq.F2]))

    def test_get_attacking_pawn_sqs(self):
        """
        Tests the _get_attacking_pawn_sqs() function of the Board class
        """
        # normal
        board = Board('7k/8/8/8/6p1/7K/8/8 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        pawn_sqs = board._get_attacking_pawn_sqs(king_sq)
        self.assertEqual(len(pawn_sqs), 1)
        self.assertListEqual(sorted(pawn_sqs), sorted([Sq.G4]))

        # no check
        board = Board('7k/8/8/8/p6p/7K/8/8 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        pawn_sqs = board._get_attacking_pawn_sqs(king_sq)
        self.assertEqual(len(pawn_sqs), 0)

        # double check
        # not possible in actual game of chess
        board = Board('7K/8/8/8/8/4k3/3P1P2/8 b - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        pawn_sqs = board._get_attacking_pawn_sqs(king_sq)
        self.assertEqual(len(pawn_sqs), 2)
        self.assertListEqual(sorted(pawn_sqs), sorted([Sq.D2, Sq.F2]))

        # pawn on 2nd/7th row (promotion)
        board = Board('7k/8/8/8/8/8/3p4/4K3 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        pawn_sqs = board._get_attacking_pawn_sqs(king_sq)
        self.assertEqual(len(pawn_sqs), 1)
        self.assertListEqual(sorted(pawn_sqs), sorted([Sq.D2]))

    def test_get_attacking_knight_sqs(self):
        """
        Tests the _get_attacking_knight_sqs() function of the Board class
        """
        # normal
        board = Board('7k/8/8/8/5n2/7K/8/8 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        knight_sqs = board._get_attacking_knight_sqs(king_sq)
        self.assertEqual(len(knight_sqs), 1)
        self.assertListEqual(sorted(knight_sqs), sorted([Sq.F4]))

        # no check
        board = Board('nn6/8/8/8/8/7K/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        knight_sqs = board._get_attacking_knight_sqs(king_sq)
        self.assertEqual(len(knight_sqs), 0)

        # double check
        # not possible in actual game of chess
        board = Board('7K/8/8/8/8/4k3/8/3N1N2 b - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        knight_sqs = board._get_attacking_knight_sqs(king_sq)
        self.assertEqual(len(knight_sqs), 2)
        self.assertListEqual(sorted(knight_sqs), sorted([Sq.D1, Sq.F1]))

    def test_get_attacking_bishop_sqs(self):
        """
        Tests the _get_attacking_bishop_sqs() function of the Board class
        """
        # normal
        board = Board('7k/8/8/8/6b1/7K/8/8 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        bishop_sqs = board._get_attacking_bishop_sqs(king_sq)
        self.assertEqual(len(bishop_sqs), 1)
        self.assertListEqual(sorted(bishop_sqs), sorted([Sq.G4]))

        # no check
        board = Board('6bb/8/8/8/8/7K/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        bishop_sqs = board._get_attacking_bishop_sqs(king_sq)
        self.assertEqual(len(bishop_sqs), 0)

        # no check (covered)
        board = Board('8/8/8/5b2/6N1/7K/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        bishop_sqs = board._get_attacking_bishop_sqs(king_sq)
        self.assertEqual(len(bishop_sqs), 0)

        # double check
        # not possible in actual game of chess
        board = Board('7K/8/8/8/8/4k3/3B4/6B1 b - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        bishop_sqs = board._get_attacking_bishop_sqs(king_sq)
        self.assertEqual(len(bishop_sqs), 2)
        self.assertListEqual(sorted(bishop_sqs), sorted([Sq.D2, Sq.G1]))

    def test_get_attacking_rook_sqs(self):
        """
        Tests the _get_attacking_rook_sqs() function of the Board class
        """
        # normal
        board = Board('7k/8/8/7r/8/7K/8/8 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        rook_sqs = board._get_attacking_rook_sqs(king_sq)
        self.assertEqual(len(rook_sqs), 1)
        self.assertListEqual(sorted(rook_sqs), sorted([Sq.H5]))

        # no check
        board = Board('6r1/8/8/8/8/7K/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        rook_sqs = board._get_attacking_rook_sqs(king_sq)
        self.assertEqual(len(rook_sqs), 0)

        # no check (covered)
        board = Board('8/8/8/5b2/6N1/5rnK/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        rook_sqs = board._get_attacking_rook_sqs(king_sq)
        self.assertEqual(len(rook_sqs), 0)

        # double check
        # not possible in actual game of chess
        board = Board('7K/8/8/4R3/8/2R1k3/3B4/6B1 b - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        rook_sqs = board._get_attacking_rook_sqs(king_sq)
        self.assertEqual(len(rook_sqs), 2)
        self.assertListEqual(sorted(rook_sqs), sorted([Sq.E5, Sq.C3]))

    def test_get_attacking_queen_sqs(self):
        """
        Tests the _get_attacking_queen_sqs() function of the Board class
        """
        # normal
        board = Board('7k/8/7q/8/8/7K/8/8 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        queen_sqs = board._get_attacking_queen_sqs(king_sq)
        self.assertEqual(len(queen_sqs), 1)
        self.assertListEqual(sorted(queen_sqs), sorted([Sq.H6]))

        # no check
        board = Board('5q1Q/8/8/8/8/7K/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        queen_sqs = board._get_attacking_queen_sqs(king_sq)
        self.assertEqual(len(queen_sqs), 0)

        # no check (covered)
        board = Board('8/8/8/5b2/q2N3K/8/8/3k4 w - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        queen_sqs = board._get_attacking_queen_sqs(king_sq)
        self.assertEqual(len(queen_sqs), 0)

        # triple check
        # not possible in actual game of chess
        board = Board('7K/8/6Q1/5n2/8/3Q2k1/7Q/6b1 b - - 0 1')
        king = Piece.WK if board.turn == Color.WHITE else Piece.BK
        king_sq = board.piece_sq[king][0]
        queen_sqs = board._get_attacking_queen_sqs(king_sq)
        self.assertEqual(len(queen_sqs), 3)
        self.assertListEqual(sorted(queen_sqs), sorted([Sq.H2, Sq.D3, Sq.G6]))

    def test_find_pinned(self):
        """
        Tests the _find_pinned() function of the Board class
        """
        # pinned by bishop
        board = Board('k6K/1p6/8/8/8/8/8/7B b - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 1)
        self.assertEqual(sorted(pinned[0]), sorted([Sq.B7]))
        self.assertEqual(len(pinned[1]), 0)

        # pinned by rook
        board = Board('k6K/8/8/n7/8/8/8/R7 b - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 1)
        self.assertEqual(sorted(pinned[0]), sorted([Sq.A5]))
        self.assertEqual(len(pinned[1]), 0)

        # pinned by queen
        board = Board('k6K/1p6/8/8/8/5Q2/8/8 b - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 1)
        self.assertEqual(sorted(pinned[0]), sorted([Sq.B7]))
        self.assertEqual(len(pinned[1]), 0)

        # no pinned piece (no slider on trajectory)
        board = Board('k6K/1p6/8/2r5/8/3b4/8/8 w - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 0)
        self.assertEqual(len(pinned[1]), 0)

        # no pinned piece (multiple allied piece on slider trajectory)
        board = Board('K6k/1N6/8/3P4/4q3/8/8/8 w - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 0)
        self.assertEqual(len(pinned[1]), 0)

        # no pinned piece (enemy piece on slider trajectory)
        board = Board('q3k3/8/2n5/3K4/8/8/8/7B w - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 0)
        self.assertEqual(len(pinned[1]), 0)

        # no pinned piece, piece in trajectory but further than king
        board = Board('1q5k/8/8/8/8/6K1/7R/8 w - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 0)
        self.assertEqual(len(pinned[1]), 0)

        # one pinned, piece in trajectory but further than king
        board = Board('q6k/8/8/8/4P3/5K2/8/7B w - - 0 1')
        pinned = board.find_pinned()
        self.assertEqual(len(pinned[0]), 1)
        self.assertEqual(sorted(pinned[0]), sorted([Sq.E4]))
        self.assertEqual(len(pinned[1]), 0)

        # multiple pinned pieces
        board = Board('1q1k4/2R5/8/rN2K3/8/8/8/8 w - - 0 1')
        pinned = board.find_pinned()
        print(board)
        self.assertEqual(len(pinned[0]), 2)
        self.assertEqual(sorted(pinned[0]), sorted([Sq.C7, Sq.B5]))
        self.assertEqual(len(pinned[1]), 0)

    def test_pinned_move_gen(self):
        """
        Tests the _pinned_move_gen() function of the Board class
        """
        # pawn pinned by rook
        board = Board('k6K/8/8/8/8/p7/8/R7 b - - 0 1')
        moves = board._pinned_move_gen(Sq.A3, Sq.A1, Direction.U)
        self.assertEqual(len(moves), 0)

        # knight pinned by rook
        board = Board('k6K/8/8/8/8/n7/8/R7 b - - 0 1')
        moves = board._pinned_move_gen(Sq.A3, Sq.A1, Direction.U)
        self.assertEqual(len(moves), 0)

        # bishop pinned by rook
        board = Board('k6K/8/8/8/b7/8/8/R7 b - - 0 1')
        moves = board._pinned_move_gen(Sq.A4, Sq.A1, Direction.U)
        self.assertEqual(len(moves), 0)

        # rook pinned by rook
        board = Board('k6K/8/8/8/8/r7/8/R7 b - - 0 1')
        moves = board._pinned_move_gen(Sq.A3, Sq.A1, Direction.U)
        self.assertEqual(len(moves), 1)
        self.assertEqual(sorted(moves), [Move(Sq.A3, Sq.A1, MoveType.CAPTURE)])

        # queen pinned by rook
        board = Board('k6K/8/8/8/8/q7/8/R7 b - - 0 1')
        moves = board._pinned_move_gen(Sq.A3, Sq.A1, Direction.U)
        self.assertEqual(len(moves), 1)
        self.assertEqual(sorted(moves), [Move(Sq.A3, Sq.A1, MoveType.CAPTURE)])

        # pawn pinned by bishop
        board = Board('K6k/8/8/8/8/2p5/1B6/8 b - - 0 1')
        moves = board._pinned_move_gen(Sq.C3, Sq.B2, Direction.UR)
        self.assertEqual(len(moves), 1)
        self.assertEqual(sorted(moves), [Move(Sq.C3, Sq.B2, MoveType.CAPTURE)])

        # pawn pinned by bishop (promo attack)
        board = Board('K6k/6N1/8/8/8/8/2p5/1B6 b - - 0 1')
        moves = board._pinned_move_gen(Sq.C2, Sq.B1, Direction.UR)
        self.assertEqual(len(moves), 4)
        self.assertEqual(sorted(moves), [Move(Sq.C2, Sq.B1, MoveType.N_PROMO_CAPTURE),
                                         Move(Sq.C2, Sq.B1, MoveType.B_PROMO_CAPTURE),
                                         Move(Sq.C2, Sq.B1, MoveType.R_PROMO_CAPTURE),
                                         Move(Sq.C2, Sq.B1, MoveType.Q_PROMO_CAPTURE)])

        # knight pinned by bishop
        board = Board('k6K/6N1/8/8/8/8/1b6/8 w - - 0 1')
        moves = board._pinned_move_gen(Sq.G7, Sq.B2, Direction.UR)
        self.assertEqual(len(moves), 0)

        # bishop pinned by bishop
        board = Board('k6K/6B1/8/8/8/8/1b6/8 w - - 0 1')
        moves = board._pinned_move_gen(Sq.G7, Sq.B2, Direction.UR)
        self.assertEqual(len(moves), 1)
        self.assertEqual(sorted(moves), [Move(Sq.G7, Sq.B2, MoveType.CAPTURE)])

        # rook pinned by bishop
        board = Board('k6K/6R1/8/8/8/8/1b6/8 w - - 0 1')
        moves = board._pinned_move_gen(Sq.G7, Sq.B2, Direction.UR)
        self.assertEqual(len(moves), 0)

        # queen pinned by bishop
        board = Board('k6K/8/5Q2/8/8/8/1b6/8 w - - 0 1')
        moves = board._pinned_move_gen(Sq.F6, Sq.B2, Direction.UR)
        self.assertEqual(len(moves), 1)
        self.assertEqual(sorted(moves), [Move(Sq.F6, Sq.B2, MoveType.CAPTURE)])

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

        # test for optional parameter pinned_sqs
        board = Board('k7/8/2q5/8/4P3/8/8/7K w - - 0 1')
        pinned_sqs = [Sq.E4]
        pawn_moves = board._pawn_move_gen(pinned_sqs)
        self.assertEqual(len(pawn_moves), 0)

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

        # test for optional parameter pinned_sqs
        board = Board('k7/8/2q5/8/8/5N2/8/7K w - - 0 1')
        pinned_sqs = [Sq.F3]
        knight_moves = board._knight_move_gen(pinned_sqs)
        self.assertEqual(len(knight_moves), 0)

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

        # test for optional parameter pinned_sqs
        board = Board('k7/8/2q5/8/8/5N2/8/r2B3K w - - 0 1')
        pinned_sqs = [Sq.D1]
        bishop_moves = board._bishop_move_gen(pinned_sqs)
        self.assertEqual(len(bishop_moves), 0)

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

        # test for optional parameter pinned_sqs
        board = Board('k7/1b6/8/8/8/5R2/8/7K w - - 0 1')
        pinned_sqs = [Sq.F3]
        rook_moves = board._rook_move_gen(pinned_sqs)
        self.assertEqual(len(rook_moves), 0)

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

        # test for optional parameter pinned_sqs
        # note that the move capturing the pinning piece is not generated in this function, but in the
        # Board._pinned_move_gen()
        board = Board('k7/8/8/8/8/8/8/1r4QK w - - 0 1')
        pinned_sqs = [Sq.G1]
        queen_moves = board._queen_move_gen(pinned_sqs)
        self.assertEqual(len(queen_moves), 0)

    def test_king_move_gen(self):
        """
        Tests the king_move_gen() function of the Board class
        """
        board = Board()
        king_moves = board._king_move_gen()
        self.assertEqual(len(king_moves), 0)

        # 3 pseudolegal moves, 2 legal moves
        board = Board('k7/8/8/8/8/6p1/8/6nK w - - 0 1')
        king_moves = board._king_move_gen()
        self.assertEqual(len(king_moves), 2)
        self.assertListEqual(sorted(king_moves), sorted([Move(Sq.H1, Sq.G2, MoveType.QUIET),
                                                         Move(Sq.H1, Sq.G1, MoveType.CAPTURE)]))

        # 7 pseudolegal moves, 5 legal moves
        board = Board('8/8/8/3kb3/3N4/8/8/6nK b - - 0 1')
        print()
        print(board)
        king_moves = board._king_move_gen()
        self.assertEqual(len(king_moves), 5)
        self.assertListEqual(sorted(king_moves), sorted([Move(Sq.D5, Sq.C4, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.C5, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.D6, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.E4, MoveType.QUIET),
                                                         Move(Sq.D5, Sq.D4, MoveType.CAPTURE)]))

    def test_castling_move_gen(self):
        """
        Tests the castling_move_gen() function of the Board class
        """
        # all castling possible
        board = Board('k7/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 2)
        self.assertListEqual(sorted(moves), sorted([Move(Sq.E1, Sq.C1, MoveType.Q_CASTLE),
                                                    Move(Sq.E1, Sq.G1, MoveType.K_CASTLE)]))
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 2)
        self.assertListEqual(sorted(moves), sorted([Move(Sq.E8, Sq.C8, MoveType.Q_CASTLE),
                                                    Move(Sq.E8, Sq.G8, MoveType.K_CASTLE)]))

        # one castling blocked by allied piece
        board = Board('k7/8/8/8/8/8/8/R2BK2R w KQkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 1)
        self.assertListEqual(sorted(moves), sorted([Move(Sq.E1, Sq.G1, MoveType.K_CASTLE)]))

        # one castling blocked by "rook moving"
        board = Board('k7/8/8/8/8/8/8/R3K2R w Qkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 1)
        self.assertListEqual(sorted(moves), sorted([Move(Sq.E1, Sq.C1, MoveType.Q_CASTLE)]))

        # both castling blocked by "king moving"
        board = Board('k7/8/8/8/8/8/8/R3K2R w kq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 0)

        # castling not allowed due to king on check
        board = Board('k7/8/8/8/8/4r3/8/R3K2R w KQkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 0)

        # one castling not allowed due to check while castling
        board = Board('k7/8/8/8/8/3r4/8/R3K2R w KQkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 1)
        self.assertListEqual(sorted(moves), sorted([Move(Sq.E1, Sq.G1, MoveType.K_CASTLE)]))

        # one castling not allowed due to check after castling
        board = Board('k7/8/8/8/8/2r5/8/R3K2R w KQkq - 0 1')
        moves = board._castling_move_gen()
        self.assertEqual(len(moves), 1)
        self.assertListEqual(sorted(moves), sorted([Move(Sq.E1, Sq.G1, MoveType.K_CASTLE)]))

    def test_get_safe_bb(self):
        """
        Tests the _get_safe_bb() function of the Board class
        """
        # just king
        board = Board('k7/8/8/8/8/8/8/7K w - - 0 1')
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.B7, Sq.B8, Sq.A7]))

        # king and pawn
        board = Board('k7/7p/8/8/8/8/8/7K w - - 0 1')
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.B7, Sq.B8, Sq.A7, Sq.G6]))

        # king and knight
        board = Board('k5n1/8/8/8/8/8/8/7K w - - 0 1')
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.B7, Sq.B8, Sq.A7, Sq.E7, Sq.F6, Sq.H6]))

        # king and bishop
        board = Board('k4b2/8/8/8/8/8/8/7K w - - 0 1')
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.B7, Sq.B8, Sq.A7, Sq.E7, Sq.D6, Sq.C5, Sq.B4, Sq.A3,
                                                               Sq.G7, Sq.H6]))

        # king and rook
        board = Board('k7/8/8/8/8/8/8/4K2R b - - 0 1')
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.H2, Sq.H3, Sq.H4, Sq.H5, Sq.H6, Sq.H7, Sq.H8, Sq.G1,
                                                               Sq.F1, Sq.F2, Sq.E1, Sq.E2, Sq.D2, Sq.D1]))

        # king and queen
        board = Board('k7/8/8/8/8/8/8/4KQ2 b - - 0 1')
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.F2, Sq.F3, Sq.F4, Sq.F5, Sq.F6, Sq.F7, Sq.F8,
                                                               Sq.E2, Sq.D3, Sq.C4, Sq.B5, Sq.A6,
                                                               Sq.G1, Sq.H1, Sq.G2, Sq.H3, Sq.D1, Sq.D2, Sq.F1, Sq.E1]))

        # starting position
        board = Board()
        safe_bb = board._get_safe_bb()
        self.assertEqual(sorted((~safe_bb).indices()), sorted([Sq.B8, Sq.C8, Sq.D8, Sq.E8, Sq.F8, Sq.G8,
                                                               Sq.A7, Sq.B7, Sq.C7, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7,
                                                               Sq.A6, Sq.B6, Sq.C6, Sq.D6, Sq.E6, Sq.F6, Sq.G6, Sq.H6]))

    def test_eval(self):
        """
        Tests the test_eval() function of the Board class
        """
        # starting position
        board = Board()
        assert board.eval() == 0

        # after 1. e4
        board.make_move(Move(Sq.E2, Sq.E4, MoveType.DOUBLE))
        # note that make_move() also changes the turn
        assert board.eval() == -(const.PCSQ_VALUE[Piece.WP][Sq.E4] - const.PCSQ_VALUE[Piece.WP][Sq.E2])
        # after 1. e4 - d5
        board.make_move(Move(Sq.D7, Sq.D5, MoveType.DOUBLE))
        assert board.eval() == (const.PCSQ_VALUE[Piece.WP][Sq.E4] - const.PCSQ_VALUE[Piece.WP][Sq.E2]) + \
               (const.PCSQ_VALUE[Piece.BP][Sq.D5] - const.PCSQ_VALUE[Piece.BP][Sq.D7])


        # no piece
        board = Board('8/8/8/8/8/8/8/8 w - - 0 1')
        assert board.eval() == 0

        # white pawn
        board = Board('8/8/8/8/8/8/7P/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.WP] + const.PCSQ_VALUE[Piece.WP][Sq.H2]
        board = Board('8/8/8/8/8/8/7P/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.WP] + const.PCSQ_VALUE[Piece.WP][Sq.H2])

        # black pawn
        board = Board('8/3p4/8/8/8/8/8/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.BP] + const.PCSQ_VALUE[Piece.BP][Sq.D7]
        board = Board('8/3p4/8/8/8/8/8/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.BP] + const.PCSQ_VALUE[Piece.BP][Sq.D7])

        # white knight
        board = Board('8/8/8/8/8/8/8/1N6 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.WN] + const.PCSQ_VALUE[Piece.WN][Sq.B1]
        board = Board('8/8/8/8/8/8/8/1N6 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.WN] + const.PCSQ_VALUE[Piece.WN][Sq.B1])

        # black knight
        board = Board('8/8/8/8/2n5/8/8/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.BN] + const.PCSQ_VALUE[Piece.BN][Sq.C4]
        board = Board('8/8/8/8/2n5/8/8/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.BN] + const.PCSQ_VALUE[Piece.BN][Sq.C4])

        # white bishop
        board = Board('8/8/8/8/8/8/6B1/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.WB] + const.PCSQ_VALUE[Piece.WB][Sq.G2]
        board = Board('8/8/8/8/8/8/6B1/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.WB] + const.PCSQ_VALUE[Piece.WB][Sq.G2])

        # black bishop
        board = Board('6b1/8/8/8/8/8/8/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.BB] + const.PCSQ_VALUE[Piece.BB][Sq.G8]
        board = Board('6b1/8/8/8/8/8/8/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.BB] + const.PCSQ_VALUE[Piece.BB][Sq.G8])

        # white rook
        board = Board('8/8/8/8/8/8/8/R7 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.WR] + const.PCSQ_VALUE[Piece.WR][Sq.A1]
        board = Board('8/8/8/8/8/8/8/R7 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.WR] + const.PCSQ_VALUE[Piece.WR][Sq.A1])

        # black rook
        board = Board('8/7r/8/8/8/8/8/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.BR] + const.PCSQ_VALUE[Piece.BR][Sq.H7]
        board = Board('8/7r/8/8/8/8/8/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.BR] + const.PCSQ_VALUE[Piece.BR][Sq.H7])

        # white queen
        board = Board('8/8/8/8/8/8/2Q5/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.WQ] + const.PCSQ_VALUE[Piece.WQ][Sq.C2]
        board = Board('8/8/8/8/8/8/2Q5/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.WQ] + const.PCSQ_VALUE[Piece.WQ][Sq.C2])

        # black queen
        board = Board('3q4/8/8/8/8/8/8/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.BQ] + const.PCSQ_VALUE[Piece.BQ][Sq.D8]
        board = Board('3q4/8/8/8/8/8/8/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.BQ] + const.PCSQ_VALUE[Piece.BQ][Sq.D8])

        # white king
        board = Board('8/8/8/8/8/8/8/4K3 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.WK] + const.PCSQ_VALUE[Piece.WK][Sq.E1]
        board = Board('8/8/8/8/8/8/8/4K3 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.WK] + const.PCSQ_VALUE[Piece.WK][Sq.E1])

        # black king
        board = Board('8/8/3k4/8/8/8/8/8 w - - 0 1')
        assert board.eval() == const.PIECE_VALUE[Piece.BK] + const.PCSQ_VALUE[Piece.BK][Sq.D6]
        board = Board('8/8/3k4/8/8/8/8/8 b - - 0 1')
        assert board.eval() == -(const.PIECE_VALUE[Piece.BK] + const.PCSQ_VALUE[Piece.BK][Sq.D6])
