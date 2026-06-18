# Week 1 - student marks manager
# you type in a few subjects + marks and it works out total / average / pass or fail

import json
import os

DATA_FILE = "students.json"
PASS_MARK = 35   # anything below this in any subject = fail


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=2)


def read_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please type a number, like 85.")


def add_student(students):
    name = input("Enter student name: ")

    marks = {}
    print("Enter subjects and marks. Leave the subject empty to finish.")
    while True:
        subject = input("Subject name: ")
        if subject == "":
            break   # empty subject means we're done adding
        mark = read_number("Marks in " + subject + ": ")
        marks[subject] = mark

    if len(marks) == 0:
        print("No marks entered. Student not added.\n")
        return

    # work out the total
    total = 0
    for mark in marks.values():
        total = total + mark
    average = total / len(marks)

    # start off assuming they passed, flip to FAIL if any subject is below the pass mark
    result = "PASS"
    for mark in marks.values():
        if mark < PASS_MARK:
            result = "FAIL"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": round(average, 2),
        "result": result,
    }

    students.append(student)
    save_students(students)
    print("Saved! Total:", total, "| Average:", round(average, 2), "|", result, "\n")


def show_students(students):
    if len(students) == 0:
        print("No students yet.\n")
        return

    print("\n----- All Students -----")
    for student in students:
        print("\nName:", student["name"])
        for subject in student["marks"]:
            print("  ", subject, ":", student["marks"][subject])
        print("  Total:", student["total"])
        print("  Average:", student["average"])
        print("  Result:", student["result"])
    print()


def main():
    students = load_students()

    while True:
        print("===== Student Marks Manager =====")
        print("1. Add student")
        print("2. Show all students")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1, 2, or 3.\n")


main()
