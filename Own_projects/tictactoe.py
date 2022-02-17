import random
import string
from copy import copy


class Game:
    """
    Class that represents the game
    """
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
        self.player_in_turn = None

    def run(self):
        """"
        Method that starts up a game and asks user if they want to play again
        """
        # Here is our game loop
        while True:
            # Game setup
            self.player_selection()
            self.player_in_turn = self.player1
            self.board = Board()

            self.play()

            answer = input("Want to play again? (y/n)")
            if answer.lower() != 'y':
                # Player wants to leave. Let's exit
                break

        print("Thank you for playing Tic-Tac-Toe")

    def play(self):
        """
        Method that drives the game
        :return: None
        """
        # Start the actual game
        while True:
            self.board.draw_board()
            if self.board.move_exist():
                # Now we need to check if the player in turn is human or AI
                if not self.player_in_turn.ai_player:
                    # This is a human player
                    # Run until we get a valid input
                    while True:
                        player_choice = input(f"{self.player_in_turn.name} place your marker? Enter column and row: ")
                        if cell := self.validate_input(player_choice):
                            row, col = cell
                        else:
                            print("Invalid input.")
                            # Loop again to get new input
                            continue
                        if self.board.is_cell_empty(row, col):
                            self.board.place(self.player_in_turn.value, row, col)
                            # We are done with the move so we can exit the loop
                            break
                        else:
                            # Player select an occupied cell
                            print("That cell is taken.")
                            continue
                else:
                    # This is an AI player
                    row, col = self.player_in_turn.computer_move(self.board, self.player_in_turn.value)
                    print(f"Computer placed a marker at {chr(65 + col)}{'0' if row < 10 else ''}{row + 1}")
                    self.board.place(self.player_in_turn.value, row, col)
            else:
                print("It is a tie! Try again...")
                break
            winner = self.board.check_winner()
            if winner > 0:
                self.board.draw_board()
                print(f"{self.player_in_turn.name} is the winner!!!")
                break
            self.switch_player()

    @staticmethod
    def validate_input(player_choice: str):
        """
        Validate a user move
        :param player_choice:
        :return: Tuple of row and column to place the marker on
        """
        if len(player_choice) != 2:
            return None
        col = player_choice[0]
        row = player_choice[1:]

        # Validate the column input
        if col.isalpha() and 'A' <= col.upper() <= string.ascii_uppercase[3-1]:
            col = ord(col.upper()) - ord('A')
        else:
            return None

        # Validate row input
        if not row.isdecimal():
            return None
        row = int(row)
        if not (1 <= row <= 3):
            return None
        return row-1, col

    def player_selection(self):
        """
        Get the player names
        :return: None
        """
        while True:
            player1_name = input("Please enter name of player 1 (playing X). Enter Computer for AI opponent: ")
            if player1_name.lower() == 'computer':
                player2_name = input("Please enter name of player 2 (playing O): ")
                if player2_name.lower() != 'computer':
                    break
            else:
                player2_name = input("Please enter name of player 2 (playing O). Enter Computer for AI opponent: ")
                break
            print("Sorry. You already said that player 1 is a computer player. The second player must then be human")

        self.player1 = Player(player1_name, 1)
        self.player2 = Player(player2_name, 2)

    def switch_player(self):
        """
        Switch player in turn
        :return: None
        """
        self.player_in_turn = self.player1 if self.player_in_turn == self.player2 else self.player2


