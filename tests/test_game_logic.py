from game import check_guess, update_score


def test_check_guess_correct():
    assert check_guess(5, 5) == "correct"


def test_check_guess_too_low():
    assert check_guess(3, 5) == "too low"


def test_check_guess_too_high():
    assert check_guess(8, 5) == "too high"


def test_update_score_correct_guess():
    assert update_score(0, True) == 10


def test_update_score_wrong_guess():
    assert update_score(10, False) == 9
