import random


stored_num = random.randint(1, 100) # Picks a random number between 1 and 100 and stores it as the number to guess
print("I'm thinking of a number between 1 and 100, can you guess it within 10 guesses?")

for i in range(1, 11): # Asks the user to guess up to 10 times or ends if the user gets it correct
    guess = input()
    if guess.isdigit() == True: # Checks that the guess is actually a number and then proceeds with the comparison
        guess = int(guess)
        if stored_num > guess:
            print("My number is higher than that! Guess again!")
        elif stored_num < guess:
            print("My number is lower than that! Guess again!")
        else:
            break # Breaks if the correct number is guessed
    else:
        print("Sorry, guess must be an integer.")


if stored_num == guess:
    print("Congratulations! You guessed the correct answer in", i, "guesses!")
else:
    print("Sorry, you ran out of guesses. The correct answer is:", stored_num)