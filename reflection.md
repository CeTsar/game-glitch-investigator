# Reflection

## Revision Note

After receiving feedback, I improved this project by adding clearer bug reproduction evidence and more edge-case tests. My first version focused more on building clean functions, but this revision explains the debugging process more clearly.

---

## Bug Reproduction Evidence

### Bug 1: Inverted Hint Message

- **Triggering Input:** `guess = 3`, `answer = 5`
- **Expected Result:** `"too low"`
- **Actual Result Before Fix:** The game could give the wrong hint, such as `"too high"`.
- **Root Cause:** The comparison logic was not clearly separated, so the hint messages could be placed in the wrong branch.
- **Fix:** Refactored the hint logic into `check_guess()` so `guess < answer` returns `"too low"` and `guess > answer` returns `"too high"`.
- **Verification:** `test_check_guess_too_low` and `test_check_guess_too_high` passed.

---

### Bug 2: Score Changed Unpredictably

- **Triggering Input:** A correct guess and a wrong guess during gameplay.
- **Expected Result:** Correct guesses should add points, and wrong guesses should subtract a small amount.
- **Actual Result Before Fix:** The score logic was not easy to test or verify because it was mixed into the game loop.
- **Root Cause:** Score updates were handled inside the gameplay flow instead of being isolated in a testable function.
- **Fix:** Refactored the score logic into `update_score()` so correct guesses add 10 and wrong guesses subtract 1.
- **Verification:** `test_update_score_correct_guess` and `test_update_score_wrong_guess` passed.

---

### Bug 3: Pytest Did Not Find Tests Correctly

- **Triggering Input:** Running `python -m pytest`.
- **Expected Result:** Pytest should collect and run the automated tests.
- **Actual Result Before Fix:** At first, pytest found 0 tests. Later, it tried to read `test_results.txt` and caused an error.
- **Root Cause:** The tests needed to be placed inside the `tests` folder, and pytest needed to be run against that folder instead of scanning unrelated files.
- **Fix:** Created `tests/test_game_logic.py` and ran `python -m pytest tests`.
- **Verification:** Pytest collected the tests and all tests passed.

---

## Edge-Case Testing Added

I added tests for boundary and unusual values:

- `guess = 1`
- `guess = 10`
- `guess = 0`
- `guess = -5`
- `guess = 100`

These tests help check that the game logic still behaves correctly when the input is outside or at the edge of the normal guessing range.

---

## How Did You Use AI as a Teammate?

I used AI as a teammate by asking it to explain Git errors, pytest errors, and project structure problems. Some AI suggestions were helpful, but I still had to verify the results myself.

**One correct AI suggestion** was to move the test file into a `tests` folder and run:

```bash
python -m pytest tests
```