class Player:
    """
    Class that represent a player, both human and computer
    """
    def __init__(self, player_name, value):
        """
        :param player_name: The name of the player, Computer for AI player
        :param value: The numeric value to use on the board for this player
        """
        self.name = player_name
        # If the player name is computer this is an AI player
        self.ai_player = self.name.lower() == 'computer'
        self.value = value

    @staticmethod
    def computer_move(current_board, player_id):
        """
        This is the computer AI
        :param current_board: The current board with all pieces currently placed
        :param player_id: The id of the computer player
        :return: None
        """
        # First check if it is possible to win in the next move
        board = copy(current_board)
        for r, row in enumerate(board.board):
            for c, col in enumerate(row):
                if col == 0:
                    board.board[r][c] = player_id
                    if board.check_winner():
                        return r, c
                    else:
                        # Did not win on this move. Reset board
                        board = copy(current_board)
        # Then check if player can win in next move. If so block
        board = copy(current_board)
        for r, row in enumerate(board.board):
            for c, col in enumerate(row):
                if col == 0:
                    board.board[r][c] = 1 if player_id == 2 else 2
                    if board.check_winner():
                        return r, c
                    else:
                        # Did not win on this move. Reset board
                        board = copy(current_board)
        # Is a corner free? If so take it
        # To make the game more interesting let us randomize the order the computer picks corners
        positions = [(0, 0), (0, 2), (2, 0), (2, 2)]
        random.shuffle(positions)
        for row, col in positions:
            if current_board.board[row][col] == 0:
                return row, col
        mid_row = 1
        mid_col = 1
        if current_board.board[mid_row][mid_col] == 0:
            return mid_row, mid_col
        # If all other move fail, pick one at random
        while True:
            rand_row = random.randint(1, 3) - 1
            rand_col = random.randint(1, 3) - 1
            if current_board.board.is_cell_empty(rand_row, rand_col):
                return rand_row, rand_col


class Board:
    """
    Class that represent the playing board
    """
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draws the current board to the screen
        :return: None
        """
        # To make things line up we need to play with spaces
        # Print the letter labels for each column
        col_labels = "  ".join(string.ascii_uppercase[i]+" " for i in range(3))
        print("     " + col_labels)
        # Now we can print the board, row by row
        for row in range(3):
            # Draw top line for this row
            print("    " + "----" * 3)
            # Here we print the row numbers
            print(f"{row+1} ", end="")

            # Now we can work though this row, column by column
            for col in range(3):
                # First we need to decide what to print inside this cell
                # A space if it is empty, and X if player 1 has a marker here
                # and an O if it is a player 2 marker
                piece = " " if self.board[row][col] == 0 else "X" if self.board[row][col] == 1 else "O"
                # Now we print a left cell wall and the marker
                print(f"| {piece} ", end="")
            # When we are done we print the right wall for this row
            print("|")
        # We are now done, we just need to draw the final line below the last row
        print("    " + "----" * 3)

    def move_exist(self):
        """
        Check if there is any possible moves left
        :return: True if there are more moves to be made, otherwise False
        """
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return True
        return False

    def is_cell_empty(self, row, col):
        return self.board[row][col] == 0

    def place(self, value, row, col):
        """
        Place a value at row, column on board
        :param value: Value to place
        :param row: Row to place at
        :param col: Column to place at
        :return: None
        """
        self.board[row][col] = value

    @staticmethod
    def __win_indexes(n):
        """
        Generator to build the indexes for rows, columns, and diagonals
        :param n: board size
        :return: row, column index as tuple
        """
        # Rows
        for r in range(n):
            yield [(r, c) for c in range(n)]
        # Columns
        for c in range(n):
            yield [(r, c) for r in range(n)]
        # Diagonal top left to bottom right
        yield [(i, i) for i in range(n)]
        # Diagonal top right to bottom left
        yield [(i, n - 1 - i) for i in range(n)]

    def __is_winner(self, player):
        """
        Checks if a player is a winner
        :param player: Player to check
        :return: True if this is a winner, False if not
        """
        n = len(self.board)
        for indexes in self.__win_indexes(n):
            if len([1 for r, c in indexes if self.board[r][c] == player]) >= 3:
                return True
        return False

    def check_winner(self):
        """
        Check if any player has won
        :return: The value of the winner. 0 = no winner yet
        """
        if self.__is_winner(1):
            return 1
        if self.__is_winner(2):
            return 2
        return 0

    def __copy__(self):
        """
        Used by the copy function
        :return: A copy of this board
        """
        new_board = Board()
        new_board.board = []
        for row in self.board:
            new_board.board.append([value for value in row])
        return new_board


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()