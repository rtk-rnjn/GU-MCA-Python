# Program to demonstrate working with List


def demostration(ls: list) -> None:
    print("List before modification", ls)
    ls[0] = 100
    print("List after modification", ls)


if __name__ == "__main__":
    ls = [1, 2, 3, 4, 5]
    demostration(ls)
    print("List after function call", ls)
