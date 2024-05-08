from player import Player
from opponent import Opponent
from game_flow import GameFlow
play_again = 'y'

while play_again.lower() == 'y':
  player_1 = Player()
  opp = Opponent()
  game = GameFlow()

  while game.game_length == 0:
    length = input('Please enter a game length: ')
    print(game.select_game_length(length))

  while (player_1.w < game.game_length) & (opp.w < game.game_length):
    opponent_selection = opp.make_selection()
    player_selection = input('Make your selection: ')

    while player_1.invalid_selection(player_selection):
      print(player_1.get_input(player_selection))
      player_selection = input('Make your selection: ')
    
    print('The selections are in.....')
    print('....')
    print('....')
    print('....')
    print('....')
    print('....')
    print(f'Opponent chose {opponent_selection}')
    print(game.determine_winner(player_1, player_selection, opp, opponent_selection))

    print(f'The current score if {player_1.w} to {opp.w}. Reminder, first to {game.game_length} wins!')
    opp.selection_probability(player_selection)

  if player_1.w > opp.w:
    print('You win!')
  else:
    print('You lose!')

  play_again = input('Press y to play again, any key to end: ')
