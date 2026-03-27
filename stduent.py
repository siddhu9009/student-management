students = []

def add_student(name, age, grade):
    students.append({
        "name": name,
        "age": age,
        "grade": grade
    })
    print(f"Student {name} added!")

def show_students():
    if len(students) == 0:
        print("No students found!")
    else:
        print("\nStudent List:")
        for s in students:
            print(f"Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

def delete_student(name):
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print(f"Student {name} deleted!")
            return
    print("Student not found!")

def search_student(name):
    for s in students:
        if s["name"] == name:
            print("Student Found:", s)
            return
    print("Student not found!")

def update_student(name):
    for s in students:
        if s["name"] == name:
            s["age"] = int(input("Enter new age: "))
            s["grade"] = input("Enter new grade: ")
            print("Student updated!")
            return
    print("Student not found!")

# Menu
while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        add_student(name, age, grade)

    elif choice == "2":
        show_students()

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_student(name)

    elif choice == "4":
        name = input("Enter name to search: ")
        search_student(name)

    elif choice == "5":
        name = input("Enter name to update: ")
        update_student(name)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")