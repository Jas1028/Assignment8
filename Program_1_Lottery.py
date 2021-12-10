
import random  
import time
print("\n             --JC LOTTERY GAME--\n**A game that depends on how lucky your numbers are**")

def LotteryGame():
    GamePlay = "y"
    while GamePlay[0] == "y":
        print("\nThe lottery game will start in:\n ")
        # Countdown timer
        seconds = int(5)
        for i in range(seconds):
            print(str(seconds - i ))
            time.sleep(0.75)
        print("\nGame Started. Goodluck!")
        print("\nHello, Please enter your name: ")
        PlayerName = input()
        print("\nGood day "  + PlayerName + ". Welcome to JC Lottery Game.\n\n>>> Choose your three lucky numbers in between of 0 and 9.")
        # Create a program that ask 3 numbers (0-9) from the user.
        NumberOne = int(input("\nType your first lucky number (0-9):\n\n"))
        NumberTwo = int(input("\nType your second lucky number (0-9):\n\n"))
        NumberThree = int(input("\nType your third lucky number (0-9):\n\n"))
        # Generate 3 random winning numbers (0-9)
        FirstValue = (random.randint(0,9))
        SecondValue = (random.randint(0,9))
        ThirdValue = (random.randint(0,9))
        GuessNumberList = (NumberOne, NumberTwo, NumberThree)
        ValueList = (FirstValue, SecondValue, ThirdValue)
LotteryGame()
