def adventure_game():
    health = 3
    name = input("Type your name: ")
    print(f"Welcome {name} to this adventure! You start with {health} health points.\n")

    answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? (left/right) ").lower()

    if answer == "left":
        answer = input(
            "You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()

        if answer == "swim":
            print("You swam across and were eaten by an alligator. -1 health.")
            health -= 1
        elif answer == "walk":
            print("You walked for many miles, ran out of water. -1 health.")
            health -= 1
        else:
            print("Not a valid option. You lose 1 health.")
            health -= 1

    elif answer == "right":
        answer = input(
            "You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back) ").lower()

        if answer == "back":
            print("You go back and lose 1 health.")
            health -= 1
        elif answer == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()

            if answer == "yes":
                print("You talk to the stranger and they offer you a reward!")
                choice = input("Do you want to keep the gold or take a sword instead? (gold/sword): ").lower()
                if choice == "gold":
                    print("You become rich! 🎉 You WIN!")
                    return
                elif choice == "sword":
                    print("You take the sword and become a mighty warrior! ⚔️ You WIN!")
                    return
                else:
                    print("You hesitated and lost the chance. -1 health.")
                    health -= 1
            elif answer == "no":
                print("You ignore the stranger and they curse you. -1 health.")
                health -= 1
            else:
                print("Not a valid option. You lose 1 health.")
                health -= 1
        else:
            print("Not a valid option. You lose 1 health.")
            health -= 1
    else:
        print("Not a valid option. You lose 1 health.")
        health -= 1

    if health > 0:
        print(f"\n🎉 Congratulations {name}, you survived with {health} health left!")
    else:
        print(f"\n💀 Sorry {name}, you ran out of health. Game Over.")

# 🎮 Game loop with replay option
while True:
    adventure_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break
