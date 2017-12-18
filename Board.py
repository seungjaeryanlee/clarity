#!/usr/bin/env python3
"""
This file defines the Board class.
"""
from BitBoard import BitBoard
from Color import Color
import constants as const
from Move import Move
from MoveType import MoveType
from Piece import Piece
from Sq import Sq


class Board:
    """
    This class represents the status of a board.
    """

    def __init__(self, fen_str=None):
        """
        Run when a Board object is created. If fen_str is specified, set the board according to the given FEN string.
        Otherwise, set the board to the starting position.
        :param fen_str: FEN string to set the board to (if specified)
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
        # dictionary where for each piece (key), the value is the list of bit indices of where piece exists
        # the kings are also in the list for uniformity, although there can only be one king
        self.piece_sq = {
            Piece.WP: [Sq.A2, Sq.B2, Sq.C2, Sq.D2, Sq.E2, Sq.F2, Sq.G2, Sq.H2],
            Piece.WN: [Sq.B1, Sq.G1],
            Piece.WB: [Sq.C1, Sq.F1],
            Piece.WR: [Sq.A1, Sq.H1],
            Piece.WQ: [Sq.D1],
            Piece.WK: [Sq.E1],
            Piece.BP: [Sq.A7, Sq.B7, Sq.C7, Sq.D7, Sq.E7, Sq.F7, Sq.G7, Sq.H7],
            Piece.BN: [Sq.B8, Sq.G8],
            Piece.BB: [Sq.C8, Sq.F8],
            Piece.BR: [Sq.A8, Sq.H8],
            Piece.BQ: [Sq.D8],
            Piece.BK: [Sq.E8],
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

        if fen_str is not None:
            self._set_fen(fen_str)

    def __str__(self):
        """
        Overrides default function to a string showing a 8x8 chessboard with character notation strings
        :return: a string of 8x8 chessboard with character notation strings
        """
        return self._get_fen().split(' ')[0].replace('/', '\n').replace('1', '-').replace('2', '--')\
                                                               .replace('3', '---').replace('4', '----')\
                                                               .replace('5', '-----').replace('6', '------')\
                                                               .replace('7', '-------').replace('8', '--------')

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
            if i % 8 == 0:
                if empty_count > 0:
                    fen_str += str(empty_count)
                    empty_count = 0
            if i % 8 == 0 and i != 0:
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

        # reset all bitboards and piece_sq
        for piece in Piece:
            self.bitboards[piece] = BitBoard(0)
            self.piece_sq[piece] = []
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
            self.piece_sq[piece].append(Sq(63 - bit_index))
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

        # update self.piece_sq
        self.piece_sq[moved_piece].remove(move.init_sq())
        self.piece_sq[moved_piece].append(move.dest_sq())
        if captured_piece != -1:
            self.piece_sq[captured_piece].remove(move.dest_sq())

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
        if move.move_type() == MoveType.DOUBLE:
            self.ep_square = Sq((move.init_sq() + move.dest_sq()) / 2)
        else:
            self.ep_square = -1

        self.half_move_clock = 0 if moved_piece == Piece.WP or moved_piece == Piece.BP else self.half_move_clock + 1
        # note that turn is switched before this
        if self.turn == Color.WHITE:
            self.full_move_count += 1

        return captured_piece

    def move_gen(self):
        """
        TODO implement
        Returns a list of all possible legal moves
        :return: a list of all possible legal moves
        """
        king = Piece.WK if self.turn == Color.WHITE else Piece.BK
        king_sq = self.piece_sq[king][0]
        checks = self.get_attacking_sqs(king_sq)

        if len(checks) == 2:
            # king must move out of danger
            return self._king_move_gen()
        elif len(checks) == 1:
            pinned = self.find_pinned()
            pinned_sqs = [pinned_tuple[0] for pinned_tuple in pinned]

            # move king out of danger
            moves = self._king_move_gen()
            # capture piece attacking king
            attacking_sqs = self.get_attacking_sqs(checks[0])
            if len(attacking_sqs) > 0:
                for attacking_sq in attacking_sqs:
                    # check if the attacking_sq is pinned
                    if attacking_sqs in pinned_sqs:
                        # TODO check type of capture (CAPTURE, EP_CAPTURE, X_PROMO_CAPTURE)
                        moves.append(Move(attacking_sq, checks[0], MoveType.CAPTURE))
            # 3. block slider piece attacking king
            # TODO similar to above, but check for all spaces in between the slider and the king, and also
            # TODO pawn needs to move quiet or via double pawn push, not by capture.
            return moves
        else:
            # TODO exclude pinned pieces
            pinned = self.find_pinned()
            pinned_sqs = [pinned_tuple[0] for pinned_tuple in pinned]

            # generate moves
            moves = self._pawn_move_gen()
            moves.extend(self._knight_move_gen())
            moves.extend(self._bishop_move_gen())
            moves.extend(self._rook_move_gen())
            moves.extend(self._queen_move_gen())
            moves.extend(self._king_move_gen())
            moves.extend(self._castling_move_gen())
            return moves

    def get_attacking_sqs(self, sq):
        """
        Returns list of squares of pieces putting the king on check. Returns an empty list if the king is not in check.
        :return: a list squares of pieces putting the king on check or an empty list if the king is not in check.
        """
        checks = self._get_attacking_pawn_sqs(sq)
        checks.extend(self._get_attacking_knight_sqs(sq))
        # TODO can also find pinned pieces similarly
        checks.extend(self._get_attacking_bishop_sqs(sq))
        checks.extend(self._get_attacking_rook_sqs(sq))
        checks.extend(self._get_attacking_queen_sqs(sq))

        return checks

    def _get_attacking_pawn_sqs(self, sq):
        """
        Returns list of squares of pawns putting the king on check.
        :return: a list of squares of pawns putting the king on check.
        """
        checks = []

        pawn = Piece.WP if self.turn == Color.WHITE else Piece.BP
        enemy_pawn = Piece.BP if self.turn == Color.WHITE else Piece.WP

        pawns = const.ATTACK[pawn][sq] & self.bitboards[enemy_pawn]
        if pawns != BitBoard(0):
            for pawn_sq in pawns.indices():
                checks.append(pawn_sq)

        return checks

    def _get_attacking_knight_sqs(self, sq):
        """
        Returns list of squares of knights putting the king on check.
        :return: a list of squares of knights putting the king on check.
        """
        checks = []

        knight = Piece.WN if self.turn == Color.WHITE else Piece.BN
        enemy_knight = Piece.BN if self.turn == Color.WHITE else Piece.WN

        # note that const.ATTACK[knight] and const.ATTACK[enemy_knight] uses same bitboards
        knights = const.ATTACK[knight][sq] & self.bitboards[enemy_knight]
        if knights != BitBoard(0):
            for knight_sq in knights.indices():
                checks.append(knight_sq)

        return checks

    def _get_attacking_slider_sqs(self, sq, slider, enemy_slider):
        """
        Returns list of squares of the given slider piece putting the king on check.
        :return: a list of squares of the given slider piece putting the king on check.
        """

        # Find the king. Use the directional attack bitboards of each slider on the KING'S SQUARE and AND(&) it with
        # the bitboard of enemy sliders to find the sliders that could be putting the king on check. Then, check if
        # the trajectory is blocked. To find blocking pieces, AND(&) the directional attack bitboards with the
        # bitboard of all pieces on board. Then, to check if this piece is actually between the king and the enemy
        # slider, compare the blocking piece and the enemy slider piece for their distance to the king square. (Not
        # the slider piece since the directional attack bitboard was used on the KING'S SQUARE) If the distance is
        # smaller for the blocking piece, the slider is not putting king on check. If the distance is bigger, add
        # it to the list of checks.

        check_sqs = []

        # note that const.ATTACK[slider] and const.ATTACK[enemy_slider] uses same bitboards
        for _, ATTACK_DIR in const.ATTACK[slider].items():
            # get bitboard of slider pieces with king on their trajectory
            sliders = ATTACK_DIR[sq] & self.bitboards[enemy_slider]
            # get other pieces on that trajectory
            possible_blocks = ATTACK_DIR[sq] & (self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])

            # search for a blocking piece between the slider and the king
            for slider_sq in sliders.indices():
                is_blocked = False
                for possible_block_sq in possible_blocks.indices():
                    # if the piece is closer to the king then it is to the slider piece, it is a block
                    if abs(sq - possible_block_sq) < abs(slider_sq - sq):
                        is_blocked = True
                        break
                if not is_blocked:
                    check_sqs.append(slider_sq)

        return check_sqs

    def _get_attacking_bishop_sqs(self, sq):
        """
        Returns list of squares of bishops putting the king on check.
        :return: a list of squares of bishops putting the king on check.
        """
        bishop = Piece.WB if self.turn == Color.WHITE else Piece.BB
        enemy_bishop = Piece.BB if self.turn == Color.WHITE else Piece.WB

        return self._get_attacking_slider_sqs(sq, bishop, enemy_bishop)

    def _get_attacking_rook_sqs(self, sq):
        """
        Returns list of squares of rooks putting the king on check.
        :return: a list of squares of rooks putting the king on check.
        """
        rook = Piece.WR if self.turn == Color.WHITE else Piece.BR
        enemy_rook = Piece.BR if self.turn == Color.WHITE else Piece.WR

        return self._get_attacking_slider_sqs(sq, rook, enemy_rook)

    def _get_attacking_queen_sqs(self, sq):
        """
        Returns list of squares of queens putting the king on check.
        :return: a list of squares of queens putting the king on check.
        """
        queen = Piece.WQ if self.turn == Color.WHITE else Piece.BQ
        enemy_queen = Piece.BQ if self.turn == Color.WHITE else Piece.WQ

        return self._get_attacking_slider_sqs(sq, queen, enemy_queen)

    def find_pinned(self):
        """
        Returns list of tuples of the square of pinned pieces and the square of the slider pinning it.
        :return: a list of tuples of the square of pinned pieces and the square of the slider pinning it.
        """

        # Find the king. Use the directional attack bitboards of each slider on the KING'S SQUARE and AND(&) it with
        # the bitboard of enemy sliders to find the sliders that could be pinning a piece. Then, check if the
        # trajectory is blocked by a single allied piece.
        #
        # To find all blocking pieces, AND(&) the directional attack bitboards with the bitboard of all the pieces on
        # board. Then, to check if this piece is actually between the king and the enemy slider, compare the blocking
        # piece and the enemy slider piece for their distance to the king square. (Not the slider piece since the
        # directional attack bitboard was used on the KING'S SQUARE) If the distance is smaller for the blocking piece,
        # the piece is between the enemy slider piece and the king.
        #
        # If there is only one allied piece, add the square of that piece to the list of pinned piece squares. If there
        # is zero or multiple allied piece, or if there is an enemy piece between the king and the enemy slider,
        # do nothing.

        pinned = []
        king_sq = self.piece_sq[Piece.WK if self.turn == Color.WHITE else Piece.BK][0]
        enemy_sliders = {Piece.BB, Piece.BR, Piece.BQ} if self.turn == Color.WHITE else {Piece.WB, Piece.WR, Piece.WQ}

        for enemy_slider in enemy_sliders:
            # const.ATTACK[slider] and const.ATTACK[enemy_slider] uses same bitboards, so using either is fine
            for _, ATTACK_DIR in const.ATTACK[enemy_slider].items():
                # get bitboard of slider pieces with king on their trajectory
                sliders = ATTACK_DIR[king_sq] & self.bitboards[enemy_slider]
                # get other pieces on that trajectory
                possible_blocks = ATTACK_DIR[king_sq] & (self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])

                for slider_sq in sliders.indices():
                    # find all blocking pieces between the slider and the king
                    blocks = []
                    for possible_block_sq in possible_blocks.indices():
                        # if the piece is closer to the king then it is to the slider piece, it is a block
                        if abs(king_sq - possible_block_sq) < abs(slider_sq - king_sq):
                            blocks.append(possible_block_sq)
                    # if there are many pieces between the king and the slider, nothing is pinned
                    # if the piece between is not the king's piece, nothing is pinned
                    if len(blocks) == 1 and self.color_bb[self.turn][blocks[0]] == 1:
                        pinned.append((blocks[0], slider_sq))

        return pinned

    def _pinned_move_gen(self, pinned_sq, slider_sq, slider_direction):
        """
        TODO implement
        Returns a move possible for a piece on the given pinned_sq square using given slider_sq and slider_type.
        If there is no move possible, return None.
        :param pinned_sq: the square the pinned piece is on
        :param slider_sq: the square the pinning slider is on
        :param slider_direction: the direction of the pinning slider
        :return: a move possible for a piece on the given pinned_sq square.
        """

        # The only move the pinned piece can make is capturing the slider piece pinning it. 1. If the pinned piece is
        # a pawn, it can only capture a bishop on its attacking square. 2. Otherwise, check if the piece on the pinned
        # square is a slider that can slide the correct direction. Note that pinned knights can never move.

        # 1. Find piece type of pinned piece
        # 2. If knight, return None
        # 3. If pawn, check for both ATTACK bitboard and PROMO-ATTACK bitboard
        # 4. If slider, check if the slider can move the given direction
        pass

    def _pawn_move_gen(self):
        """
        Returns a list of all possible legal pawn moves
        :return: a list of all possible legal pawn moves
        """
        moves = []
        piece = Piece.WP if self.turn == Color.WHITE else Piece.BP

        for pawn_sq in self.piece_sq[piece]:
            # quiet moves
            quiet = const.MOVE_P[piece][pawn_sq] & ~(self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])
            for index in quiet.indices():
                moves.append(Move(pawn_sq, index, MoveType.QUIET))

            # double pawn push moves
            double = const.DOUBLE_P[piece][pawn_sq] & ~(self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])
            for index in double.indices():
                # the middle square should also be empty
                if (self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])[(pawn_sq + index)/2] == 0:
                    moves.append(Move(pawn_sq, index, MoveType.DOUBLE))

            # attack moves
            capture = const.ATTACK[piece][pawn_sq] & self.color_bb[Color.switch(self.turn)]
            for index in capture.indices():
                moves.append(Move(pawn_sq, index, MoveType.CAPTURE))

            # quiet promotion moves
            # TODO check if there exists a 7th/2nd row pawn before this?
            promo = const.PROMO_P[piece][pawn_sq] & ~(self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])
            for index in promo.indices():
                moves.append(Move(pawn_sq, index, MoveType.N_PROMO))
                moves.append(Move(pawn_sq, index, MoveType.B_PROMO))
                moves.append(Move(pawn_sq, index, MoveType.R_PROMO))
                moves.append(Move(pawn_sq, index, MoveType.Q_PROMO))

            # capture promotion moves
            # TODO check if there exists a 7th/2nd row pawn before this?
            promo_capture = const.PROMO_CAPTURE_P[piece][pawn_sq] & self.color_bb[Color.switch(self.turn)]
            for index in promo_capture.indices():
                moves.append(Move(pawn_sq, index, MoveType.N_PROMO_CAPTURE))
                moves.append(Move(pawn_sq, index, MoveType.B_PROMO_CAPTURE))
                moves.append(Move(pawn_sq, index, MoveType.R_PROMO_CAPTURE))
                moves.append(Move(pawn_sq, index, MoveType.Q_PROMO_CAPTURE))

            # check for en passant
            if self.ep_square != -1:
                if const.ATTACK[piece][pawn_sq][self.ep_square]:
                    moves.append(Move(pawn_sq, self.ep_square, MoveType.EP_CAPTURE))

        return moves

    def _knight_move_gen(self):
        """
        TODO check if knight is pinned
        Returns a list of all possible legal knight moves
        :return: a list of all possible legal knight moves
        """
        moves = []
        piece = Piece.WN if self.turn == Color.WHITE else Piece.BN

        for knight_sq in self.piece_sq[piece]:
            capture = const.ATTACK[piece][knight_sq] & self.color_bb[Color.switch(self.turn)]
            for index in capture.indices():
                moves.append(Move(knight_sq, index, MoveType.CAPTURE))
            noncapture = const.ATTACK[piece][knight_sq] & ~(self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])
            for index in noncapture.indices():
                moves.append(Move(knight_sq, index, MoveType.QUIET))

        return moves

    def _slider_move_gen(self, piece):
        """
        TODO check for pin
        Returns a list of all possible legal moves for the given slider piece
        :param piece: a slider piece (bishop, rook, or queen)
        :return: a list of all possible legal moves for the given slider piece
        """
        moves = []

        for sq in self.piece_sq[piece]:
            for direction, ATTACK_DIR in const.ATTACK[piece].items():
                capture_or_block = ATTACK_DIR[sq] & (self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])
                if capture_or_block == BitBoard(0):
                    for index in ATTACK_DIR[sq].indices():
                        moves.append(Move(sq, index, MoveType.QUIET))
                else:
                    min_diff = 64
                    min_sq = -1
                    # Get the closest piece in the way of movement
                    for index in capture_or_block.indices():
                        if min_diff > abs(sq - index):
                            min_diff = abs(sq - index)
                            min_sq = index
                    # Add all moves before that piece
                    for index in ATTACK_DIR[sq].indices():
                        if min_diff > abs(sq - index):
                            moves.append(Move(sq, index, MoveType.QUIET))
                    capture = ATTACK_DIR[sq] & self.color_bb[Color.switch(self.turn)]
                    # If enemy piece, add CAPTURE move
                    if capture[min_sq] == 1:
                        moves.append(Move(sq, min_sq, MoveType.CAPTURE))

        return moves

    def _bishop_move_gen(self):
        """
        TODO check for pin
        Returns a list of all possible legal bishop moves
        :return: a list of all possible legal bishop moves
        """
        piece = Piece.WB if self.turn == Color.WHITE else Piece.BB
        return self._slider_move_gen(piece)

    def _rook_move_gen(self):
        """
        TODO check for pin
        Returns a list of all possible legal rook moves
        :return: a list of all possible legal rook moves
        """
        piece = Piece.WR if self.turn == Color.WHITE else Piece.BR
        return self._slider_move_gen(piece)

    def _queen_move_gen(self):
        """
        TODO check for pin
        Returns a list of all possible legal queen moves
        :return: a list of all possible legal queen moves
        """
        piece = Piece.WQ if self.turn == Color.WHITE else Piece.BQ
        return self._slider_move_gen(piece)

    def _king_move_gen(self):
        """
        Returns a list of all possible legal king moves
        :return: a list of all possible legal king moves
        """
        moves = []
        piece = Piece.WK if self.turn == Color.WHITE else Piece.BK

        safe_bb = self._get_safe_bb()

        # note that this should only once since there can only be one king
        for king_sq in self.piece_sq[piece]:
            capture = const.ATTACK[piece][king_sq] & self.color_bb[Color.switch(self.turn)] & safe_bb
            for index in capture.indices():
                moves.append(Move(king_sq, index, MoveType.CAPTURE))
            noncapture = const.ATTACK[piece][king_sq] & ~(self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK])\
                & safe_bb
            for index in noncapture.indices():
                moves.append(Move(king_sq, index, MoveType.QUIET))

        return moves

    def _castling_move_gen(self):
        """
        Returns a list of all possible legal castling moves
        :return: a list of all possible legal castling moves
        """
        moves = []
        king = Piece.WK if self.turn == Color.WHITE else Piece.BK
        king_sq = self.piece_sq[king][0]
        pieces_bb = self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK]

        # is king on check?
        # TODO this is probably checked multiple times in a single Board.move_gen(). maybe save this value?
        checks = self.get_attacking_sqs(king_sq)
        if len(checks) != 0:
            return []

        if self.turn == Color.WHITE:
            if self.wk_castling:
                # is there a piece between?
                if pieces_bb[Sq.F1] == 0 and pieces_bb[Sq.G1] == 0:
                    # will king be on check while moving or after move?
                    if len(self.get_attacking_sqs(Sq.F1)) == 0 and len(self.get_attacking_sqs(Sq.G1)) == 0:
                        moves.append(Move(Sq.E1, Sq.G1, MoveType.K_CASTLE))
            if self.wq_castling:
                # is there a piece between?
                if pieces_bb[Sq.D1] == 0 and pieces_bb[Sq.C1] == 0:
                    # will king be on check while moving or after move?
                    if len(self.get_attacking_sqs(Sq.D1)) == 0 and len(self.get_attacking_sqs(Sq.C1)) == 0:
                        moves.append(Move(Sq.E1, Sq.C1, MoveType.Q_CASTLE))
        else:
            if self.bk_castling:
                # is there a piece between?
                if pieces_bb[Sq.F8] == 0 and pieces_bb[Sq.G8] == 0:
                    # will king be on check while moving or after move?
                    if len(self.get_attacking_sqs(Sq.F8)) == 0 and len(self.get_attacking_sqs(Sq.G8)) == 0:
                        moves.append(Move(Sq.E8, Sq.G8, MoveType.K_CASTLE))
            if self.bq_castling:
                # is there a piece between?
                if pieces_bb[Sq.D8] == 0 and pieces_bb[Sq.C8] == 0:
                    # will king be on check while moving or after move?
                    if len(self.get_attacking_sqs(Sq.D8)) == 0 and len(self.get_attacking_sqs(Sq.C8)) == 0:
                        moves.append(Move(Sq.E8, Sq.C8, MoveType.Q_CASTLE))

        return moves

    def _get_safe_bb(self):
        """
        Returns the BitBoard of safe squares
        :return: the BitBoard of safe squares
        """
        danger_bb = BitBoard(0)
        if self.turn == Color.WHITE:
            king = Piece.WK
            enemy_pieces = {Piece.BP, Piece.BN, Piece.BK}
            enemy_sliders = {Piece.BB, Piece.BR, Piece.BQ}
        else:
            king = Piece.BK
            enemy_pieces = {Piece.WP, Piece.WN, Piece.WK}
            enemy_sliders = {Piece.WB, Piece.WR, Piece.WQ}

        for enemy_piece in enemy_pieces:
            for sq in self.piece_sq[enemy_piece]:
                danger_bb = danger_bb | const.ATTACK[enemy_piece][sq]

        # exclude king when checking for slider blocks
        block_bb = (self.color_bb[Color.WHITE] | self.color_bb[Color.BLACK]) & ~self.bitboards[king]

        for enemy_slider in enemy_sliders:
            for _, ATTACK_DIR in const.ATTACK[enemy_slider].items():
                for slider_sq in self.piece_sq[enemy_slider]:
                    # check if there is anything blocking the slider
                    blocks = ATTACK_DIR[slider_sq] & block_bb
                    # if nothing is blocking it, add all squares
                    if blocks == BitBoard(0):
                        danger_bb = danger_bb | ATTACK_DIR[slider_sq]
                    else:
                        # get the closest block
                        min_diff = 64
                        closest_block_sq = -1
                        for block_sq in blocks.indices():
                            diff = abs(block_sq - slider_sq)
                            if min_diff > diff:
                                min_diff = diff
                                closest_block_sq = block_sq

                        # add all squares before the block square
                        for index in ATTACK_DIR[slider_sq].indices():
                            diff = abs(index - slider_sq)
                            if min_diff > diff:
                                danger_bb[index] = 1

                        # add block square if block is not king's color
                        if self.color_bb[Color.switch(self.turn)][closest_block_sq] == 1:
                            danger_bb[closest_block_sq] = 1

        return ~danger_bb


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
