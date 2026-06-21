Game Glitch Investigator
Project Overview

This project is a beginner Python debugging project. The goal was to investigate a Python game that had glitches, fix the problems, and add automated tests.

I made a number guessing game where the player guesses a number from 1 to 10. The game gives hints, updates the score, and ends when the player guesses correctly or runs out of attempts.

The game uses separate functions for checking guesses and updating the score. This makes the code easier to read, debug, and test.

Demo Walkthrough

To run the game:

python game.py

To run the tests:

python -m pytest tests

To save the test output:

python -m pytest tests > test_results.txt
Bugs Fixed
Bug 1: Hint Logic

The game needed a clear way to tell the player if a guess was correct, too low, or too high.

I fixed this by creating a check_guess() function. This function returns "correct", "too low", or "too high" depending on the player's guess.

Bug 2: Score Logic

The score needed to update in a simple and predictable way.

I fixed this by creating an update_score() function. A correct guess adds 10 points, and a wrong guess subtracts 1 point.

Bug 3: Pytest Setup

At first, pytest did not find my tests correctly.

I fixed this by putting my test file inside the tests folder and running:

python -m pytest tests
Testing

My tests are located in:

tests/test_game_logic.py

The tests check that:

correct guesses return "correct"
low guesses return "too low"
high guesses return "too high"
the score increases after a correct guess
the score decreases after an incorrect guess

The final test result was:

5 passed
What I Learned

I learned how to use Git, GitHub, pytest, and basic debugging strategies.

I also learned that AI can help explain errors and suggest fixes, but I still need to check the output and verify that the code actually works.
