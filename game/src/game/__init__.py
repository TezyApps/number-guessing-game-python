
import random

def __secret_number() -> int:
    return random.randint(1, 100)

def __guess(user_input: int, expected: int) -> bool:
    if user_input == expected:
        print(f"{user_input} 🏆", end= " | ")
        print("Congrats, you've guessed the number correct!")
        return True
    elif user_input > expected:
        print(f"Your guess {user_input} is greater than the target")
        print(f"{user_input} ❌", end= " | ")
        print(f"Not Quite! Please try again")
    elif user_input < expected:
        print(f"Your guess {user_input} is less than the target")
        print(f"{user_input} ❌", end= " | ")
        print(f"Not Quite! Please try again")

    return False

def __start_game_with_for_loop() -> None:
    print("\n Starting game. Enter a number between 1 and 100")
    expected = __secret_number()
    for i in range(7):
        print(f"\nTries left : {7 - i}", end=" | ")
        user_input = int(input("Enter your guess : "))
        if user_input > 0 and user_input <= 100:
            guessed_right = __guess(user_input, expected)
            if guessed_right:
                print("\n")
                break
        else:
            print("Invalid number! Please enter between 1 and 100")
            continue
    else:
        print(f"\n Game Over! Secret Number is {expected} \n")
        return

def main() -> None:
    user_name = input("What should we call you? ")
    print(f"Hello {user_name} 👋, Welcome to the 'Number Guessing Game'!")
    __start_game_with_for_loop()