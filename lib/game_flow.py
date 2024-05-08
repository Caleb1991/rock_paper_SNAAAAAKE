class GameFlow():
  def __init__(self):
    self.game_length = 0
  
  def determine_winner(self, player, player_selection, opponent, opponent_selection):
    if player_selection.lower() == opponent_selection:
      return 'DRAW!!!!!'

    match player_selection.lower():
      case 'rock':
        if opponent_selection == 'scissors':
          player.w += 1
          return 'You won!'
        else:
          opponent.w += 1
          return 'Mmmmmmm, another win for Milosh!'
      case 'paper':
        if opponent_selection == 'rock':
          player.w += 1
          return 'You won!'
        else:
          opponent.w += 1
          return 'Mmmmmmm, another win for Milosh!'
      case 'scissors':
        if opponent_selection == 'paper':
          player.w += 1
          return 'You won!'
        else:
          opponent.w += 1
          return 'Mmmmmmm, another win for Milosh!'

  def select_game_length(self, length):
    try:
      length = int(length)

      if length > 5:
        return 'Ummmmmm thats a bit long, please select again.'
      else:
        self.game_length = length
        return f'You have selected first to {length} wins, good luck!'
    except ValueError:
      return 'Sorry, that is not an acceptable game duration!'
    

  def is_winner(self, player_wins, opponent_wins):
    if player_wins == game_length | opponent_wins == game_length:
      if player_wins > opponent_wins:
        return 'Congratulations! You won!'
      else:
        return 'Sorry, you lost. Better luck next time!'
  
  def get_input(self, input_type):
    inputs = {
      'length': 'Please select a game length: '
    }

    return inputs[input_type]