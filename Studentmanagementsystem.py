# Student Management System

students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("enter your marks:"))

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student Added Successfully!")

def display_students():
    if len(students) == 0:
        print("No Student Record Found")
    else:
        print("\nStudent Records:")
        for student in students:
            print("Roll No:", student["roll"])
            print("Name:", student["name"])
            print("Marks:",student["marks"])

def search_student():
    roll = input("Enter Roll Number to Search: ")

    found = False

    for student in students:
        if student["roll"] == roll:
            print("Student Found")
            print("Roll No:", student["roll"])
            print("Name:", student["name"])
            found = True

    if found == False:
        print("Student Not Found")

while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")