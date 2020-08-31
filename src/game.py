from domino_pieces import get_random_sorted_pieces

class Game:
    def __init__(self):
        pieces = get_random_sorted_pieces()
        self.player1 = pieces[:7]
        self.player2 = pieces[7:15]
        self.game_board = [pieces[15]]
        self.aux_pieces = pieces[16:]

    def print_board(self):
        for item in self.game_board:
            print(f'[ {item.left} | {item.right} ]', end = '')

        print()

    def get_player_pieces(self):
        return self.player

    def get_player2_pieces(self):
        return self.player2

    def get_edges(self):
        if len(self.game_board):
            return [self.game_board[0].left,  self.game_board[-1].right]
        return[]

    def move_player_1(self, piece):
        print(f'Peca selecionada: [ {piece.left} | {piece.right} ]')
        edges = self.get_edges()
        if self.__validate_pieces(piece, edges):
            position = self.__get_position(piece, self.get_edges())
            if position == 'right':
                value_from_board = self.get_edges()[1]
            else:
                value_from_board = self.get_edges()[0]


            self.player1.remove(piece)
            piece_validated = self.__validate_pieces_position(piece, position, value_from_board)
            self.__play(piece_validated, position)
            return True

        return False

    def move_player_2(self, piece):
        print(f'Peca selecionada pelo player 2: [ {piece.left} | {piece.right} ]')
        edges = self.get_edges()
        if self.__validate_pieces(piece, edges):
            position = self.__get_position(piece, edges)
            if position == 'right':
                value_from_board = edges[1]
            else:
                value_from_board = edges[0]

            self.player2.remove(piece)
            piece_validated = self.__validate_pieces_position(piece, position, value_from_board)
            self.__play(piece_validated, position)
            return True

        return False

    def get_an_extra_piece(self, name):
        if len(self.game_board):
            piece = self.aux_pieces.pop()
            if name == 'player1':
                print(f'Voce acabou de pedir uma peça extra [ {piece.left} | {piece.right} ].')
                self.player1.append(piece)
                return self.player1
            else:
                print('Player 2 acabou de pedir uma peça extra.')
                self.player2.append(piece)
                return self.player2

        else:
            print('Nao existem mais peças extras, voce perdeu sua vez.')
            return False

    def finish_game(self):
        score_player1 = sum(item.right + item.left for item in self.player1)
        score_player2 = sum(item.right + item.left for item in self.player2)
        print('Parabens!' if score_player1 < score_player2 else 'Nao foi dessa vez :(')

    def __validate_pieces(self, piece, piece_from_board):
        if piece.right in piece_from_board or piece.left in piece_from_board:
            return True

        print('Voce selecionou uma peca invalida, perdeu sua vez!')
        return False

    def __validate_pieces_position(self, piece, position, value_from_board):
        if position == 'right' and piece.right == value_from_board:
            piece.right = piece.left
            piece.left = value_from_board

        if position == 'left' and piece.left == value_from_board:
            piece.left = piece.right
            piece.right = value_from_board

        return piece

    def __play(self, piece, position):
        if position == 'right':
            self.game_board.append(piece)
        else:
            self.game_board.insert(0, piece)

    def __get_position(self, piece, board_values):
        if piece.right == board_values[0] or piece.left == board_values[0]:
            return 'left'

        return'right'