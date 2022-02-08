secret: str = "codes"
secret_len: int = int(len(secret))
guess: str = str(input(f"Enter a {secret_len} character word: "))

while len(guess) != len(secret):
    guess = input(f"That wasn't {secret_len} chars! Try again: ")

if len(guess) == len(secret):
    if guess != secret:
        print(str(input(f"Enter a {secret_len} character word: ")))
    else:
        print("You won in x/6 turns!")

# i: int = 0
# WHITE_BOX: str = "\U00002B1C"
# GREEN_BOX: str = "\U0001F7E9"
# YELLOW_BOX: str = "\U0001F7E8"
# emoji: str = ""
#  (under assert)  if len(char) != 1:
# return False