import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

player_scores = [0 for _ in range(players)]

for player_idx in range(players):
    print("\nPlayer number", player_idx + 1, "turn has just started!")
    print("Your total score is:", player_scores[player_idx], "\n")
    current_score = 0

    while True:
        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() != "y":
            break

        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
            print("You rolled a:", value)
            print("Your score is:", current_score)

    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])
