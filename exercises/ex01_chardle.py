"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730390195"

character_word: str = str(input("Enter a 5-character word: "))

if len(character_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(character_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = str(input("Enter a single character: "))

if len(single_character) == 0:
    print("Error: Character must be a single character.")
    exit()
if len(single_character) > 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + str(single_character) + " in " + str(character_word))

instance: int = 0
if character_word[0] == single_character:
    print(str(single_character) + " found at index 0")
    instance = instance + 1
if character_word[1] == single_character:
    print(str(single_character) + " found at index 1")
    instance = instance + 1
if character_word[2] == single_character:
    print(str(single_character) + " found at index 2")
    instance = instance + 1
if character_word[3] == single_character:
    print(str(single_character) + " found at index 3")
    instance = instance + 1
if character_word[4] == single_character:
    print(str(single_character) + " found at index 4")
    instance = instance + 1

if instance == 1:
    print(str(instance) + " instance of " + str(single_character) + " found in " + str(character_word))
if instance > 1:
    print(str(instance) + " instances of " + str(single_character) + " found in " + str(character_word))
if instance == 0:
    print("No instances of " + str(single_character) + " found in " + str(character_word))
