from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

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


# Bug fix tests

def test_hint_direction_with_int_secret():
    """Bug #2: Ensure hints are correct when secret stays as int (no string conversion)"""
    # Secret is 50. Guess is 60 (higher than secret).
    # Should say "Too High", not backwards.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "HIGHER" in message


def test_hint_direction_low_guess():
    """Bug #2: Ensure hints are correct for low guesses too"""
    # Secret is 50. Guess is 30 (lower than secret).
    # Should say "Too Low"
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "LOWER" in message


def test_parse_guess_valid():
    """Bug #3: Verify parse_guess correctly parses input"""
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_guess_invalid():
    """Bug #3: Verify parse_guess rejects non-numbers"""
    ok, guess, err = parse_guess("hello")
    assert ok is False
    assert guess is None
    assert err is not None


def test_difficulty_ranges():
    """Verify difficulty levels return correct ranges"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20
    
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100
    
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50
