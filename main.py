import random
def import_words(file):
    with open(file,'r') as f:
        words = f.read().splitlines() 
    return words

# Hangman stages (ASCII art for wrong guesses)
HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]
words = import_words("words.txt")
word = random.choice(words)
guessed_letters = set()
tries = len(HANGMAN_PICS) - 1  
wrong_guesses = 0
won = False

print("Welcome to Hangman!")
print(HANGMAN_PICS[wrong_guesses])
print("_ " * len(word))

while wrong_guesses < len(HANGMAN_PICS) - 1:

    guess = input("Guess a letter: ").lower()  
    
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
        wrong_guesses += 1
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

    # Show hangman stage
    print(HANGMAN_PICS[wrong_guesses])

    # Showing the current word status
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

    if "_" not in display:
        won = True
        break

if won:
    print("You won! The word you guessed:", word)
else:
    print("Game over! The word was:", word)
