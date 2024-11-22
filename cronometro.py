def twodigit(number):
    """
    Ensures the number is limited to two digits.
    If the number is a single digit, it adds a leading zero.
    If the number is already two digits, it remains unchanged.
    """
    if 0 <= number < 10:
        return f"0{number}"  # Add leading zero for single-digit numbers
    elif 10 <= number <= 99:
        return str(number)  # Return the number as-is if it's already two digits
    else:
        raise ValueError("Number must be between 0 and 99 (inclusive).")  ##


# ^feito por ChatGPT^

from time import sleep

x = 0
y = 0
z = 0
while True:
    print(f"{twodigit(z)}:{twodigit(y)}:{twodigit(x)}")
    x = int(x) + 1
    if x == 60:
        x = 0
        y += 1
    if y == 60:
        y = 0
        z += 1
    sleep(1)
