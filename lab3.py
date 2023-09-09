import string


def sum_of_squares_of_digits(num: int) -> int:
    try:
        if num < 0:
            raise Exception("Invalid Input")
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit**2
            num = num // 10
        return sum
    except:
        raise Exception("Invalid Input")


def is_happy_number(num: int) -> bool:
    try:
        if num < 0:
            raise Exception("Invalid Input")

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = get_next(num)

        return num == 1
    except:
        raise Exception("Invalid Input")


def is_acceptable(password: str) -> bool:
    try:
        # Condition 1: Length between 10 and 20
        if len(password) < 10 or len(password) > 20:
            return False

        lower_count = 0
        upper_count = 0
        special_count = 0
        digit_count = 0

        allowed_special_chars = set(string.punctuation)

        for char in password:
            if char.islower():
                lower_count += 1
            elif char.isupper():
                upper_count += 1
            elif char in allowed_special_chars:
                special_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char == " ":
                continue
            else:
                return False
        if lower_count >= 1 and upper_count >= 1 and special_count >= 2 and digit_count >= 2:
            return True
        else:
            return False
    except:
        raise Exception("Invalid Input")
