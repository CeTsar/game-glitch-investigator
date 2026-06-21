# Reflection

## Bug Reproduction Logs

### Bug 1: Hint Logic

**What I did:**
I tested the guess-checking logic with guesses that were lower than, higher than, and equal to the answer.

**What happened:**
The game needed a clear way to decide what message to give the player after each guess.

**What I expected:**
If the guess was correct, the game should return `"correct"`. If the guess was lower than the answer, it should return `"too low"`. If the guess was higher than the answer, it should return `"too high"`.

**How I fixed it:**
I created a function called `check_guess()` to handle the hint logic. This made the game easier to read and easier to test.

---

### Bug 2: Score Logic

**What I did:**
I checked how the score changed after correct and incorrect guesses.

**What happened:**
The score logic needed to be simple and predictable.

**What I expected:**
A correct guess should increase the score, and an incorrect guess should lower the score by a small amount.

**How I fixed it:**
I created a function called `update_score()`. If the guess is correct, it adds 10 points. If the guess is wrong, it subtracts 1 point.

---

### Bug 3: Pytest Setup

**What I did:**
I tried running the tests with:

```bash
python -m pytest
```

**What happened:**
At first, pytest did not run correctly. One time it found 0 tests. Another time it tried to read `test_results.txt` and caused an error.

**What I expected:**
Pytest should find and run the tests inside my `tests` folder.

**How I fixed it:**
I created this test file:

```text
tests/test_game_logic.py
```

Then I ran:

```bash
python -m pytest tests
```

After that, pytest found 5 tests and all of them passed.

---

## AI Collaboration Reflection

I used AI to help me work through the project step by step. I asked for help setting up Git, making commits, fixing pytest errors, and understanding which files the assignment required.

One issue I ran into was accidentally running Git in the wrong folder. Git started trying to track files from my whole user folder, which caused permission warnings. With AI help, I figured out that I needed to use the `codepath` folder instead.

Another issue was that PowerShell did not recognize the `pytest` command at first. I learned to install pytest with:

```bash
python -m pip install pytest
```

Then I learned to run the tests with:

```bash
python -m pytest tests
```

I did not accept every step without checking it. I read the terminal output after each command and made sure the tests passed before committing my work. When the output showed `5 passed`, I knew the test file and game logic were working.

This project helped me understand that AI can be useful for explaining errors and suggesting fixes, but I still need to verify the results myself. I had to check the file names, make sure the project structure matched the assignment, and confirm that my GitHub repository contained the required files.

Overall, I learned more about debugging, Git, GitHub, pytest, and how to organize a Python project for submission.
