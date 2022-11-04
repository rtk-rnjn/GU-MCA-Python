# program to return the odd and even numbers in the given range


def odd_even(start: int, end: int) -> tuple[list, list]:
    odd = []
    even = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return odd, even


if __name__ == "__main__":
    start = int(input("Enter start of interval: "))
    end = int(input("Enter end of interval: "))
    odd, even = odd_even(start, end)
    print("Odd numbers in given interval are", odd)
    print("Even numbers in given interval are", even)
