#!/usr/bin/env python3
"""
This file defines the Board class.
"""
from BitBoard import BitBoard
from Color import Color
from Piece import Piece
from Sq import Sq


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
        # bitboards for every piece, each color
        self.color_bb = {
            Color.WHITE: BitBoard(65535),
            Color.BLACK: BitBoard(18446462598732840960),
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
            return self._get_fen()
        else:
            self._set_fen(fen_str)

    def _get_fen(self):
        """
        Returns the FEN string of the board
        :return: the FEN string of the board
        """
        fen_str = ''

        # counter for empty squares
        empty_count = 0
        # reversed since index 0 starts at the right end for BitBoard
        for i in reversed(range(64)):
            is_empty = True
            for piece in Piece:
                if self.bitboards[piece][i] == 1:
                    if empty_count > 0:
                        fen_str += str(empty_count)
                        empty_count = 0
                    fen_str += Piece.to_char(piece)
                    is_empty = False
                    break
            if is_empty:
                empty_count += 1
            if i % 8 == 0 and i != 0:
                if empty_count > 0:
                    fen_str += str(empty_count)
                    empty_count = 0
                fen_str += '/'

        fen_str += ' ' + ('w' if self.turn == Color.WHITE else 'b')
        fen_str += ' ' + ('K' if self.wk_castling else '')
        fen_str += 'Q' if self.wq_castling else ''
        fen_str += 'k' if self.bk_castling else ''
        fen_str += 'q' if self.bq_castling else ''
        fen_str += '-' if not (self.wk_castling or self.wq_castling or self.bk_castling or self.bq_castling) else ''
        fen_str += ' ' + ('-' if self.ep_square == -1 else Sq.sq_to_filerank(self.ep_square))
        fen_str += ' ' + str(self.half_move_clock)
        fen_str += ' ' + str(self.full_move_count)

        return fen_str

    def _set_fen(self, fen_str):
        """
        Sets the board according to the given FEN string
        :param fen_str: FEN string to set the board to
        """
        # TODO validate fen_str
        board_str, turn_str, castling_str, ep_str, half_move_str, full_move_str = fen_str.split(' ')

        # reset all bitboards
        for piece in Piece:
            self.bitboards[piece] = BitBoard(0)
        self.color_bb[Color.WHITE] = BitBoard(0)
        self.color_bb[Color.BLACK] = BitBoard(0)

        board_str = board_str.replace('/', '')
        bit_index = 0
        for i, char in enumerate(board_str):
            # empty squares
            if char.isdigit():
                bit_index += int(char)
                continue
            piece = Piece.from_char(char)
            self.bitboards[piece][63 - bit_index] = 1
            self.color_bb[Piece.color(piece)][63 - bit_index] = 1
            bit_index += 1

        self.turn = Color.WHITE if turn_str == 'w' else Color.BLACK
        self.wk_castling = True if 'K' in castling_str else False
        self.wq_castling = True if 'Q' in castling_str else False
        self.bk_castling = True if 'k' in castling_str else False
        self.bq_castling = True if 'q' in castling_str else False
        self.ep_square = -1 if ep_str == '-' else Sq.filerank_to_sq(ep_str)
        self.half_move_clock = int(half_move_str)
        self.full_move_count = int(full_move_str)

    def make_move(self, move):
        """
        Make a given move and return the captured piece or 1 if no piece was captured
        :param move: captured piece from the move
        :return: the captured piece if a piece was captured, otherwise 1
        """
        captured_piece = -1
        moved_piece = -1
        for piece in Piece:
            if self.bitboards[piece][move.init_sq()]:
                moved_piece = piece
                self.bitboards[piece][move.init_sq()] = 0
                self.bitboards[piece][move.dest_sq()] = 1
                self.color_bb[self.turn][move.init_sq()] = 0
                self.color_bb[self.turn][move.dest_sq()] = 1
        # TODO how about iterating over all opponent piece and setting the bit as 0 without check?
        for piece in Piece:
            # ignore piece that just moved there
            if piece == moved_piece:
                continue
            if self.bitboards[piece][move.dest_sq()]:
                self.bitboards[piece][move.dest_sq()] = 0
                self.color_bb[Color.switch(self.turn)][move.dest_sq()] = 0
                captured_piece = piece
                break

        self.turn = Color.switch(self.turn)

        # update castling
        if moved_piece == Piece.WR:
            if move.init_sq() == Sq.A1:
                self.wq_castling = False
            if move.init_sq() == Sq.H1:
                self.wk_castling = False
        elif moved_piece == Piece.WK:
            if move.init_sq() == Sq.E1:
                self.wk_castling = False
                self.wq_castling = False
        elif moved_piece == Piece.BR:
            if move.init_sq() == Sq.A8:
                self.bq_castling = False
            if move.init_sq() == Sq.H8:
                self.bk_castling = False
        elif moved_piece == Piece.BK:
            if move.init_sq() == Sq.E8:
                self.bk_castling = False
                self.bq_castling = False

        # compute en passant square
        # TODO implement MoveType enum
        if move.move_type() == 2:
            self.ep_square = Sq((move.init_sq() + move.dest_sq()) / 2)
        else:
            self.ep_square = -1

        self.half_move_clock = 0 if moved_piece == Piece.WP or moved_piece == Piece.BP else self.half_move_clock + 1
        # note that turn is switched before this
        if self.turn == Color.WHITE:
            self.full_move_count += 1

        # TODO add Piece enum key EMPTY
        return captured_piece

    def move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal moves
        :return: a list of all possible legal moves
        """
        # TODO find if king is checked and for pinned pieces
        moves = self._pawn_move_gen()
        moves.extend(self._knight_move_gen())
        moves.extend(self._bishop_move_gen())
        moves.extend(self._rook_move_gen())
        moves.extend(self._queen_move_gen())
        moves.extend(self._king_move_gen())
        return moves

    def _pawn_move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal pawn moves
        :return: a list of all possible legal pawn moves
        """
        return []

    def _knight_move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal knight moves
        :return: a list of all possible legal knight moves
        """
        # PSEUDOCODE
        # moves = []
        #
        # for knight_sq in self.piece_sq[Piece.WN]: (or Piece.BN)
        #     get ATTACK_BB
        #     capture = ATTACK_BB & self.color_bb[Color.BLACK]
        #     for index in capture.indices():
        #         moves.append(knight_sq, index, 1)
        #     noncapture = ATTACK_BB & !self.color_bb[Color.BLACK]
        #     for index in noncapture.indices():
        #         moves.append(knight_sq, index, 0)
        #
        # return moves

        return []

    def _bishop_move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal bishop moves
        :return: a list of all possible legal bishop moves
        """
        return []

    def _rook_move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal rook moves
        :return: a list of all possible legal rook moves
        """
        return []

    def _queen_move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal queen moves
        :return: a list of all possible legal queen moves
        """
        return []

    def _king_move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal king moves
        :return: a list of all possible legal king moves
        """
        return []


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
