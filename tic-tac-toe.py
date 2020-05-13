#!/env/bin/python3

import re

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # Board size 3x3
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
        if combination.issubset(user_set):
            return True
    return False

turn = 'X'
_continue = True
x_set = set()
o_set = set()

"""
Initializes program from here.
Starts from accepting input from users (1 & 2), validates and
calls for verification function on each input.
Based on return value it also decides match status who won or drawn
"""
while _continue == True:
    print_board()
    player_choice = input("Select postion by choosing number between 1 to 9 for choice {turn}:\n".format(turn=turn))
    match = re.search(r'^\d$', player_choice)
    if match in [None, '']:
        print("Invalid!")
    else:
        player_choice = int(match.group()[0])
        if board[player_choice-1] != str(player_choice):
            print("Invalid! selected postion is not empty, try again")
            continue

        # Verifies win case and decides who is the winner
        board[player_choice-1] = turn
        if turn == 'X':
            x_set.add(player_choice)
            is_won = verify_win_case(x_set)
            if is_won == True:
                print("Congratulations, Player 1(X) won!!")
                _continue = False
            turn = 'O'
        else:
            o_set.add(player_choice)
            is_won = verify_win_case(o_set)
            if is_won == True:
                print("Congratulations, Player 2(O) won!!")
                _continue = False
            turn = 'X'
    #print(x_set)
    #print(o_set)
    if re.findall('\d+', ''.join(board)) == []:
        print("Match drawn")
        _continue = False
    if _continue == False:
        print_board()

