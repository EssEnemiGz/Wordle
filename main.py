"""
Wordle game with algorithms.
By: EssEnemiGz

Color code:

RED (31): NOT IN
YELLOW (33): WRONG POSITION
GREEN (32): CORRECT
"""

from typing import List

word = "HELLO"
RESET_COLOR = "\033[0m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"

def comprobation(user_input: str):
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

    print(output)

def main():
    attempts = 1
    while attempts <= 6:
        answer = input("ANSWER: ")
        answer = answer.upper()

        if answer == "EXIT":
            break

        if len(answer) != 5:
            print(f"{RED}ANSWER MUST BE 5 CHARACTERS!{RESET_COLOR}")
            continue

        comprobation(answer)
        print(f"{YELLOW}ATTEMPT: {attempts}{RESET_COLOR}")

        if answer == word:
            print(f"{GREEN}YOU WIN!{RESET_COLOR}")
            break

        attempts+=1

if __name__=="__main__":
    main()
