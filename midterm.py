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

    :param character: a one dimensional list containing the character's current status
    :param direction: an integer representing a specific direction, 1 = north, 2 = south, 3 = west, 4 = east
    :precondition: character list must contains character's current x and y position, its heal and name in order;
    direction must be one of 1, 2, 3, 4
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


def validate_and_move(character, direction, board):
    """Validate a move and move a character

    Validate if a move is valid, perform the move if it is valid

    :param character: a one dimensional list containing the character's current status
    :param direction: an integer representing a specific direction, 1 = north, 2 = south, 3 = west, 4 = east
    :param board: a two dimensional list representing the whole dungeon
    :precondition: character list must contains character's current x and y position, its heal and name in order;
    direction must be one of 1, 2, 3, 4; board has to be a list which contains five [1,2,3,4,5] as its element.
    :postcondition: Correctly validate a move; perform the corresponding move if it is valid
    :return: True if the move is valid; Otherwise reture False

    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 1, test_board)
    False
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 2, test_board)
    True
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 3, test_board)
    False
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 4, test_board)
    True
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 'wasd', test_board)
    Sorry, I can't understand you.
    False
    """

    directions = (1, 2, 3, 4)
    if direction in directions:
        initial_position_x = character[0]
        initial_position_y = character[1]
        move_character(character, direction)
        if character[0] not in range(1, len(board[0]) + 1):
            character[0] = initial_position_x
            return False
        elif character[1] not in range(1, len(board) + 1):
            character[1] = initial_position_y
            return False
        else:
            return True
    else:
        print("Sorry, I can't understand you.")
        return False


def health_regen(character):
    """
    Regenerate Player's health points if they are in range(1, 9).
    
    :param character: a 1D list representing player's status
    :precondition: character[2], aka player's health, must be in range(1, 9)
    :postcondition: player's HP will +2 if they are in range(1, 8),+1 if they are 9
    :return: None
    >>> test_character = [2, 3, 6, 'test_player']   
    >>> health_regen(test_character)
    >>> print(test_character)
    [2, 3, 8, 'test_player']
    >>> test_character = [2, 3, 9, 'test_player']   
    >>> health_regen(test_character)
    >>> print(test_character)
    [2, 3, 10, 'test_player'] 
    >>> test_character = [2, 3, 10, 'test_player']   
    >>> health_regen(test_character)
    >>> print(test_character)
    [2, 3, 10, 'test_player']  
    """
    if 1 <= character[2] <= 8:
        character[2] += 2
    elif character[2] == 9:
        character[2] = 10