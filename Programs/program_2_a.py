# Program to determine Armstrong number


def is_armstrong_number(num: int) -> bool:
    return num == sum(int(digit) ** 3 for digit in str(num))


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(
        num,
        "is an Armstrong number"
        if is_armstrong_number(num)
        else "is not an Armstrong number",
    )
