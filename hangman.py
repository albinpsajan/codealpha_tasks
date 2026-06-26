import random

# Predefined word list
words = ['python', 'hangman', 'keyboard', 'random', 'variable']

MAX_TRIES = 6

def pick_word():
    return random.choice(words)

def display_word(word, guessed):
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def get_guess(guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Enter only a single letter.")
        elif not guess.isalpha():
            print("Enter a valid letter.")
        elif guess in guessed:
            print("You already guessed that letter.")
        else:
            return guess

def check_win(word, guessed):
    for letter in word:
        if letter not in guessed:
            return False
    return True

def play():
    word = pick_word()
    guessed = []
    wrong_count = 0


    while wrong_count < MAX_TRIES:
        display_word(word, guessed)
        print(f"Wrong guesses: {[l for l in guessed if l not in word]}")
        print(f"Tries left: {MAX_TRIES - wrong_count}\n")

        guess = get_guess(guessed)
        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong_count += 1
            print(f"Wrong! {MAX_TRIES - wrong_count} tries left.\n")

        if check_win(word, guessed):
            display_word(word, guessed)
            print("You won! Congratulations!")
            return

    print(f"\nGame over! The word was: '{word}'")

play()