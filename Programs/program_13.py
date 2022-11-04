# Copy content from one file to other


def main(file_to_read: str, file_to_write: str) -> None:
    with open(file_to_read, "r") as file1:
        with open(file_to_write, "w") as file2:
            file2.write(file1.read())


if __name__ == "__main__":
    file_to_read = input("Enter file to read: ")
    file_to_write = input("Enter file to write: ")
    main(file_to_read, file_to_write)
