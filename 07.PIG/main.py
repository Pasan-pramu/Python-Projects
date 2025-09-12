import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score :
    should_roll = input("would you like to roll (y)")
    if should_roll.lower() != "y" :

        value = roll();

        if value == 1:
            if value == 1 :
                print (" You rolled a 1 ! Turn done!")
                break
        else:
            current_score += value
            print("You rolled  a:" , value)

print("Your score is " +    current_score);