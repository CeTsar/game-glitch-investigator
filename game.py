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
