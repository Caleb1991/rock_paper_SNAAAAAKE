from lib.game_flow import *
from lib.player import *
from lib.opponent import *

def test_creation():
  game = GameFlow()

  assert isinstance(game, GameFlow)

def test_winner():
  game = GameFlow()
  opp = Opponent()
  player = Player()
  
  assert game.determine_winner(player, 'Rock', opp, 'paper') == 'Mmmmmmm, another win for Milosh!'
  assert opp.w == 1
  assert game.determine_winner(player, 'Rock', opp, 'rock') == 'DRAW!!!!!'
  assert game.determine_winner(player, 'Rock', opp, 'scissors') == 'You won!'
  assert player.w == 1

def test_game_length():
  game = GameFlow()

  assert game.select_game_length('Peanut') == 'Sorry, that is not an acceptable game duration!'
  assert game.select_game_length('Lou') == 'Sorry, that is not an acceptable game duration!'
  assert game.select_game_length('Anya') == 'Sorry, that is not an acceptable game duration!'
  assert game.select_game_length('7') == 'Ummmmmm thats a bit long, please select again.'
  assert game.select_game_length('2') == 'You have selected first to 2 wins, good luck!'

  game.select_game_length(3)

  assert game.game_length == 3

def test_get_input():
  game = GameFlow()

  assert game.get_input('length') == 'Please select a game length: '
