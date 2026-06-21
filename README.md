# Game Glitch Investigator

## Project Overview

This project is a beginner Python debugging project. The goal was to investigate a Python game that had glitches, fix the problems, and add automated tests.

I made a number guessing game where the player guesses a number and receives hints. The game uses separate functions for checking guesses and updating the score so the logic is easier to test.

## Demo Walkthrough

To run the game:

```bash
python game.py
```

To run the tests:

```bash
python -m pytest tests
```

To save the test output:

```bash
python -m pytest tests > test_results.txt
```

## Bugs Fixed

### Bug 1: Hint Logic

The game needed a clear way to tell the player if a guess was correct, too low, or too high. I fixed this by creating a `check_guess()` function.

### Bug 2: Score Logic

The score needed to update in a simple way. I fixed this by creating an `update_score()` function. A correct guess adds 10 points, and a wrong guess subtracts 1 point.

### Bug 3: Pytest Setup

At first, pytest did not find my tests correctly. I fixed this by putting my test file inside the `tests` folder and running `python -m pytest tests`.

## Testing

My tests are located in:

```text
tests/test_game_logic.py
```

The tests check:

- correct guesses
- guesses that are too low
- guesses that are too high
- score increase after a correct guess
- score decrease after an incorrect guess

The final result was:

```text
5 passed
```

## What I Learned

I learned how to use Git, GitHub, pytest, and basic debugging strategies. I also learned that AI can help explain errors, but I still need to check the output and verify that the code actually works.
