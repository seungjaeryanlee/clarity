#!/usr/bin/env python3
"""
This file defines the Board class.
"""
from BitBoard import BitBoard
from Color import Color
from Piece import Piece


class Board:
    """
    This class represents the status of a board.
    """

    def __init__(self):
        """
        Run when a Board object is created.
        """
        # dictionary of bitboards for each piece. bits set to their starting positions
        self.bitboards = {
            Piece.WP: BitBoard(65280),
            Piece.WN: BitBoard(66),
            Piece.WB: BitBoard(36),
            Piece.WR: BitBoard(129),
            Piece.WQ: BitBoard(16),
            Piece.WK: BitBoard(8),
            Piece.BP: BitBoard(71776119061217280),
            Piece.BN: BitBoard(4755801206503243776),
            Piece.BB: BitBoard(2594073385365405696),
            Piece.BR: BitBoard(9295429630892703744),
            Piece.BQ: BitBoard(1152921504606846976),
            Piece.BK: BitBoard(576460752303423488),
        }
        # color to play next move
        self.turn = Color.WHITE
        # en passant square (if no square, -1)
        self.ep_square = -1
        # possibility to castling (checked based on rook/king being moved)
        self.wk_castling = True
        self.wq_castling = True
        self.bk_castling = True
        self.bq_castling = True
        # number of half moves for the fifty move rule
        self.half_move_clock = 0
        # number of full moves made
        self.full_move_count = 1

    def fen(self, fen_str=None):
        """
        Returns a FEN string or sets the board according to given FEN string
        :param fen_str: FEN string given to set the board
        :return: the FEN string of the board if fen_str is not specified, None if fen_str is specified
        """
        if fen_str is None:
            self._get_fen()
        else:
            return self._set_fen(fen_str)

    def _get_fen(self):
        """
        Returns the FEN string of the board
        :return: the FEN string of the board
        """
        pass

    def _set_fen(self, fen_str):
        """
        Sets the board according to the given FEN string
        :param fen_str: FEN string to set the board to
        """
        pass


# only runs when this module is called directly
if __name__ == '__main__':
    board = Board()
    print("White Pawns:")
    print(board.bitboards[Piece.WP])
    print("White Knights:")
    print(board.bitboards[Piece.WN])
    print("White Bishops:")
    print(board.bitboards[Piece.WB])
    print("White Rooks:")
    print(board.bitboards[Piece.WR])
    print("White Queen:")
    print(board.bitboards[Piece.WQ])
    print("White King:")
    print(board.bitboards[Piece.WK])
    print("Black Pawns:")
    print(board.bitboards[Piece.BP])
    print("Black Knights:")
    print(board.bitboards[Piece.BN])
    print("Black Bishops:")
    print(board.bitboards[Piece.BB])
    print("Black Rooks:")
    print(board.bitboards[Piece.BR])
    print("Black Queen:")
    print(board.bitboards[Piece.BQ])
    print("Black King:")
    print(board.bitboards[Piece.BK])
