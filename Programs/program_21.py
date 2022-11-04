# Program to copy all elements from one list to another list


def copy_list(source: list, destination: list) -> None:
    destination.extend(source)


if __name__ == "__main__":
    source = [1, 2, 3, 4, 5]
    destination = []
    copy_list(source, destination)
    print(destination)
