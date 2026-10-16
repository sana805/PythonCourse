import random

# List of 5 predefined words
words = ["python", "computer", "program", "keyboard", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Main game loop
while incorrect_guesses < max_incorrect_guesses:
    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

    # Check if the player has guessed the whole word
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game over if the player runs out of guesses
if incorrect_guesses == max_incorrect_guesses:
    print("\nGame Over!")
    print("The word was:", word)










 ### Key concepts used

#  - random.choice()` → selects a random word.
# - **List** → stores the 5 possible words and guessed letters.
# - **While loop** → keeps the game running until the word is guessed or 6 wrong guesses occur.
# - **If-else** → checks whether guesses are valid/correct.
# - **Strings** → handles the secret word and individual letters.
# - `input()` → gets guesses from the player.
# - `all()` → checks whether every letter has been guessed.