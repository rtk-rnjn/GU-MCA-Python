# Program to demonstrate working with Dictionary


def demonstration(d: dict) -> None:
    print("Dictionary before modification", d)
    d[0] = 100
    print("Dictionary after modification", d)


if __name__ == "__main__":
    d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    demonstration(d)
    print("Dictionary after function call", d)
