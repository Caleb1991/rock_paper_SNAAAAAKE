from lib.player import *

def test_player_creation():
  player_1 = Player()
  assert isinstance(player_1, Player)

def test_wins():
  player_1 = Player(1)
  assert player_1.w == 1

def test_losses():
  player_1 = Player(0, 1)
  assert player_1.l == 1

def test_get_input():
  player_1 = Player()

  assert player_1.get_input('peanut') == 'Sorry, only rock, paper, or scissors are valid selections!'
  assert player_1.get_input('rock') == 'You have selected: rock'