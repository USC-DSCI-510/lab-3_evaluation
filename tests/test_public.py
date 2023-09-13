import pytest

from lab3 import sum_of_squares_of_digits, is_happy_number, is_acceptable


@pytest.mark.parametrize("num, ans", [(123, 14), (987, 194), (0, 0), (-45, "Exception")])
@pytest.mark.timeout(0.03)
def test_sum_of_squares_of_digits(num, ans):
    if ans == "Exception":
        with pytest.raises(Exception):
            sum_of_squares_of_digits(num)
    else:
        assert sum_of_squares_of_digits(num) == ans


@pytest.mark.parametrize("num, ans", [(19, True), (2, False), (-45, "Exception")])
@pytest.mark.timeout(0.03)
def test_is_happy_number(num, ans):
    if ans == "Exception":
        with pytest.raises(Exception):
            is_happy_number(num)
    else:
        assert is_happy_number(num) == ans


@pytest.mark.parametrize(
    "password, ans",
    [("Pass*!123", False), ("Good*password!123", True), ("don’t try stealing my password", False)],
)
@pytest.mark.timeout(0.03)
def test_is_acceptable(password, ans):
    assert is_acceptable(password) == ans
