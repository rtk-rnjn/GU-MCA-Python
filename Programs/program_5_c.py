# Program to demonstrate working with Set


def demonstration(s: set) -> None:
    print("Set before modification", s)
    s.add(100)
    print("Set after modification", s)


if __name__ == "__main__":
    s = {1, 2, 3, 4, 5}
    demonstration(s)
    print("Set after function call", s)
