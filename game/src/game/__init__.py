
def __secret_number() -> int:
    return 56

def __start_game_with_for_loop() -> None:
    print("\n Starting game")
    for i in range(7):
        print(f"\n Tries left : {7 - i}", end=" | ")
        user_input = input(f"Enter your guess : ")
        if int(user_input) == __secret_number():
            print(f"{user_input} 🏆", end= " | ")
            print("Congrats, you've guessed the number correct!")
            break
        else:
            print(f"{user_input} ❌", end= " | ")
            print(f"Not Quite! Please try again")
    else:
        print("\n Game Over \n")

    print("\n Game Ended \n")

def __start_game_with_while_loop() -> None:
    tries = 7

    print("\n Starting game")
    while tries > 0:
        print(f"\nTries left : {tries}", end=" | ")
        tries -= 1

        user_input = input("Enter your guess : ")
        if int(user_input) == __secret_number():
            print(f"{user_input} 🏆", end= " | ")
            print("Congrats, you've guessed the number correct!")
            break
        else:
            print(f"{user_input} ❌", end= " | ")
            print(f"Not Quite! Please try again")
    else:
        print("\n Game Over \n")

    print("\n Game Ended \n")

def main() -> None:
    user_name = input("What should we call you? ")
    print(f"Hello {user_name} 👋, Welcome to the 'Number Guessing Game'!")

    # __start_game_with_for_loop()
    __start_game_with_while_loop()