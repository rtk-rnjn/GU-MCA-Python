# Program to read or write CSV file

import csv


def read_csv_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        return list(csv.reader(file))


def write_csv_file(file_name: str, data: list) -> None:
    with open(file_name, "w") as file:
        csv.writer(file).writerows(data)


if __name__ == "__main__":
    file_name = input("Enter file name: ")
    data = read_csv_file(file_name)
    print(data)
