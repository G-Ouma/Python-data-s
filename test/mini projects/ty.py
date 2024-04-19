import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)
    return roll


while True:
    players = input("How many players are you (2 - 4)? ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print('The number should be between 2 and 4!')
    else:
        print("Kindly input a number in your next trial.")

player_scores = [0 for _ in range(players)]
high_score = 50
top_score = max(player_scores)

while top_score < high_score:
    for player_idx in range(players):
        print("It's player " + str(player_idx + 1) + "'s turn.")
        print("Your total score is", player_scores[player_idx])
        current_score = 0

        while True:
            player_input = input("Would you like to roll (y/n) or q to quit ") 
            if player_input != "y":
                break 
            
            random_roll = roll()
            if random_roll == 1:
                print("You rolled a 1! Next turn.")
                current_score = 0
                break
            else:
                print("You rolled a", random_roll)
                current_score += random_roll
            print("Your score for this turn is:", current_score)
        player_scores[player_idx] += current_score
            
        
        
