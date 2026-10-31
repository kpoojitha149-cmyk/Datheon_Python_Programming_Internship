

import os
import random

MAX_MISTAKES = 6
MIN_WORD_LENGTH = 4
WORDS_FILE = "words.txt"

FALLBACK_WORDS = [
    "python", "internship", "variable", "function", "algorithm", "database",
    "network", "keyboard", "compiler", "software", "developer", "terminal",
    "repository", "debugging", "iteration", "dictionary", "program", "library",
]

# One ASCII picture per number of mistakes (0 to 6)
HANGMAN_STAGES = [
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


def load_words():
    """Load words from words.txt if present, otherwise use the built-in list."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), WORDS_FILE)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            words = [w.strip().lower() for w in f
                     if w.strip().isalpha() and len(w.strip()) >= MIN_WORD_LENGTH]
        if words:
            return words
    return FALLBACK_WORDS


def masked_word(word, correct_letters):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(ch.upper() if ch in correct_letters else "_" for ch in word)


def show_status(word, correct_letters, wrong_letters):
    mistakes = len(wrong_letters)
    print(HANGMAN_STAGES[mistakes])
    print(f"\n  Word:   {masked_word(word, correct_letters)}")
    print(f"  Wrong:  {' '.join(sorted(l.upper() for l in wrong_letters)) or '-'}")
    print(f"  Lives left: {MAX_MISTAKES - mistakes}\n")


def get_guess(guessed):
    """Ask for a single new letter. Repeats/invalid input never cost a life."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  Please enter a single letter (A-Z).")
        elif guess in guessed:
            print(f"  You already guessed '{guess.upper()}'. No penalty - try another.")
        else:
            return guess


def play_round(word):
    correct_letters = set()
    wrong_letters = set()

    print("\n=== HANGMAN ===")
    print(f"I'm thinking of a {len(word)}-letter word.")

    while True:
        show_status(word, correct_letters, wrong_letters)

        if set(word) <= correct_letters:
            print("*" * 34)
            print(f"  YOU WIN!  The word was: {word.upper()}")
            print("*" * 34)
            return True
        if len(wrong_letters) >= MAX_MISTAKES:
            print("x" * 34)
            print(f"  GAME OVER. The word was: {word.upper()}")
            print("x" * 34)
            return False

        guess = get_guess(correct_letters | wrong_letters)
        if guess in word:
            correct_letters.add(guess)
            print(f"  Good guess! '{guess.upper()}' is in the word.")
        else:
            wrong_letters.add(guess)
            print(f"  Sorry, '{guess.upper()}' is not in the word.")


def main():
    words = load_words()
    wins = losses = 0
    while True:
        if play_round(random.choice(words)):
            wins += 1
        else:
            losses += 1
        print(f"\nScore -> Wins: {wins}  Losses: {losses}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
