"""EX02 - Loop practice in one-shot Wordle."""

__author__ = "730390195"

secret: str = "python"
secret_len: int = int(len(secret))
guess: str = str(input(f"What is your {secret_len} -letter guess? "))


while len(guess) != len(secret):
    guess = input(f"That was not {secret_len} letters! Try again: ")


if len(guess) == len(secret):
    if guess != secret:
        print("Not quite. Play again soon!")
    else:
        print("Woo! You got it!")

i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
exists: bool = False
j: int = 0


while i < len(secret):
    if secret[i] == guess[i]:
        emoji = emoji + GREEN_BOX
    else:
        j: int = 0
        exists: bool = False
        while (not exists) and (j < len(secret)):
            if secret[j] == guess[i]:
                exists = True
            else:
                j += 1
        if exists:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i = i + 1
print(emoji)