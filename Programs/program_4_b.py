# Program to split and join a String


def split_and_join(string: str, *, spliter: str, joiner: str) -> str:
    return joiner.join(string.split(spliter))


if __name__ == "__main__":
    string = input("Enter a string: ")
    spliter = input("Enter spliter: ")
    joiner = input("Enter joiner: ")
    print(
        "Splited and joined string is",
        split_and_join(string, spliter=spliter, joiner=joiner),
    )
