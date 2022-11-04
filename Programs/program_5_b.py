# Program to demonstrate working with Tuple


def demonstration(tu: tuple) -> None:
    print("Tuple before modification", tu)
    tu[0] = 100
    print("Tuple after modification", tu)


if __name__ == "__main__":
    tu = (1, 2, 3, 4, 5)
    demonstration(tu)
    print("Tuple after function call", tu)
