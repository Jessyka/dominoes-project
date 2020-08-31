from game import Game
from artificial_player import ArtificialPlayer

def main():
    print('Vamos iniciar um jogo de domino.')
    print('...')

    print('Voce vai comecar a jogar.')

    game = Game()
    player_2 = ArtificialPlayer()
    no_movements = False
    while not no_possible_moves(game, no_movements):
        game.print_board()
        no_movements_play_1 = move_player(game, True)

        print('Agora eh a vez do seu oponente:')

        if len(game.player1) > 0:
            no_movements_play_2 = player_2.play(game)

        no_movements = no_movements_play_1 and no_movements_play_2

    game.finish_game()



def move_player(game, can_access_extra_piece):
    print('Escolha uma de suas pecas:')
    counter = 1
    for item in game.player1:
        print(f'Digite {counter} para escolher peca: [ {item.right} | {item.left} ]')
        counter = counter + 1

    if can_access_extra_piece:
        print(f'Digite {counter} para pedir uma peca extra.')
    else:
        print(f'Digite {counter} para passar a vez.')

    option = int(input())

    if option < counter:
        game.move_player_1(game.player1[option - 1])
        return True
    elif option == counter:
        if can_access_extra_piece:
            game.get_an_extra_piece('player1')
            move_player(game, False)
        else:
            print('Voce passou a vez...')
    else:
        print('Opcao invalida, voce perdeu a vez :(')

    return False

def no_possible_moves(game, no_movements):
    return len(game.player1) == 0 or len(game.player2) == 0 or (no_movements and len(game.aux_pieces) == 0)



main()