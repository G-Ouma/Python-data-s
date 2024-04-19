import random

print("Welcome to Rock-Paper-scissor game!")

playing = input("Do you want to play (y/n)? ")
if playing.lower() != "y":
    quit()

print("Let's play!")

player_wins = 0
computer_wins = 0
trials = 0
options = ["r", "p", "s"]
print("r = rock, p = paper, s = scissors")
# r = rock, p = paper, s = scissors

while True:
    player_input = input("Choose r/p/s or q to quit: ").lower() 
    if player_input == 'q':
        break
    
    if player_input not in options:
         continue
    
    trials += 1
    computer_input = options[random.randint(0, 2)]
    print("Computer has picked", computer_input + ".")
    
    if player_input == 'r' and computer_input == 's':
        print("You win!")
        player_wins += 1

    elif player_input == 's' and computer_input == 'p':
            print("You win!")
            player_wins += 1

    elif player_input == 'p' and computer_input == 'r':
        print("You win!")
        player_wins += 1
    
    elif computer_input == 'r' and player_input == 's':
        print("Computer wins!")
        computer_wins += 1

    elif computer_input == 's' and player_input == 'p':
            print("Computer wins!")
            computer_wins += 1

    elif computer_input == 'p' and player_input == 'r':
        print("Computer wins!")
        computer_wins += 1

    else:
        print("pass.")

print("Goodbye!")
print("You won", player_wins,"times out of", trials, "trials.")
print("Computer won", computer_wins,"times out of", trials, "trials.")