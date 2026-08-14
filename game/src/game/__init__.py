
def secret_number() -> int:
    return 56

def start_game() -> None:
    print("\n Starting game")
    for i in range(7):
        print(f"\n Tries left : {7 - i}", end=" | ")
        user_input = input(f"Enter your guess : ")
        if int(user_input) == secret_number():
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

    start_game()