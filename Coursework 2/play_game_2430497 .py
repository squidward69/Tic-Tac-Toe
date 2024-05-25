"""Module providing a Tic-Tac-Toe game implementation."""
from noughtsandcrosses_2430497  import *


def main():
    """
    Defines the main function for running the "Unbeatable Noughts and Crosses" game.
    
    This function initializes the game board, 
    displays the welcome message, 
    and manages the game loop.
    It allows players to play the game, 
    save their score, 
    load the leaderboard, 
    or quit the game.
    """
    board = [ ['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return

# Program execution begins here
if __name__ == '__main__':
    main()
