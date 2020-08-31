
class ArtificialPlayer:
    def play(self, game):
        # choose a piece according rules
        piece = self.__get_a_valid_piece(game)

        if piece:
            game.move_player_2(piece)
            return True

        return False


    def __get_a_valid_piece(self, game):
        all_possible_movements = self.__get_all_possible_moviments(game.player2, game.get_edges())

        if len(all_possible_movements) == 0:
            all_possible_movements = self.__try_with_an_extra_piece(game)

        if len(all_possible_movements):
            # Regra: Pegar a peca com valor mais alto.
            max_value = max(item.right + item.left for item in all_possible_movements)
            for item in all_possible_movements:
                if item.right + item.left == max_value:
                    return item


    def __try_with_an_extra_piece(self, game):
        game.get_an_extra_piece('player2')
        return self.__get_all_possible_moviments(game.player2, game.get_edges())

    def __get_all_possible_moviments(self, my_pieces, board_values):
        possible_movies = []
        for item in my_pieces:
            if item.right in board_values or item.left in board_values:
                possible_movies.append(item)

        return possible_movies
