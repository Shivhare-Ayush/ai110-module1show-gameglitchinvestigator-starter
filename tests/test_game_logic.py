from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1 regression: hints were backwards — verify message direction is correct
def test_too_high_message_says_lower():
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected LOWER in message, got: {message}"


def test_too_low_message_says_higher():
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected HIGHER in message, got: {message}"


# Bug 3 regression: secret must never be compared as a string
def test_high_single_digit_vs_two_digit_secret():
    # "9" > "50" is True as strings, but 9 < 50 as ints — must return Too Low
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low", f"int comparison failed, got: {outcome}"


def test_check_guess_int_types_not_str():
    # Explicit type check: both args are ints, result must be correct
    outcome, message = check_guess(9, 5)
    assert outcome == "Too High"


# parse_guess sanity check (supports Bug 3 fix — confirms we always get an int)
def test_parse_guess_returns_int():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert isinstance(value, int)
    assert value == 42
