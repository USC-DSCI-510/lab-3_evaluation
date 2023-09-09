import pytest

from lab3 import sum_of_squares_of_digits, is_happy_number, is_acceptable


@pytest.mark.parametrize(
    "num, ans",
    [
        (1, 1),
        (11, 2),
        (111, 3),
        (-17835, "Exception"),
        (0, 0),
        (-86, "Exception"),
        (100, 1),
        (12345, 55),
        (352569878, 357),
        (-764931298, "Exception"),
        (3525999099969878, 843),
        (-659, "Exception"),
        (-4356, "Exception"),
        (98286528794279879799099969878, 1564),
        (-47385729384012481023847121356, "Exception"),
    ],
)
def test_sum_of_squares_of_digits(num, ans):
    if ans == "Exception":
        with pytest.raises(Exception):
            sum_of_squares_of_digits(num)
    else:
        assert sum_of_squares_of_digits(num) == ans


@pytest.mark.parametrize(
    "num, ans",
    [
        (0, False),
        (-7, "Exception"),
        (7, True),
        (8, False),
        (179, False),
        (23, True),
        (111, False),
        (133, True),
        (-188, "Exception"),
        (-17, "Exception"),
        (9867037441891641, False),
        (59867037441891797, True),
        (888, True),
        (8290787, False),
        (479078662705, True),
        (11113, True),
        (245428, True),
        (-8788, "Exception"),
        (54775689, False),
    ],
)
def test_is_happy_number(num, ans):
    if ans == "Exception":
        with pytest.raises(Exception):
            is_happy_number(num)
    else:
        assert is_happy_number(num) == ans


@pytest.mark.parametrize(
    "password, ans",
    [
        ("test!12", False),
        ("T3st!ngp@ssw0rd", True),
        ("Spaces Are Not Allowed", False),
        ("VeryLongPasswordWithSpecialChars12345!@#$%", False),
        ("12345678901234567890", False),
        ("ShortP@ss", False),
        ("JustText", False),
        ("12345678901234567890!@#$%", False),
        ("!@#$%67890!@#$%", False),
        ("Secure#Pass123", False),
        ("Strong$P@ssw0rd", False),
        ("My$S3cr3tP@ss", True),
        ("P@ssw0rd!1234", True),
        ("P@ssw0rd", False),
        ("   ", False),
        ("1_@m_the_grAder 0f_d$ci510", False),
    ],
)
def test_is_acceptable(password, ans):
    assert is_acceptable(password) == ans
