import random

print('\nWelcome to the Dice Game!\n')

def roll():
    max = 6
    min = 1
    value = random.randint(min, max)
    return value


while True:
    players = input("How many players are you (2 - 4)? ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
             break
        else:
             print("Must be between 2 and 4!")
    else:
        print("Please enter a number in your next trial.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nIt's player " +  str(player_idx + 1) + "'s turn.")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            playing = input('Would you like to roll a dice (y/n)? ')
            if playing.lower() != 'y':
                break

            value_rolled = roll()
            if value_rolled == 1:
                print("You rolled a 1. Next turn!")
                current_score = 0
                break
            else:
                current_score += value_rolled
                print("You rolled a:", value_rolled)
                print("Your score is:", current_score)

        player_scores[player_idx] += current_score
       
high_score = max(player_scores)
winner = player_scores.index(high_score) + 1
print("\nPlayer", winner, "is the winner with a score of:", high_score, "\n")