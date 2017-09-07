import random
from IPython.display import clear_output

game_board = [[None for val in range(0,3)] for item in range(0,3)]
player_status = {"player1":False,"player2":False}
player_symbols = {}
end_game = False
start_first = False

def main():

    global start_first,end_game,player_status,player_symbols,game_board

    while True:

        variables()
        setup_players()
        game_loop()
        play_again = str(input("Would you like to Play again?(y/n) "))
        play_again = play_again.lower()

        if play_again[0] == 'y':

            variables()
            continue
        else:

            print("Thanx for playing, Bye! :)")
            break


def variables():

    global start_first,end_game,player_status,player_symbols,game_board
    game_board = [[None for val in range(0, 3)] for item in range(0, 3)]
    player_status = {"player1": False, "player2": False}
    player_symbols = {}
    end_game = False
    start_first = False


def setup_players():

    global start_first, player_symbols
    print("Welcome to tic tac toe!!!\n\n")
    symbol = input("Player 1 please input Symbol(O/X): \n\n").lower()

    while True:

        if symbol.lower() == 'x':

            print("Player 2, your symbol is O\n\n")
            player_symbols["player1"] = 'x'
            player_symbols["player2"] = 'o'
            break

        elif symbol.lower() == 'o':

            print("Player 2, your symbol is X\n\n")
            player_symbols["player1"] = 'o'
            player_symbols["player2"] = 'x'
            break

        elif symbol.lower() != 'x' or symbol.lower() != 'o':
            print("Please keep answers to either X or O!")
            continue


        turn = random.randint(0, 1)

        if turn == 1:

            start_first = True
            print("Player 1 is going first!")

        else:

            print("Player 2 is going first!")


def game_loop():

    global end_game,game_board,start_first

    while True:

        if start_first:

            player = "Player1"
            player_symbol = player_symbols["player1"]

        else:

            player = "Player2"
            player_symbol = player_symbols["player2"]

        clear_output(False)

        display_board()

        check_board()

        if end_game == True :

            status_compare = False

            for player,status in player_status.items():

                if status == True:

                    print(player+" is the winner! Well Done! :)")
                    status_compare = True


            if status_compare == False:

                print("Game was a Tie -_-")
                break

            else:

                break

        val = get_input(player,player_symbol)
        x_coordinate, y_coordinate = find_coords(val)

        if game_board[y_coordinate][x_coordinate] is None:

                game_board[y_coordinate][x_coordinate] = player_symbol

        else:
            print("This position is already taken!, Please try again")
            continue

        swap_turn()

def display_board():

    print("\n\n")
    game_board_str = ""

    for row in game_board:

        for item in row:

            game_board_str += "|_"

            if item is None:

                game_board_str += "_"

            elif item is not None:

                game_board_str += str(item)

            game_board_str += "_"

        game_board_str += "|\n"

    print("\n" + game_board_str)




def check_board():

    global game_board
    total_space_count = 0
    matching_values = False

    for row in game_board:

        if not (None in row) and row[0] == row[1] == row[2]:

            matching_values = True
            set_player_status(row[0])
            break

    if not matching_values:

        for colunm_count in range(0, 3):

            found_count = 0
            symbol = None

            for row_count in range(0, 3):

                if game_board[row_count][colunm_count] is None:

                    continue

                elif symbol is None:

                    symbol = game_board[row_count][colunm_count]
                    found_count += 1
                    total_space_count += 1

                elif symbol == game_board[row_count][colunm_count]:

                    found_count += 1
                    total_space_count += 1

                else:

                    total_space_count += 1

                if found_count == 3:

                    matching_values = True
                    set_player_status(symbol)
                    break

            if matching_values == True:

                break

    if not matching_values:

        found_count = 0
        symbol = None

        for row_count in range(0, 3):

            if game_board[row_count][row_count] is None:

                break

            elif symbol is None:

                symbol = game_board[row_count][row_count]
                found_count += 1

            elif symbol == game_board[row_count][row_count]:
                found_count += 1

            if found_count == 3:

                matching_values = True
                set_player_status(symbol)
                break

    if not matching_values:

        tmp_lst = []

        for row in game_board:

            tmp_lst.append(row[::-1])



        found_count = 0
        symbol = None

        for row_count in range(0,3):

            if tmp_lst[row_count][row_count] is None:

                break

            elif symbol is None:

                symbol = tmp_lst[row_count][row_count]
                found_count += 1

            elif symbol == tmp_lst[row_count][row_count]:

                found_count += 1

            if found_count == 3:

                matching_values = True
                set_player_status(symbol)

    if total_space_count == 9 and matching_values==False:

        global end_game
        end_game = True




def get_input(player,player_symbol):

    while True:

        try:

            print("1)Top Left\n2)Top Centre\n3)Top Right\n4)Middle Left\n5)Centre\n6)Middle Right\n7)Bottom Left\n8)Bottom Centre\n9)Bottom Right" + "\n\n")
            val = input(player + ", Please select via the menu where you would like to place " + player_symbol + ":")
            val = int(val)
            if 9 >= val > 0:
                break
            else:
                print("Please enter a number between 1 and 9!")
                continue

        except Exception as e:

            print("Please enter a number between 1 and 9!")

    return val


def find_coords(val):

    y_cordinate = 0

    if 7 > val >= 4:

        y_cordinate = 1
        x_cordinate = val - 4

    elif val >= 7:

        y_cordinate = 2
        x_cordinate = val - 7

    else:

        x_cordinate = val - 1

    return x_cordinate,y_cordinate

def swap_turn():

    global start_first

    if start_first:

        start_first = False
    else:

        start_first = True

def set_player_status(symbol):

    global end_game

    for player,val in player_symbols.items():

        if val == symbol:

            player_status[player] = True


    end_game = True




if __name__=="__main__":
    main()