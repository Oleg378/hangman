from game import Game

game = Game()

while (not game.is_win_condition()) and (game.get_available_tries() > 0):
    print(f'try to guess this word: {(game.opened_symbols())}')
    print(f'Available tries: {game.get_available_tries()}')
    game.set_symbol()
    print(f'You used this chars: {game.get_symbols()}')