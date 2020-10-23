"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Team member: Sean Yang & Vincent Wang
"""
import random
import sys


def exit_the_game(play_input):
  if play_input.lower() == 'quit':
    print("you quit the game.")
    sys.exit()


def make_board():
  """
  create a 2D list as the board of the game.

  :precondition: BOARD_COLUMN and BOARD_ROW must be greater than 0
  :postcondition: create a 5*5 2D list 
  :return: A 2D list act as the board of the game.
  """
  board = []
  (BOARD_ROW, BOARD_COLUMN) = (5, 5)
  for column in range(1, BOARD_COLUMN +1):
    rows = []
    for row in range(1, BOARD_ROW +1):
      rows.append(row)
    board.append(rows)
  return board


def make_character(player_name, board):
  """Create a new character

  Create new character profile for new player_name
  
  :param player_name: a string
  :param board: a two dimensional list
  :precondition: board has to be a list which contains five [1,2,3,4,5] as its element.
  :postcondition: generate character profile with correct information
  :return: a list which contain the player's name, its health, start x postion and y position within board.
  
  """
  position_x = random.randint(1, len(board[0]))
  position_y = random.randint(1, len(board))
  health = 10
  return [position_x, position_y, health, player_name]