import random

# ASCII art for the hangman stages
HANGMAN_PICS = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
]

# Word pool for the game
WORDS = [
    "python",
    "developer",
    "algorithm",
    "hangman",
    "variable",
    "function",
    "keyboard",
    "computer",
]


def get_random_word(word_list):
    """Selects and returns a random word from the list."""
    return random.choice(word_list).lower()


def display_game_state(incorrect_guesses, correct_guesses, secret_word):
    """Prints the current hangman stage, guessed word state, and missed letters."""
    print(HANGMAN_PICS[len(incorrect_guesses)])
    print("\nIncorrect letters:", " ".join(incorrect_guesses) if incorrect_guesses else "None")

    # Build the display string with underscores for hidden letters
    word_state = [letter if letter in correct_guesses else "_" for letter in secret_word]
    print("Word:", " ".join(word_state))
    print("-" * 30)


def get_user_guess(already_guessed):
    """Prompts for input and validates that it is a single un-guessed letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter (A-Z).")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        else:
            return guess


def play_hangman():
    """Main game loop."""
    secret_word = get_random_word(WORDS)
    correct_guesses = set()
    incorrect_guesses = set()
    max_attempts = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")

    while True:
        display_game_state(incorrect_guesses, correct_guesses, secret_word)

        # Get player guess
        already_guessed = correct_guesses | incorrect_guesses
        guess = get_user_guess(already_guessed)

        if guess in secret_word:
            correct_guesses.add(guess)

            # Check for win condition
            if all(letter in correct_guesses for letter in secret_word):
                display_game_state(incorrect_guesses, correct_guesses, secret_word)
                print(f"Congratulations! You guessed the word: '{secret_word}'!")
                break
        else:
            incorrect_guesses.add(guess)

            # Check for loss condition
            if len(incorrect_guesses) == max_attempts:
                display_game_state(incorrect_guesses, correct_guesses, secret_word)
                print(f"Game Over! The word was: '{secret_word}'.")
                break


if __name__ == "__main__":
    play_hangman()


