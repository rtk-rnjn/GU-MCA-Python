# To find prime numbers in given interval


def prime_numbers(start: int, end: int) -> list:
    return [num for num in range(start, end + 1) if all(num % i for i in range(2, num))]


if __name__ == "__main__":
    start = int(input("Enter start of interval: "))
    end = int(input("Enter end of interval: "))
    print("Prime numbers in given interval are", prime_numbers(start, end))
