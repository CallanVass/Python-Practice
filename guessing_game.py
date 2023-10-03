import random

guessLimit = 10
secretNumber = random.randint(0, 100)

def guessingGame():
    secretNumber = random.randint(0, 100)
    guessLimit = 10
    print("Welcome to the guessing game. You have " + int(guessLimit) + " guesses left. ")
    theirGuess = int(input("Enter your guess here:"))
    while theirGuess != secretNumber:
        if theirGuess < secretNumber:
            guessLimit -= 1
            print("Too low. You have " + int(guessLimit) + " guesses left")
            theirGuess = int(input("Enter another guess here:"))
        elif theirGuess > secretNumber:
            print("Too high")
            theirGuess = int(input("Enter another guess here:"))
        else:
            break
            
    print("Your guess was correct! Would you like to play again?")
    input("Y/N? ")
    if input == "Y" or "y":
        print("Well too bad, we haven't added this feature yet.")
    elif input == "N" or "n":
        print("Okay, enjoy your day!")
    else: 
        print("Please enter a valid value")


           

guessingGame()