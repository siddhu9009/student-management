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
        for s in students:
            print(s)

def delete_student(name):
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print(f"Student {name} deleted!")
            return
    print("Student not found!")

delete_student("Siddhu")
show_students()