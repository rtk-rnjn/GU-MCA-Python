# Program to manage student's details using Dictionary


def add_student(d: dict, *, name: str, roll_no: int, marks: int) -> None:
    d[roll_no] = {"name": name, "marks": marks}
    print("Student added successfully")


def remove_student(d: dict, *, roll_no: int) -> None:
    d.pop(roll_no)
    print("Student removed successfully")


if __name__ == "__main__":
    d = {}
    while True:
        print("1. Add student details")
        print("2. Remove student details")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            roll_no = int(input("Enter roll number: "))
            marks = int(input("Enter marks: "))
            add_student(d, name=name, roll_no=roll_no, marks=marks)

        elif choice == 2:
            roll_no = int(input("Enter roll number: "))
            remove_student(d, roll_no=roll_no)

        elif choice == 3:
            break

        else:
            print("Invalid choice")

    print("Student details are", d)
