# Program 15


class NegativeValueError(Exception):
    pass


class ValueTooSmallError(Exception):
    pass


class ValueTooLargeError(Exception):
    pass


UPPER_LIMIT = 100
LOWER_LIMIT = 10


def main():
    while True:
        try:
            number = input("Enter a number: ")
            if number == "exit":
                return
            number = int(number)
            if number < 0:
                raise NegativeValueError
            elif number < LOWER_LIMIT:
                raise ValueTooSmallError
            elif number > UPPER_LIMIT:
                raise ValueTooLargeError
            print("You entered", number)
        except NegativeValueError:
            print("Negative value is not allowed")
        except ValueTooSmallError:
            print("Value is too small")
        except ValueTooLargeError:
            print("Value is too large")


if __name__ == "__main__":
    main()
