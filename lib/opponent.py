class Opponent():
  def __init__(self, wins = 0, losses = 0):
    self.w = wins
    self.l = losses
    self.selections = {
                        'rock': 0,
                        'paper': 0,
                        'scissors': 0,
                      }
    self.inverse_selections = {
                                'paper': 'scissors',
                                'scissors': 'rock',
                                'rock': 'paper'
                              }

  def selection_probability(self, player_selection):
    self.selections_update(self.inverse_selections[player_selection.lower()])

  def selections_update(self, inverse):
    self.selections[inverse] = self.selections[inverse] + 1
  
  def make_selection(self):
    highest_propability = ''

    for selection in self.selections:
      if highest_propability == '':
        highest_propability = selection
      elif self.selections[selection] > self.selections[highest_propability]:
        highest_propability = selection
    
    return highest_propability