import random


def check_guess(guess, answer):
    if guess == answer:
        return "correct"
    elif guess < answer:
        return "too low"
    else:
        return "too high"


def update_score(score, is_correct):
    if is_correct:
        return score + 10
    return score - 1


def play_game():
    answer = random.randint(1, 10)
    score = 0
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("Guess a number from 1 to 10.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        result = check_guess(guess, answer)

        if result == "correct":
            score = update_score(score, True)
            print("Correct! You win!")
            break
        else:
            score = update_score(score, False)
            print(result)

    print(f"The answer was {answer}.")
    print(f"Final score: {score}")


if __name__ == "__main__":
    play_game()
