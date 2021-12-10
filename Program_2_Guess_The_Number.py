
import random
import time

# Print the name of game show
print("\n      --JC Guess The Number Game--\n**A game that depends on how lucky your number is**")

def GuessNumber():
    GamePlay = 'y'
    while GamePlay[0] == 'y':
        print("\nThe guess the number game will start in:\n ")
        # Countdown timer
        seconds = int(5) 
        for i in range(seconds):
            print(str(seconds - i ))
            time.sleep(0.75)
        print("\nGame Started. Goodluck!")
        # Ask the user's name
        print("\nHello, please enter your name: ")
        PlayerName = input()
        print(f"\nGood day {PlayerName}. Welcome to JC Guess the Number Game.\n\n> Choose a lucky number between 0 and 100.\n> You have 10 attempts to guess the winning number.\n\nGoodluck! {PlayerName}. ")
        # Generate 1 random number (0-100)
        WinningNumber = random.randint(0, 100) 
        # Repeat asking the user until the random number has been guessed correctly. 
        for TotalGuess in range(10): # Limit it in 10 attempts
            # Ask the user to guess the number
            GuessNum = int(input(f"\n{PlayerName}, guess the number (0-100):\n\n"))   
            # Display “Less than” if the inputed number is less than the random number
            if GuessNum < WinningNumber:
                print("\n>>> Your guess number is less than the winning number. Guess again.")
            # Display “Greater than” if the inputed number is greater than the random number
            elif GuessNum > WinningNumber:
                print("\n>>> Your guess number is greater than the winning number. Guess again.")
            else: 
                break
        # If the user guessed the winning number
        if GuessNum == WinningNumber:
            TotalGuess = TotalGuess + 1
            print(f"\nCongratulations! {PlayerName}. You guessed the winning number in {TotalGuess} attempts. ")
        else:
            # If the user didn't guess the winning number
            if GuessNum != WinningNumber:
                print(f"\nYou have no more attempts, {PlayerName}. The winning number is {WinningNumber}.")
        # Ask if the user want to play again
        GamePlay = input(f"\nPlay again? (y or n): ")
        # If the user enter “y” the user will play again
        if GamePlay == 'y':
            print("\n**Next Game**")
        else:
            # if “n” the program will exit.
            if GamePlay != 'y':
                print(f"\nThanks {PlayerName} for playing JC Guess the Number Game. Hope you enjoy!\n ")
                exit
                
GuessNumber()


