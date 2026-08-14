
def secret_number() -> int:
    return 56

def start_game() -> None:
    user_input = input("Enter your guess : ")
    if int(user_input) == secret_number():
        print(f"{user_input} 🏆")
        print("Congrats, you've guessed the number correct!")
    else:
        print(f"{user_input} ❌")
        print(f"Not Quite! Please try again")

def main() -> None:
    user_name = input("What should we call you? ")
    print(f"Hello {user_name} 👋, Welcome to the 'Number Guessing Game'!")

    start_game()