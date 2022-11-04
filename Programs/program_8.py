# Program to find factorial of a number


def factorial(num: int) -> int:
    return 1 if num in {1, 0} else num * factorial(num - 1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is", factorial(num))
