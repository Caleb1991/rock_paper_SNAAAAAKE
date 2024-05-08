class Player:
  def __init__(self, wins = 0, losses = 0):
    self.w = wins
    self.l = losses

  def get_input(self, selection):
    if self.invalid_selection(selection):
      return 'Sorry, only rock, paper, or scissors are valid selections!'
      self.get_input()
    else:
      return 'You have selected: ' + selection
  
  def invalid_selection(self, selection):
    if selection.lower() not in ['rock', 'paper', 'scissors']:
      return True
    return False

  