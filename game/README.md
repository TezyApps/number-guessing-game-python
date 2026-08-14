# Number Guessing Game

A simple Python CLI project, scaffolded with [`uv`](https://docs.astral.sh/uv/).

## Setup

This project was scaffolded in the following steps (see commit history):

1. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install `uv`**

   ```bash
   pip install uv
   ```

3. **Initialize the project with `uv`**

   ```bash
   uv init game
   ```

4. **Add a `.gitignore`**

   Ignore `__pycache__/`, `*.py[cod]`, and `.venv/` so build artifacts and the
   virtual environment don't get committed.

5. **Lock dependencies**

   ```bash
   uv lock
   ```

   This generates `uv.lock`, which is committed to keep builds reproducible.

## Running the game

```bash
uv run game
```

## Requirements

- Python >= 3.14 (see `.python-version`)
