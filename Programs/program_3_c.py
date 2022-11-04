# Program to sum all the elements in the list


def sum_list(numbers: list) -> int:
    return sum(numbers)


if __name__ == "__main__":
    numbers = [int(num) for num in input("Enter numbers: ").split()]
    print("Sum of all the elements in the list is", sum_list(numbers))
