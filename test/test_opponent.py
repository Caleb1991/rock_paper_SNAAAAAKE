from lib.opponent import *

def test_creation():
  opp = Opponent()
  assert isinstance(opp, Opponent)

def test_wins():
  opp = Opponent(1)
  assert opp.w == 1

def test_losses():
  opp = Opponent(0, 1)
  assert opp.l == 1

def test_selections():
  opp = Opponent()
  select_hash = {
                  'rock': 0,
                  'paper': 0,
                  'scissors': 0,
                }
  assert opp.selections == select_hash

def test_inverse_selections():
  opp = Opponent()
  inverse_select_hash = {
                          'paper': 'scissors',
                          'scissors': 'rock',
                          'rock': 'paper'
                        }
  assert opp.inverse_selections == inverse_select_hash

def test_selection_probability():
  opp = Opponent()

  opp.selection_probability('rock')
  opp.selection_probability('paper')
  opp.selection_probability('scissors')
  opp.selection_probability('scissors')
  
  assert opp.selections == {
                            'paper': 1,
                            'rock': 2,
                            'scissors': 1,
                           }

def test_selections_update():
  opp = Opponent()
  opp.selections['rounds'] = 1
  opp.selections_update('rock')

  assert opp.selections['rock'] == 1

def test_make_selection():
  opp = Opponent()

  opp.selection_probability('rock')
  opp.selection_probability('paper')
  opp.selection_probability('scissors')
  opp.selection_probability('scissors')

  assert opp.make_selection() == 'rock'