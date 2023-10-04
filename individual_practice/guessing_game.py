import random

# guessLimit = 10
# secretNumber = random.randint(0, 100)

def guessingGame():
    # game_run = True
    # while game_run == True:
        secretNumber = random.randint(0, 100)
        guessLimit = 10
        print("Welcome to the guessing game. You have " + str(guessLimit) + " guesses left. ")
        theirGuess = input("Enter your guess here: ")
        while theirGuess != secretNumber:
            if int(theirGuess) < int(secretNumber):
                guessLimit -= 1
                print("Too low. You have " + str(guessLimit) + " guesses left")
                theirGuess = input("Enter another guess here:")
            elif int(theirGuess) > int(secretNumber):
                guessLimit -= 1
                print("Too high. You have " + str(guessLimit) + " guesses left")
                theirGuess = input("Enter another guess here: ")
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