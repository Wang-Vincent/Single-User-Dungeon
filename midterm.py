"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Team member: Sean Yang & Vincent Wang
"""
import random
import sys


def get_user_choice():
    """
    Prompt users to enter the direction they wish to go.

    :precondition: users input must be one of range(1, 4) that represent north, south, west, east and not be "quit"
    :postcondition: adjust player's coordinate base on their directional input.
    :return: a list representing player's updated coordinate.
    """
    return exit_the_game(input('Tell me a number that represent the direction you want to go, programmer.\n [1 = north, 2 = south, 3 = west, 4 = east]\n').strip().lower())


def get_user_name():
    """
    Prompt users to enter their name.

    :precondition: users input must not be "quit"
    :postcondition: return users' input as string
    :return: a string of users' input
    """
    return exit_the_game(input('Tell me your name, programmer.\n').upper())


def exit_the_game(play_input):
    """
    Quit the game if user enter "quit".

    :precondition: user must input "quit" to quit the game.
    :postcondition: quit the game if user input "quit". Otherwise return user input.
    :param play_input: user input strings.
    :return: user input string.
    """
    if play_input.lower() == 'quit':
      print("you quit the game.")
      sys.exit()
    else:
      return play_input


def make_board():
    """
    create a 2D list as the board of the game.

    :precondition: BOARD_COLUMN and BOARD_ROW must be greater than 0
    :postcondition: create a 5*5 2D list 
    :return: A 2D list act as the board of the game.
    """
    board = []
    (BOARD_ROW, BOARD_COLUMN) = (5, 5)
    for column in range(1, BOARD_COLUMN + 1):
        rows = []
        for row in range(1, BOARD_ROW + 1):
            rows.append(row)
        board.append(rows)
    return board


def make_character(player_name, board):
    """Create a new character

    Create new character profile for new player_name
    
    :param player_name: a string representing the player's name
    :param board: a two dimensional list representing the whole dungeon
    :precondition: board has to be a list which contains five [1,2,3,4,5] as its element.
    :postcondition: generate character profile with correct information
    :return: a list which contain the player's name, its health, start x postion and y position within board.
    
    """
    position_x = random.randint(1, len(board[0]))
    position_y = random.randint(1, len(board))
    health = 10
    return [position_x, position_y, health, player_name]


def move_character(character, direction):
    """Move character towards given direction

    Move character's current position by 1 towards given direction

    :param character: a one dimensional list
    :param direction: an integer represent a specific direction, 1 = north, 2 = south, 3 = west, 4 = east
    :precondition: character list must contains character's current x and y position, its heal and name in order;
    direction must one of 1, 2, 3, 4
    :postcondition: move character's position by one towards correct direction
    :return: None

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, 1)
    >>> print(test_character)
    [2, 4, 6, 'test_player']

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, 2)
    >>> print(test_character)
    [2, 2, 6, 'test_player']

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, 3)
    >>> print(test_character)
    [1, 3, 6, 'test_player']
    
    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, 4)
    >>> print(test_character)
    [3, 3, 6, 'test_player']
    """
    if direction == 1 :
        character[1] += 1
    elif direction == 2 :
        character[1] -= 1
    elif direction == 3:
        character[0] -= 1
    elif direction == 4:
        character[0] += 1