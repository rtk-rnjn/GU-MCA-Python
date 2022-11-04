# Program to check if a string is palindrome or not


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


if __name__ == "__main__":
    string = input("Enter a string: ")
    if is_palindrome(string):
        print("String is palindrome")
    else:
        print("String is not palindrome")
