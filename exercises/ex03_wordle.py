"""EX03 - Attempt at structured Wordle."""

__author__ = "730390195"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(guess: str, char: str) -> bool:
    """Returns True if char found in guess. Returns False otherwise."""
    assert len(char) == 1
    i: int = 0
    exists: bool = False
    while (not exists) and (i < len(guess)):
        if guess[i] == char:
            exists = True
        else:
            i += 1
    return exists


def emojified(guess: str, secret: str) -> str:
    """Emoji string of color blocks."""
    assert len(guess) == len(secret)
    emoji = ""
    i = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        else:
            box = contains_char(secret, guess[i])
            if not box:
                emoji += WHITE_BOX
            else:
                emoji += YELLOW_BOX
        i += 1
    return emoji

   
def input_guess(expected_length: int) -> str:
    """Prompts user to provide a guess of the expected length."""
    guess: str = (input(f"Enter a {expected_length} character word: "))
    while len(guess) != expected_length:
        guess = input(f"That was not {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    attempts: int = 1
    allowed_attempts: int = 6
    secret_length: int = int(len(secret))
    while attempts <= allowed_attempts:
        print(f' === Turn {attempts}/{allowed_attempts} ===')
        guess: str = (input_guess(secret_length))
        print(emojified(guess, secret))
        if guess == secret:
            print(f'You won in {attempts}/{allowed_attempts} turns!')
            attempts += 10
        attempts += 1
    if attempts == 7:
        print(f'X/{allowed_attempts} - Sorry, try again tomorrow!')


if __name__ == "__main__":
    main()
    