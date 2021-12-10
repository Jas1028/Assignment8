
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

        # Ask the user's name
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
             
        # It will display the winning numbers
        if GuessNumberList == ValueList or GuessNumberList != ValueList:
            print(f">> Winning numbers are:\n   ({FirstValue}, {SecondValue}, {ThirdValue}).")
        # Display “Winner” if all 3 input numbers matched the generated numbers
        elif GuessNumberList == ValueList:
            print(">> You got all winning numbers. You are a Winner, Congratulations!")
        else:
        # Display ”You loss” if not
            if GuessNumberList != ValueList:
                print(">> You didn't get all winning numbers. You loss.")

        # Display ”Try again y/n” after each game
        GamePlay = input(f"\n{PlayerName}, You want to try again? (y/n): ")
        # If the user enter “y” the user will play again
        if GamePlay == "y":
            print("\n**Next Game**")
        # if “n” the program will exit.
        else:
            if GamePlay == "n":
                print(f"\nThanks for your time to play " + PlayerName +". Hope you enjoy JC Lottery Game.\n")
                exit
LotteryGame()
