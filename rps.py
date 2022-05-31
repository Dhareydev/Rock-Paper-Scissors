
import random
while True:
    R = "rock"
    P = "paper"
    S = "scissors"
    choices = [R, P, S]

    player_choice = input("Pick one(R, P or S): ").lower()

    while player_choice not in choices:
        print("Not amongst our options, pick again!!")
        player_choice = input("Choose your Choice: ").lower()
        
    cpu_choice = random.choice(choices)

    print("Player(",player_choice,") : CPU(",cpu_choice,")")
   

    if player_choice == cpu_choice:
        print("There's a tie!!!. Play again")
    elif player_choice == R:
        if cpu_choice == P:
            print("You lose!!! Try again")
        if cpu_choice == S:
            print("You win!!! Good job")
    elif player_choice == S:
        if cpu_choice == R:
            print("You lose!!! Try again")
        if cpu_choice == P:
            print("You win!!! Good job")
    elif player_choice == P:
        if cpu_choice == S:
            print("You lose!!! Try again")
        if cpu_choice == R:
            print("You win!!! Good job")


    play_again = input("Would you like to play again (yes or no): ").lower()

    if play_again != "yes":
        break
print("You quit!!, bye")