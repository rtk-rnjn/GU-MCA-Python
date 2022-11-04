# Program to maintain student's data and retrieve it accordingly


def add_student(student_data: dict, student_id: int, student_name: str) -> None:
    student_data[student_id] = student_name


def remove_student(student_data: dict, student_id: int) -> None:
    student_data.pop(student_id)


def get_student_name(student_data: dict, student_id: int) -> str:
    return student_data[student_id]


def get_student_id(student_data: dict, student_name: str) -> int:
    for student_id, name in student_data.items():
        if name == student_name:
            return student_id


def get_all_students(student_data: dict) -> dict:
    return student_data


def get_all_students_by_name(student_data: dict) -> dict:
    return {name: student_id for student_id, name in student_data.items()}


def get_all_students_by_id(student_data: dict) -> dict:
    return dict(student_data)


if __name__ == "__main__":
    student_data = {}
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. Get student name")
        print("4. Get student id")
        print("5. Get all students")
        print("6. Get all students by name")
        print("7. Get all students by id")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_id = int(input("Enter student id: "))
            student_name = input("Enter student name: ")
            add_student(student_data, student_id, student_name)
            print("Student added successfully")

        elif choice == 2:
            student_id = int(input("Enter student id: "))
            remove_student(student_data, student_id)
            print("Student removed successfully")

        elif choice == 3:
            student_id = int(input("Enter student id: "))
            print("Student name is", get_student_name(student_data, student_id))

        elif choice == 4:
            student_name = input("Enter student name: ")
            print("Student id is", get_student_id(student_data, student_name))

        elif choice == 5:
            print("All students are", get_all_students(student_data))

        elif choice == 6:
            print("All students by name are", get_all_students_by_name(student_data))

        elif choice == 7:
            print("All students by id are", get_all_students_by_id(student_data))

        elif choice == 8:
            break

        else:
            print("Invalid choice")

    print("Student details are", student_data)
