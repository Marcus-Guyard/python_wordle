

class Game:
    start = bool

    def __init__(self):
        self.start = True
        self.a = "A"
        self.b = "B"
        self.c = "C"
        self.d = "D"
        self.e = "E"
        self.f = "F"
        self.g = "G"
        self.h = "H"
        self.i = "I"

    def play(self):
        draw_board = Board()
        while self.start:

            draw_board.draw_board()
            player_move = input("Choose your move by entering a letter: ")
            if player_move == "a":
                self.a = "X"


class Player:
    pass


class Board(Game):

    board = f"""
    -------------
    | {Game().a} | {Game().b} | {Game().c} |
    -------------
    | {Game().d} | {Game().e} | {Game().f} |
    -------------
    | {Game().g} | {Game().h} | {Game().i} |
    -------------"""

    def draw_board(self):
        print(self.board)


if __name__ == '__main__':
    import random

    def draw_board():
        print('\033[1m' + f"""
            -------------
            | {dict["a"]} | {dict["b"]} | {dict["c"]} |
            -------------
            | {dict["d"]} | {dict["e"]} | {dict["f"]} |
            -------------
            | {dict["g"]} | {dict["h"]} | {dict["i"]} |
            -------------""" + '\033[0m')


    def computer_move(dict):
        print("Player 2, make your move: ")
        corners = [dict["a"], dict["g"], dict["c"], dict["i"]]
        bdfh = [dict["b"], dict["d"], dict["f"], dict["h"]]
        key = random.choice(corners).lower()

        print(key)

        return key.lower()


    def win_con(dict):
        if dict["a"] == "X" and dict["b"] == "X" and dict["c"] == "X":
            return "Player 1 has won the game"
        if dict["d"] == "X" and dict["e"] == "X" and dict["f"] == "X":
            return "Player 1 has won the game"
        if dict["g"] == "X" and dict["h"] == "X" and dict["i"] == "X":
            return "Player 1 has won the game"
        if dict["a"] == "X" and dict["d"] == "X" and dict["g"] == "X":
            return "Player 1 has won the game"
        if dict["a"] == "X" and dict["e"] == "X" and dict["i"] == "X":
            return "Player 1 has won the game"
        if dict["b"] == "X" and dict["e"] == "X" and dict["h"] == "X":
            return "Player 1 has won the game"
        if dict["c"] == "X" and dict["f"] == "X" and dict["i"] == "X":
            return "Player 1 has won the game"
        if dict["c"] == "X" and dict["e"] == "X" and dict["g"] == "X":
            return "Player 1 has won the game"

        if dict["a"] == "O" and dict["b"] == "O" and dict["c"] == "O":
            return "Player 2 has won the game"
        if dict["d"] == "O" and dict["e"] == "O" and dict["f"] == "O":
            return "Player 2 has won the game"
        if dict["g"] == "O" and dict["h"] == "O" and dict["i"] == "O":
            return "Player 2 has won the game"
        if dict["a"] == "O" and dict["d"] == "O" and dict["g"] == "O":
            return "Player 2 has won the game"
        if dict["a"] == "O" and dict["e"] == "O" and dict["i"] == "O":
            return "Player 2 has won the game"
        if dict["b"] == "O" and dict["e"] == "O" and dict["h"] == "O":
            return "Player 2 has won the game"
        if dict["c"] == "O" and dict["f"] == "O" and dict["i"] == "O":
            return "Player 2 has won the game"
        if dict["c"] == "O" and dict["e"] == "O" and dict["g"] == "O":
            return "Player 2 has won the game"


    start = True
    dict = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I"}
    player1 = True
    while start:
        draw_board()

        if player1:
            player_move = input("Player 1, make your move: ").lower()
            if player_move not in dict.keys():
                print("Invalid input")
            if player_move == "x" or player_move == "o":
                print("That slot has already been taken")
            if player_move in dict.keys():
                dict[player_move] = "X"
                player1 = False

        elif not player1:

            # player_move = input("Player 2, make your move: ").lower()
            player_move = computer_move(dict)
            if player_move not in dict.keys():
                print("Invalid input")
            if player_move == "x" or player_move == "o":
                print("That slot has already been taken")
            if player_move in dict.keys():
                dict[player_move] = "O"
                player1 = True

        if win_con(dict) == "Player 1 has won the game":
            draw_board()
            print(win_con(dict))
            break
        if win_con(dict) == "Player 2 has won the game":
            draw_board()
            print(win_con(dict))
            break








