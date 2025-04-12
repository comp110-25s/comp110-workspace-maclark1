"""Making my wordle assignment for EX02"""

__author__: str = "730705563"


def contains_char(overall_word: str, single_letter: str) -> bool:
    """This will see if the person got any letters correct via character and length"""
    assert len(single_letter) == 1, f"len('{single_letter}') is not 1"
    idx: int = 0
    while idx < len(overall_word):
        if overall_word[idx] == single_letter:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Code for the color of the boxes to change depending on the guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    if guess == secret:
        return GREEN_BOX
    elif contains_char(secret, guess[idx]):
        return YELLOW_BOX
    else:
        return WHITE_BOX


def input_guess(expected_length: int, guess: str) -> str:
    """This will instruct the guesser to guess the correct amount of words"""
    print(f"Enter a {expected_length} character word:")
    while expected_length == guess:
        if expected_length != guess:
            print(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turns_max: int = 6
    turns_taken: int = 0
    while turns_taken < turns_max:
        print(f"=== Turn {turns_taken}/{turns_max} ===")
        guess = input_guess
        if guess == secret:
            print(f"You won in {turns_taken}/6 turns!")
        turns_taken = turns_taken + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
