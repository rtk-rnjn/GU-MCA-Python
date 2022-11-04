# Program to search string in file


def search_string_in_file(file_name: str, string: str) -> bool:
    with open(file_name, "r") as file:
        return string in file.read()


if __name__ == "__main__":
    file_name = input("Enter file name: ")
    string = input("Enter string to search: ")
    if search_string_in_file(file_name, string):
        print("String is found in file")
    else:
        print("String is not found in file")
