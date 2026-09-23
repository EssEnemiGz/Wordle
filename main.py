"""
Wordle game with algorithms.
By: EssEnemiGz

Color code:

RED (31): NOT IN
GREEN (32): CORRECT
YELLOW (33): WRONG POSITION
"""

from random import choice
import json

RESET_COLOR = "\033[0m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"

with open("all_words.json", "r") as aw:
    all_words = json.load(aw).get("words")
    all_words = set(all_words)

with open("words.json", "r") as w:
    words = json.load(w).get("words")
    words = set(words)
    max_idx = len(words)-1

def random_word() -> str:
    random_word = choice(tuple(words))
    return random_word

def comprobation(user_input: str, word: str) -> str:
    colors = [RED] * len(word)
    letters = list(word)

    for char in range(len(word)):
        if user_input[char] == word[char]:
            colors[char] = GREEN
            letters.remove(user_input[char])

    for char in range(len(word)):
        if colors[char] != GREEN and user_input[char] in letters:
            colors[char] = YELLOW
            letters.remove(user_input[char])

    output = ""
    for idx in range(len(word)):
        output += f"{colors[idx]}{user_input[idx]}{RESET_COLOR}"

    return output

def main() -> None:
    attempts = 1
    word = random_word()
    word = word.upper()
    while attempts <= 6:
        answer = input("ANSWER: ")
        answer = answer.upper()

        if answer == "EXIT":
            break

        if len(answer) != 5:
            print(f"{RED}ANSWER MUST BE 5 CHARACTERS!{RESET_COLOR}")
            continue

        if answer not in all_words:
            print(f"{RED}NOT VALID WORD{RESET_COLOR}")
            continue

        comprobation_o = comprobation(answer, word)
        print(comprobation_o)
        print(f"{YELLOW}ATTEMPT: {attempts}{RESET_COLOR}")

        if answer == word:
            print(f"{GREEN}YOU WIN!{RESET_COLOR}")
            break

        attempts+=1

if __name__=="__main__":
    main()
