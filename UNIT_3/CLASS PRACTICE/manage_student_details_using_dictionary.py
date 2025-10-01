# Manage Student Details using Dictionary

students = {}
while True:
    print("1. Add student")
    print("2. Display students")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
    elif choice == '2':
        for name, marks in students.items():
            print(f"{name}: {marks}")
    elif choice == '3':
        break
    else:
        print("Invalid choice")