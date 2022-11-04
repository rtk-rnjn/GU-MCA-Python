# Program to find n-th Fibonacci number


def fibonacci(num: int) -> int:
    return num if num in {0, 1} else fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Fibonacci number at position", num, "is", fibonacci(num))
