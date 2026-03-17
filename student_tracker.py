students = {}

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists.")
        return

    age = input("Enter age: ")
    marks = input("Enter marks: ")

    students[name] = {"age": age, "marks": marks}
    print("Student added.")

def view_students():
    if not students:
        print("No records found.")
        return

    for name, details in students.items():
        print(f"Name: {name}, Age: {details['age']}, Marks: {details['marks']}")

def update_student():
    name = input("Enter student name to update: ")

    if name not in students:
        print("Student not found.")
        return

    age = input("Enter new age: ")
    marks = input("Enter new marks: ")

    students[name] = {"age": age, "marks": marks}
    print("Student updated.")

def delete_student():
    name = input("Enter student name to delete: ")

    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()