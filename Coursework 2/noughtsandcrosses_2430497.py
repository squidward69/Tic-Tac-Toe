"""Imports statemnent for generating random numbers."""
import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    Prints out a Tic-Tac-Toe board.

    Parameters:
    - board (list of lists): A 2D list representing the current state of the Tic-Tac-Toe board.
      
    Returns:
    - None
    """
    print(" -----------")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print(" -----------")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print(" -----------")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print(" -----------")

def welcome(board):
    """
    Prints the welcome message and the layout of the Tic Tac Toe board.

    Parameters:
        board(list of lists): A 3x3 list representing the Tic Tac Toe Board
    
    Returns:
        None
    """
    print("Welcome to the unbetable tic tac toe game.\nThis is the layout of the game: ")
    draw_board(board)
    print("When prompted, Enter the number corrseponding to the square you want.")

def initialise_board(board):
    """
    Initializes the board with all cells set to a single space ' '.

    Parameters:
    - board (list of lists): A 2D list representing the Tic-Tac-Toe board.

    Returns:
    - list of lists: The modified board with all cells set to ' '.
    """
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            board[i][j]=' '
    return board

def get_player_move(board):
    """
    Asks the user for the cell to put the X in, and returns the row and column.

    Parameters:
    - board (list of lists): A 2D list representing the Tic-Tac-Toe board.

    Returns:
    - tuple: A tuple containing the row and column numbers chosen by the user.
    """
    valid_in=False
    while not valid_in:

        print("\n".join([" ".join(row) for row in board]))

        u_in=input("Choose yor square: ")
        try:
            u_choice=int(u_in)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        #validate user's choice
        if 1 <= u_choice <= 9:
            #calc r & c indices
            row = (u_choice - 1) // 3
            col = (u_choice -1 ) % 3

            if board[row][col]!= ' ':
                print("This spot is already taken. Please choose another.")
            else:
                board[row][col] = 'X'
                valid_in = True
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
    return row, col

def choose_computer_move(board):
    """
    Lets the computer choose a cell to put 'O' in and returns the row and column.

    Parameters:
    - board (list of lists): A 2D list representing the Tic-Tac-Toe board.

    Returns:
    - tuple: A tuple containing the row and column numbers chosen by the computer.
    """
    # Check for winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_for_win(board, 'O'):
                    return i, j
                else:
                    board[i][j] = ' '  # Undo the move

    # Check for blocking player's winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_for_win(board, 'X'):
                    board[i][j] = 'O'
                    return i, j
                else:
                    board[i][j] = ' '  # Undo the move

    # Choose a strategic position
    strategic_positions = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]
    for position in strategic_positions:
        if board[position[0]][position[1]] == ' ':
            return position

    # If no strategic positions are available, choose a random position
    available_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    row,col= random.choice(available_cells)
    return row,col


def check_for_win(board, mark):
    """
    Checks if either the player or the computer has won.

    Parameters:
    - board (list of lists): A 2D list representing the Tic-Tac-Toe board.
    - mark (str): The mark to check for ('X' for the player or 'O' for the computer).

    Returns:
    - bool: True if someone has won, False otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    """
    Checks if all cells are occupied on the Tic-Tac-Toe board.

    Parameters:
    - board (list of lists): A 2D list representing the Tic-Tac-Toe board.

    Returns:
    - bool: True if all cells are occupied, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game(board):
    """
    Plays a game of Tic-Tac-Toe.

    Parameters:
    - board (list of lists): A 2D list representing the Tic-Tac-Toe board.

    Returns:
    - int: The score of the game (-1 for computer win, 0 for draw, 1 for player win).
    """
    initialise_board(board)
    draw_board(board)

    while True:
        p_row,p_col=get_player_move(board)
        board[p_row][p_col]='X'
        print("You Played: ")
        draw_board(board)
        p_win=check_for_win(board,'X')
        if p_win:
            print("SHHH..You win!")
            return 1
        draw = check_for_draw(board)
        if draw:
            print("GiveUP! You can never win.")
            return 0

        bot_row, bot_col=choose_computer_move(board)
        board[bot_row][bot_col]='O'
        print("CPU plays: ")
        draw_board(board)
        bot_win=check_for_win(board,'O')
        if bot_win:
            print("brah! Can't win against bot kkkk")
            return -1
        draw = check_for_draw(board)
        if draw:
            return 0


def menu():
    """
    Displays the main menu options and gets user input.

    Returns:
    - str: The user's choice ('1', '2', '3', 'q').
    """
    while True:
        print("\n-------------Menu-------------")
        print("1 - Play the game")
        print("2 - Save your score in the leaderboard")
        print("3 - Load and display the leaderboard")
        print("q - End the program")

        choice=input("Enter your choice: ").strip().lower()
        if choice in ['1','2','3','q']:
            return choice
        else:
            print("invalid choice. Please try again")

def load_scores():
    '''
    Loads scores from the leaderboard.txt file.
    Returns:
        dict : A dict containing the loaded scores if the file exists, 
        otherwise returns "FileNotFound".
    '''
    if os.path.exists('leaderboard.txt'):
        with open("leaderboard.txt","r",encoding="utf-8") as file:
            json_data=file.read()
            if not json_data.strip(): #checks if it contains whitespaces or file is empty
                return {}
            return json.loads(json_data) #parse json data into python dictionary.
    else:
        return "file not found!"

def save_score(score):
    """
    Asks the player for their name and saves the current score to the file 'leaderboard.txt' 
    in the specified JSON format.
    Returns:
      the updated leaderboard data.
    """
    p_name=input("Enter king's name: ")
    try:
        with open("leaderboard.txt",'r', encoding="utf-8") as file:
            leaderboard=json.load(file)
    except FileNotFoundError:
        leaderboard={}

    leaderboard[p_name]= score
    json_data = json.dumps(leaderboard, indent=4)


    with open("leaderboard.txt",'w', encoding="utf-8") as file:
        file.write(json_data)
    print(f"Your score ({score}) has been saved under the name {p_name}.")

    return leaderboard



def display_leaderboard(leaders):
    """
    Displays the leaderboard scores.

    Parameters:
    - leaders (dict): A dictionary containing player names as keys 
      and their corresponding scores as values.

    Returns:
    - None
    """

    print("\n-------------Leaderboard-------------")
    if not leaders:
        print("Leaderboard is empty.")
    else:
        sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
        for idx, (name, score) in enumerate(sorted_leaders, start=1):
            print(f"{idx}. {name}: {score}")
