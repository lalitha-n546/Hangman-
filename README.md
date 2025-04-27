# Hangman- project using python
import random

from words import words



# Choose a random word
word = random.choice(words)

guessed_letters = set()

tries = 10 # Max wrong guesses the user can enter in the input

print("Welcome to Hangman!")

print("_ " * len(word))


#If the tries is available to the user then check on to

while tries > 0:

    guess = input("Guess a letter: ").lower()  
    # the lower() helps to get only alphabets in lower case.

if not guess.isalpha() or len(guess) != 1:

        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct!")
    else:
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

    # Show current word status
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

    if "_" not in display:
        print("You won! The word was:", word)
        break
else:
    print("Game over! The word was:", word)
