
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
        
LotteryGame()
