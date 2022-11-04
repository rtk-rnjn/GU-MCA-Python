# Program to count odd even in the list


def odd_even_count(numbers: list) -> tuple[int, int]:
    odd = 0
    even = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


if __name__ == "__main__":
    numbers = [int(num) for num in input("Enter numbers: ").split()]
    odd, even = odd_even_count(numbers)
    print("Odd numbers in given list are", odd)
    print("Even numbers in given list are", even)
