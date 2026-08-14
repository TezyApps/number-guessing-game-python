# Number Guessing Game

A simple Python CLI project, scaffolded with [`uv`](https://docs.astral.sh/uv/), where
the player has 7 tries to guess a randomly generated secret number between 1 and 100.

## How it was built (commit history)

1. **Project scaffolding** — `Creating a python project structure for number guessing game`
   1. Create a `.venv`
   2. `pip install uv`
   3. `uv init game`
2. **`Adding git ignore file`** — ignore `__pycache__/`, `*.py[cod]`, and `.venv/` so build
   artifacts and the virtual environment don't get committed.
3. **`Lock deps`** — `uv lock` to generate a committed `uv.lock` for reproducible builds.
4. **`Adding README.md`** / **`Move the doc one level up`** — docs added, then moved to the
   repo root.
5. **`Get name as input and print a greeting message`** — first interactive I/O with `input()`.
6. **`Level 1`** — defined a secret number and a game loop:
   1. Define a secret number
   2. Define a method to start the game: ask for a guess, compare it to the secret
      number, print a won/lost message
7. **`Adding 7 tries to guess the secret number`** — bounded the game to 7 attempts with a
   `for` loop.
8. **`trying same with while loop`** — implemented the same game with a `while` loop to
   compare both looping styles (the `while` version was later dropped in favour of the
   `for` loop).
9. **`Add hints`** — extracted guess-checking into `__guess()`, returning a `bool`, and
   added "higher/lower" hints plus input validation for out-of-range guesses.
10. **`Generate a random secret number`**
    1. Import `random` and generate the secret with `random.randint(1, 100)`
    2. Fixed a bug where the secret number was being re-generated on every guess instead
       of once per game.
11. **Error handling for non-numeric input** *(work in progress, uncommitted)* — extracted
    input reading into `__user_input()`, wrapping `int(input(...))` in a `try`/`except
    ValueError` so a non-numeric guess (e.g. `"abc"`) no longer crashes the game; it prints
    an "Invalid input" message and returns a sentinel value instead.

## How the game works

- `main()` greets the player by name, then starts the game.
- `__start_game_with_for_loop()` picks one secret number for the whole round and gives the
  player 7 tries (`for i in range(7)`), using the loop's `else` clause to detect a
  "ran out of tries" loss and reveal the secret number.
- `__guess(user_input, expected)` compares the guess to the secret number, prints a
  higher/lower hint, and returns whether the guess was correct.
- Out-of-range guesses (not between 1 and 100) are rejected and don't cost a try.

## Error handling

- `__user_input()` wraps the raw `int(input(...))` conversion in a `try`/`except
  ValueError`, so typing a non-numeric guess (e.g. `"abc"`) prints a friendly
  "Invalid input" message instead of crashing the program with an unhandled traceback.
- On invalid input, `__user_input()` returns a sentinel value (`-1`), which the game loop
  checks for and `continue`s on — an invalid guess doesn't cost the player a try.
- Out-of-range numeric guesses (outside 1–100) are handled separately by a plain range
  check rather than an exception, since converting to `int` already succeeded.

## Data types & concepts learned

- **`int`** — the secret number, tries counter, and user guesses (`int(input(...))`)
- **`bool`** — return type of `__guess()`, used to decide whether to `break` out of the loop
- **`str`** — the player's name and all the printed messages, including f-strings
  (`f"Hello {user_name} 👋..."`)
- **`None`** — the implicit return type of `main()` and the loop function, declared
  explicitly via `-> None` type hints
- **Type hints** — annotating function signatures, e.g. `def __guess(user_input: int, expected: int) -> bool`
- **`for` loops with `range()`** and the lesser-known **`for...else`** clause (the `else`
  runs only if the loop completes without `break`)
- **`while` loops** — implemented as an alternative to the `for` loop to compare styles
- **Modules** — `import random` and `random.randint(a, b)` for generating the secret number
- **Name-mangling convention** — leading double-underscore function names (`__guess`,
  `__secret_number`) to mark them as module-private
- **Control flow** — `if` / `elif` / `else`, `break`, `continue`
- **f-strings** — formatted string interpolation used throughout for game output
- **Exception handling** — `try` / `except ValueError` to gracefully handle non-numeric
  input instead of letting the program crash

## Running the game

```bash
cd game
uv run game
```

## Requirements

- Python >= 3.14 (see `game/.python-version`)
