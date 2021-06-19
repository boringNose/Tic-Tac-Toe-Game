import random, sys

"""
    Author: Gurdeep Singh
    Made on: June 20, 2021
"""


def board(turn, comp_symbol, player_symbol):
    if turn != "":
        if turn == players[0]:
            pos = random.randrange(1, 10, 1)
            while pos not in position_list:
                pos = random.randrange(1, 10, 1)
            get_index(pos, comp_symbol)
        else:
            pos = int(input("Enter a position from 1 to 9: "))
            while pos not in position_list:
                pos = int(input(f"Position {pos} occupied!\nChoose other location: "))
            get_index(pos, player_symbol)
        position_list.remove(pos)

    for i in range(len(positions)):
        print("   |   |   \n {} | {} | {} \n   |   |   ".format(positions[i][0], positions[i][1], positions[i][2]))
        if i != 2:
            print("-----------")
    print("======================================")

    winner_symbol = check_row()
    if winner_symbol is not None:
        select_winner(winner_symbol, comp_symbol)

    winner_symbol = check_column()
    if winner_symbol is not None:
        select_winner(winner_symbol, comp_symbol)

    winner_symbol = check_diagonal()
    if winner_symbol is not None:
        select_winner(winner_symbol, comp_symbol)


def check_row():
    for index in range(len(positions)):
        count = positions[index].count(positions[index][0])
        symbol = positions[index][0]
        if count == 3:
            return symbol


def check_column():
    for index in range(len(positions)):
        symbol = positions[0][index]
        if positions[1][index] == symbol and positions[2][index] == symbol:
            return symbol


def check_diagonal():
    for index in range(len(positions)):
        symbol = positions[0][index]
        if index == 0:
            if positions[1][1] == symbol and positions[2][2] == symbol:
                return symbol
        elif index == 1:
            continue
        else:
            if positions[1][1] == symbol and positions[2][0] == symbol:
                return symbol


def select_winner(win_symbol, computer_symbol):
    if computer_symbol == win_symbol:
        print(f"{players[0]} wins!")
    else:
        print(f"{players[1]} wins")
    print("======================================")
    for x in range(len(positions)):
        print(positions[x])
    sys.exit()  # Stops the execution


def get_index(n, symbol):
    for num in range(len(positions)):
        if n in positions[num]:
            index = positions[num].index(n)
            positions[num][index] = symbol
            break


def select_turn():
    """
    Randomly selects a player from the players tuple to select who will play first
    :return: Player name that will take first turn
    """
    start_with = random.choice(players)  # selects a player randomly
    if start_with == player_name:
        print(f"{player_name} goes First!")
        return player_name
    else:
        print(f"{players[0]} goes First!")
        return players[0]


def select_symbol(p):
    """
    Selects the symbols for the players. Player that will go first will always have symbol x and
    other player will take symbol 0
    :param p:
    :return: Symbols for both the players
    """
    if p == player_name:
        player_choice = "x"
        computer_choice = "0"
    else:
        player_choice = "0"
        computer_choice = "x"
    return computer_choice, player_choice


positions = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]   # locations or positions on the board
position_list = [num for num in range(1, 10)]   # remove values from it for the location that has been filled

board("", "", "")  # displays the board
print(f"Numbers here display the location on the board.")

player_name = input("Enter your name to play a game: ")
players = ("computer", player_name)

first_turn = select_turn()   # selects who will go first
comp, player = select_symbol(first_turn)
print(f"{players[0]}: {comp} and {players[1]}: {player}")

for num in range(1, 10):
    board(first_turn, comp, player)
    if first_turn == players[0]:
        first_turn = players[1]
    else:
        first_turn = players[0]

