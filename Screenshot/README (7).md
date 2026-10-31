# Datheon Python Programming Internship

Submission for the Datheon Python Programming Internship.

## Task 1: Hangman (terminal game)

A console Hangman game: guess the hidden word letter by letter within 6 mistakes.

### Features
- Random word chosen with `random.choice()`
- Masked word display (e.g. `_ A _ H O N`)
- ASCII gallows art that updates after each wrong guess
- Guessed letters tracked in sets; repeated or invalid input costs no life
- Clear win and game-over screens, score tracking, play-again option
- Uses a `words.txt` list if present, otherwise a built-in word list

### Run
```bash
python hangman.py
```
Optional: download the [English words list](https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt) and save it as `words.txt` next to `hangman.py`.

### Requirements
Python 3 only (standard library: `random`, `os`).

## Folder structure
```
Datheon_Python_Programming_Internship/
├── README.md
├── hangman.py
└── words.txt   (optional)
```
