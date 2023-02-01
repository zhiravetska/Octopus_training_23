import random

comGuess = random.randint(0,100)
while True:
    userGuess = int(input("Guess a number between 0 - 100: "))
    if userGuess>comGuess:
        print("Cuess lower")
    elif userGuess<comGuess:
        print("Guess higher")    
    else:
        print("Congrats, You've guessed the correct number!")
        break