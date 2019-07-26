import random

potential_words = ["Summer", "Beach", "Pool", "Sunscreen", "Sun", "Hot", "Ice cream", "Vacation", "Travel", "Relax"]

word = random.choice(potential_words)

word = word.lower()

print(word)

current_word = []

for letters in word:
    current_word += "_"

guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    if (guess in guesses):
        print("You already guessed that letter.")
    if (len(guess) != 1):
        print("You can only guess one letter.")
    if (guess in word):
        print("You got that letter!")
        for i in range(0, len(word)):
            if word[i] == guess:
                current_word[i] = guess        
    guesses.extend([guess])
    print("You have guessed the following letters:" + str(guesses))
    print(current_word)
    fails += 1
    print("You have " + str(maxfails - fails) + " tries left!")
