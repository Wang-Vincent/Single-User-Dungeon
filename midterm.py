"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Team member: Sean Yang & Vincent Wang
"""
import doctest
import random
import sys


def intro():

    print('You are a hardworking student in the prestigious BCIT CST program. It is the time of the year for midterm exam week again... \n \n Tonight is a Thursday night. You finished most of your midterms for other courses, leaving only one python midterm hackathon left to do on Friday. \n \n While you were studying hard for this last python midterm in your room, a mysterious voice, coming from nowhere, hypnotized you. \n \n When you finally regained your consciousness, you found out that you had been trapped inside a mysterious space with invisible walls around you. \n \n')

    print('Suddenly, you see a very handsome man with a long beard. As this man approaches you, he begins to talk: "Greeting. I am Chris. I am here to assist you, Programmer." \n \n As Handsome Chris introduces himself, he begins to explain your situation with you. \n \n')

    print('"Unfortunately, you have been trapped inside your own nightmare in perpetuity by a mysterious evil force. \n \n In order to wake up from your nightmare and make it to your midterm hackathon on time, you must follow my instructions." \n \n')

    print('"I want to play a game." \n \n Says Handsome Chris, "In this game, you are trapped inside a 5*5, 25-cell mysterious space. \n \n Here you can enter [1, 2, 3, 4] to represent the north, south, east, and west to walk around in this space. \n \n However, when you reach the edge of the space, you will be blocked by an invisible wall. \n \n You have a starting 10 health points and 1d6 attack power. \n \n Each time you take a step, you will have a 25% chance of encountering a monster named Bug that looks like a bug, smells like a bug, and buzz like a bug. \n \n The monsters have 5 health points and 1d6 attack power. \n \n When you encounter a monster, you can choose to escape or fight until one party dies. \n \n If you choose to flee, the monster has a 10% chance to stab you back and deal 1d4 damage. If you choose to fight, it will be combat to the death. \n \n Before the start of each round of the battle, a 1d20 first strike decision will be made, and the party with the larger roll will strike first. \n \n The battle is over when either one of you dies. \n \n When you are not in battle, you can get 2 points of health regeneration if you move a step without encountering any monsters. \n \n If you successfully kill 7 bug monsters and survive, you will be victorious and wake up from this nightmare. \n \n If you die, you will fail and fall into a 72-hour sleep, thus missing your midterm hackathon and weekend."')


def get_user_name():
    """Prompt users to enter their name.

    :precondition: users input must not be "quit"
    :postcondition: return users' input as string
    :return: a string of users' input
    """
    return exit_the_game(input('Tell me your name, programmer.\n').upper())


def get_user_choice():
    """Prompt users to enter the direction they wish to go.

    :precondition: users input must be one of range(1, 4) that represent north, south, west, east and not be "quit"
    :postcondition: adjust player's coordinate base on their directional input.
    :return: a list representing player's updated coordinate.
    """
    return exit_the_game(input('Tell me a number that represent the direction you want to go, programmer.\n [1 = north, 2 = south, 3 = west, 4 = east]\n'))

    
def flee_or_not():
    """Prompt users to enter Y or N to represent their wish to flee or fight.

    :precondition: users input must be Y/N and not be "quit"
    :postcondition: return "Y" or "N" as string
    :return: a string of "Y" or "N" to represent users' input
    """
    return exit_the_game(input("You want to flee like a coward? [Y/N]\n").upper())


def exit_the_game(play_input):
    """Quit the game if user enter "quit".

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
    """create a 2D list as the board of the game.

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
    :return: True if the move is valid; Otherwise reture False and print error message if needed

    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 1, test_board)
    Ah, you can't go that way.
    False
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'okopogo']
    >>> validate_and_move(test_player, 2, test_board)
    True
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [1,5,3,'okopogo']
    >>> validate_and_move(test_player, 3, test_board)
    Ah, you can't go that way.
    False
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [1,5,3,'okopogo']
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
            print("Ah, you can't go that way.")
            return False
        elif character[1] not in range(1, len(board) + 1):
            character[1] = initial_position_y
            print("Ah, you can't go that way.")
            return False
        else:
            return True
    else:
        print("Sorry, I can't understand you.")
        return False


def check_back_stab():
    """Check if player got back stabbed

    Check if the player got back stabbed by the monster, which has 10% chance to happen

    :precondition: no precondition, the function will always execute successfully
    :postcondition: return 10 in randint(1, 10) representing a 10% chance of backstabbing, otherwise it return nothing to represent false
    :return: a integer 10 if random.randint(1, 10) == 10
    """
    return random.randint(1, 10) == 10



def health_regen(character):
    """Regenerate Player's health points if they are in range(1, 9).
    
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


def check_for_monsters():
    """check if player encounter monsters when they move.

    Check if the player encounter monsters when they move, which has 25% chance to happen

    :precondition: no precondition, the function will always execute successfully
    :postcondition: return 4 in randint(1, 4) representing a 25% chance of encounter, otherwise it return nothing to represent false
    :return: a integer 4 if random.randint(1, 4) == 4
    """
    return random.randint(1, 4) == 4


def dead(character):
    """check if player is dead.

    Check if character[2], the player's health point is less than or equal to 0.

    :precondition: no precondition, the function will always execute successfully
    :postcondition: return 0 if character[2] is less than or equal to 0, otherwise it return nothing to represent false
    :return: a integer 0 if character[2] <= 0
    >>> test_character = [2, 3, 10, 'test_player']   
    >>> dead(test_character)
    False 
    >>> test_character = [2, 3, 0, 'test_player']   
    >>> dead(test_character)
    True 
    """
    return character[2] <= 0


def get_initiative():
    """Create inititive value in a combat

    Create inititive value for both player and monster
    
    :precondition: no precondition, the function will always execute successfully
    :postcondition: correctly create two inititive value for both player and monster
    :return: a list which first element representing the player's initiative value and the second representing the monster's initiative value
    """
    return [random.randint(1, 20), random.randint(1, 20)]