#!/env/bin/python3

import re
import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # Board size 3x3
combination_list = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {4, 5, 6}, {7, 8, 9}] # rows, columns & diagnol combinations

# Print board layout
def print_board():
    brd = "\n"
    brd += "--------------\n"
    brd += "| {0} | {1} | {2} |\n".format(board[0], board[1], board[2])
    brd += "|---|---|---|\n"
    brd += "| {0} | {1} | {2} |\n".format(board[3], board[4], board[5])
    brd += "|---|---|---|\n"
    brd += "| {0} | {1} | {2} |\n".format(board[6], board[7], board[8])
    brd += "--------------\n"
    print(brd)

# Verifies winning case from current values
def verify_win_case(user_set):
    for combination in combination_list:
        if combination.issubset(user_set.keys()):
            sum_of = 0
            for i in combination:
                sum_of += user_set[i]
            if sum_of >= 15:
                return True
    return False

# Make copy of current board (with values)
def get_board_copy(dictionary):
    clone = dictionary.copy()
    return clone

"""
AI algorithm to check next move by computer to win the game
else make random move with value
"""
def make_computer_move():
    val = {}
    # Check next move by computer can win the game
    for i in range(1, 10):
        for j in range(1, 10):
            copy_dict = get_board_copy(player_dict)
            if i not in copy_dict.keys():
                if j not in copy_dict.values():
                    copy_dict[i] = j
                    did_win = verify_win_case(copy_dict)
                    if did_win == True:
                        val[i] = j
                        return val

    corner_list = [1, 3, 7, 9]
    random.shuffle(corner_list)
    side_list = [2, 4, 6, 8]
    random.shuffle(side_list)
    rangee = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(rangee)

    # Look for available empty space in corner and pick random with random value from available values
    copy_dict = get_board_copy(player_dict)
    for i in corner_list:
        if i not in copy_dict.keys():
            for j in rangee:
                if j not in copy_dict.values():
                    val[i] = j
                    return val

    # If corners are filled then look for empty in center (5)
    copy_dict = get_board_copy(player_dict)
    if 5 not in copy_dict.keys():
        for j in rangee:
            if j not in copy_dict.values():
                val[i] = j
                return val

    # If all corner and center is filled then look for all sides
    copy_dict = get_board_copy(player_dict)
    for i in side_list:
        if i not in copy_dict.keys():
            for j in rangee:
                if j not in copy_dict.values():
                    val[i] = j
                    return val
    return {}

# Randomly decide first turn either by computer or user
if random.randint(0, 1) == 1:
    turn = 'computer'
    print("\nFirst computer turn")
else:
    turn = 'user'
    print("\nYou go first")

_continue = True
player_dict = {}
"""
Initializes program from here.
Starts from accepting input from users (1 & 2), validates and
calls for verification function on each input.
Based on return value it also decides match status who won or drawn
"""
while _continue == True:
    if player_dict not in [{}] or turn == 'user': # Initially print empty board if turn is user's
        print_board()
    # Validate user input with digits, length and repeatations
    if turn == 'user':
        player_position = input("Select postion by choosing number between 1 to 9:\n")
        player_choice = input("Now enter odd number between 1 to 9:\n")

        match_position = re.search(r'^\d$', player_position)
        if match_position in [None, '']:
            print("Invalid position!")
            continue
        player_position = int(match_position.group()[0])
        if player_position in player_dict.keys():
            print("Invalid! selected postion is not empty, try again")
            continue

        match_choice = re.search(r'^\d$', player_choice)
        if match_choice in [None, '']:
            print("Invalid choice!")
            continue
        player_choice = int(match_choice.group()[0])
        if player_choice in player_dict.values():
            print("Invalid! value cannot be repeated, try again")
            continue
    else:
        computer_move_dict = make_computer_move()
        if computer_move_dict not in [None, '', {}]:
            (player_position, player_choice), = computer_move_dict.items()

    # Verifies win case and decide who is the winner
    board[player_position-1] = player_choice
    player_dict[player_position] = player_choice
    if turn == 'user':
        is_won = verify_win_case(player_dict)
        if is_won == True:
            print("Congratulations, You Won!!")
            _continue = False
        turn = 'computer'
    else:
        is_won = verify_win_case(player_dict)
        if is_won == True:
            print("Congratulations, Computer Won!!")
            _continue = False
        turn = 'user'
    if _continue == False:
        print_board()

