def is_armstrong_number(num):
    """
    Checks if a given number is an Armstrong number.

    Args:
        num: The integer to check.

    Returns:
        True if the number is an Armstrong number, False otherwise.
    """
    original_num = num
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = 0

    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits

    return sum_of_powers == original_num

number_to_check = 153
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")

number_to_check = 1634
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")

number_to_check = 123
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")