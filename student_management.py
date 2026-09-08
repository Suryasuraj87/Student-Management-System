import json
print("Student Management System")
print("Welcome!")

students = []
FILE_NAME = "students.json"


def load_students():
    global students

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    name = input("Enter student name: ")
    while True:
        age = input("Enter student age: ")

        if age.isdigit() and int(age) > 0:
            break

        print("Please enter a valid age!")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists!")
            return

    students.append(student)
    save_students()
    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("--------------------")
def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found.")
def update_student():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"] == name:

            while True:
                age = input("Enter new age: ")

                if age.isdigit() and int(age) > 0:
                    break

                print("Please enter a valid age!")

            student["age"] = age
            student["course"] = input("Enter new course: ")

            save_students()
            print("Student updated successfully!")
            return

    print("Student not found.")
def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"] == name:
            print("\n--- Student Found ---")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")

load_students()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. update Student")
    print("5. Search Student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid choice!")











