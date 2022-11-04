# Program Class to reverse a string word by word


class ReverseString:
    def __init__(self, string: str):
        self.string = string

    def __reverse__(self):
        return " ".join(reversed(self.string.split()))

    def __str__(self):
        return f"Reverse of '{self.string}' is '{self.__reverse__()}'"


if __name__ == "__main__":
    string = input("Enter string: ")
    reverse_string = ReverseString(string)
    print(reverse_string)
