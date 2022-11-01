import string
import requests
import random
import sys
from termcolor import colored, cprint


def download_data_json() -> dict:
    """Get data from the url in a json format"""
    get_url_json = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
    return get_url_json.json()


def get_random_word():
    random_word = "".join(random.sample(five_letter_Eng_dict, k=1))
    return random_word


def get_random_word_meaning(word_search):
    random_meaning = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_search}").json()
    random_meaning = random_meaning[0]["meanings"][0]["definitions"][0]["definition"]
    return random_meaning


def start_text():
    cprint("          *****Guess The Five Letter Word*****", attrs=['bold'])
    cprint("GREEN letter = Correct letter in the correct position", attrs=['bold'])
    cprint("YELLOW letter = Correct letter in the wrong position", attrs=['bold'])
    cprint("RED letter = Used letter from alphabet", attrs=['bold'])


github_Eng_dict = download_data_json()

five_letter_Eng_dict = [c for c in github_Eng_dict if len(c) == 5]

# Make sure the random selected word is a word with a definition
real_word = False
while not real_word:
    hidden_word = get_random_word()
    test = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{hidden_word}").json()
    try:
        if test[0] == "No Definitions Found":
            print(test, hidden_word)
        elif test[0] != "No Definitions Found":
            real_word = True
    except KeyError:
        pass

alphabet = ["\033[1m" + char + "\033[0m" for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]


def main():
    turn = 0
    punctuation_condition = True
    word_game = ["_", "_", "_", "_", "_"]
    start_text()
    while turn < 6:
        print("".join(alphabet))
        player_word = input(">> ")

        # Invalid input handling
        for char in string.punctuation:
            if char in player_word:
                punctuation_condition = False
        if not punctuation_condition:
            print("Invalid input, no punctuation symbols allowed")
            continue
        if len(player_word) != 5:
            print("Invalid input, wrong amount of letters")
            continue
        if player_word not in download_data_json():
            print("Invalid input, that is not a word.")
            continue

        # Right answer handling
        if turn == 0 and player_word == hidden_word:
            print(player_word.upper())
            print(f"Definition: {get_random_word_meaning(hidden_word)}")
            return f"***Well done! FIRST TRY!***"
        if turn == 5 and player_word == hidden_word:
            print(player_word.upper())
            print(f"Definition: {get_random_word_meaning(hidden_word)}")
            return f"***Phew, that was a close one! Last Try!!***"
        if player_word == hidden_word:
            print(player_word.upper())
            print(f"Definition: {get_random_word_meaning(hidden_word)}")
            return f"***Well done! You got the word in {turn} tries!***"

        # Correct letter wrong position checking
        for c in player_word:
            if f"\033[1m{c.upper()}\033[0m" in alphabet:
                alphabet_index = alphabet.index(f"\033[1m{c.upper()}\033[0m")
                alphabet[alphabet_index] = colored(f"\033[1m{c.upper()}\033[0m", "red")
            if c in hidden_word:
                index_num = player_word.index(c)
                word_game[index_num] = colored("\033[1m" + f"{c}".upper() + "\033[0m", "yellow")

        # Correct letter right position checking
        for i, ch in enumerate(player_word):
            if ch == hidden_word[i]:
                index_num = player_word.index(ch)
                word_game[index_num] = colored("\033[1m" + f"{ch}".upper() + "\033[0m", "green")

        # Current progress tracking
        print("".join(word_game))
        word_game = ["_", "_", "_", "_", "_"]
        turn += 1

    # Out of tries print
    if turn >= 6:
        print("You did not get the word..")
        print(f"The word was: {hidden_word.upper()}")
        return f"Definition: {get_random_word_meaning(hidden_word)}"


if __name__ == '__main__':
    print(main())
