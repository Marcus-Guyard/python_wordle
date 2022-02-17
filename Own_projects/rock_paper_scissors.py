import random


def rock_paper_scissors():
    game = True
    options_list = ["Rock", "Paper", "Scissors"]

    score_p = 0
    score_r = 0

    best_of = int(input("Best of: "))

    while game:
        num = 1
        for i in options_list:
            print(f"[{num}]. {i}")
            num += 1

        player = input(">> ")
        player = options_list[int(player) - 1]

        r = random.randint(0, 2)
        r = options_list[r]

        if player == r:
            print(f"{player} -- {r}")
            print("***Draw***")

        if player == "Rock" and r == "Paper":
            print(f"{player} -- {r}")
            score_r += 1
            cp_win(score_p, score_r)

        if player == "Rock" and r == "Scissors":
            print(f"{player} -- {r}")
            score_p += 1
            player_win(score_p, score_r)

        if player == "Scissors" and r == "Paper":
            print(f"{player} -- {r}")
            score_p += 1
            player_win(score_p, score_r)

        if player == "Paper" and r == "Scissors":
            print(f"{player} -- {r}")
            score_r += 1
            cp_win(score_p, score_r)

        if r == "Rock" and player == "Paper":
            print(f"{player} -- {r}")
            score_p += 1
            player_win(score_p, score_r)

        if r == "Rock" and player == "Scissors":
            print(f"{player} -- {r}")
            score_r += 1
            cp_win(score_p, score_r)

        game = rounds(best_of, game, score_p, score_r)


def rounds(best_of, game, score_p, score_r):
    if best_of % 2 == 0:
        if score_p == ((best_of / 2) + 1) or score_r == ((best_of / 2) + 1):
            print(f"\nScore is: {score_p} - {score_r}")
            if score_p < score_r:
                print(f"*****CP WINS!!*****")
            if score_p > score_r:
                print(f"*****YOU WIN!!*****")
            game = False

    else:
        if score_p == ((best_of / 2) + 0.5) or score_r == ((best_of / 2) + 0.5):
            print(f"\nScore is: {score_p} - {score_r}")
            if score_p < score_r:
                print(f"*****CP WINS!!*****")
            if score_p > score_r:
                print(f"*****YOU WIN!!*****")
            game = False
    return game


def player_win(score_p, score_r):
    if score_p < score_r:
        print(f"You win, Score is: {score_p} - {score_r} to CP")
    if score_p > score_r:
        print(f"You win, Score is: {score_p} - {score_r} to You")
    if score_p == score_r:
        print(f"You win, Score is: {score_p} - {score_r}")


def cp_win(score_p, score_r):
    if score_p < score_r:
        print(f"CP wins, Score is: {score_p} - {score_r} to CP")
    if score_p > score_r:
        print(f"CP wins, Score is: {score_p} - {score_r} to You")
    if score_p == score_r:
        print(f"CP wins, Score is: {score_p} - {score_r}")


if __name__ == '__main__':
    rock_paper_scissors()