# Task 1: Custom Hangman Game
# Developed by: [Rishika Thakur]

import random 

words = ["future", "matrix", "player", "coding", "laptop"]

word = random.choice(words)
guessed = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("--- Welcome to Hangman Game ---")
print("Guess the word")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("please enter only aplhabet letters: ")
        continue
    if guess in guessed_letters:
        print("\nYou've already guessed that letter")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("correct")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Oops! That's incorrect. Attempts left: ",attempts)
        
    print(" ".join(guessed))

if "_" not in guessed:
    print("\nCongratulations! You win!")
    print("The word was:", word)
else:
    print("Better luck next time")
    print("The word was:", word)
