#!/env/bin/python3

import re

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
    brd += "\n"
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

turn = 'odd'
_continue = True
player_dict = {}
"""
Initializes program from here.
Starts from accepting input from users (1 & 2), validates and
calls for verification function on each input.
Based on return value it also decides match status who won or drawn
"""
while _continue == True:
    print_board()
    if turn == 'odd':
        player_position = input("Select postion by choosing number between 1 to 9:\n")
        player_choice = input("Now enter odd number between 1 to 9:\n")
    else:
        player_position = input("Select postion by choosing number between 1 to 9:\n")
        player_choice = input("Now enter odd number between 2 to 8:\n")

    """
    Validates for digits, non repeaters, position empty
    """
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

    if turn == 'odd' and int(player_choice) in [2, 4, 6, 8]:
        print("Invalid! value should be odd number, try again")
        continue
    if turn == 'even' and int(player_choice) in [1, 3, 5, 7, 9]:
        print("Invalid! value should be odd number, try again")
        continue

    # Verifies win case and decides who is the winner
    board[player_position-1] = player_choice
    player_dict[player_position] = player_choice
    if turn == 'odd':
        is_won = verify_win_case(player_dict)
        if is_won == True:
            print("Congratulations, Player 1(odd) won!!")
            _continue = False
        turn = 'even'
    else:
        is_won = verify_win_case(player_dict)
        if is_won == True:
            print("Congratulations, Player 2(even) won!!")
            _continue = False
        turn = 'odd'
    if _continue == False:
        print_board()

