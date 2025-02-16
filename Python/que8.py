import prettytable

students = []

def display_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. View Student by ID")
    print("6. Exit")

def validate_input(prompt, field_name):
    value = input(prompt).strip()
    if not value:
        print(f"{field_name} is required.")
        return None
    return value


def add_student():
    student_id = len(students) + 1
    enrollment_no = f"EN{1000 + student_id}"

    name = validate_input("Enter name: ", "Name")
    if not name: return
    email = validate_input("Enter email: ", "Email")
    if not email: return
    phone = validate_input("Enter phone: ", "Phone")
    if not phone: return
    address = validate_input("Enter address: ", "Address")
    if not address: return

    print("\nSelect Program:")
    programs = {1: "B.Tech", 2: "BBA", 3: "MCA"}
    for key, value in programs.items():
        print(f"{key}. {value}")
    program_choice = input("Choose program (1-3): ").strip()
    program = programs.get(int(program_choice), None)
    if not program:
        print("Invalid program selection.")
        return

    print("\nSelect Stream:")
    streams = {1: "Computer Science", 2: "Management", 3: "Engineering"}
    for key, value in streams.items():
        print(f"{key}. {value}")
    stream_choice = input("Choose stream (1-3): ").strip()
    stream = streams.get(int(stream_choice), None)
    if not stream:
        print("Invalid stream selection.")
        return

    student = {
        "ID": student_id,
        "Enrollment": enrollment_no,
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Address": address,
        "Program": program,
        "Stream": stream,
        "Courses": []
    }
    students.append(student)
    print("\nStudent added successfully!")

def update_student():
    student_id = input("Enter student ID to update: ").strip()
    student = next((s for s in students if str(s["ID"]) == student_id), None)
    if not student:
        print("Invalid student ID.")
        return

    print("Leave fields blank to retain current values.")
    name = input(f"Enter new name ({student['Name']}): ").strip()
    email = input(f"Enter new email ({student['Email']}): ").strip()
    phone = input(f"Enter new phone ({student['Phone']}): ").strip()

    if name:
        student["Name"] = name
    if email:
        student["Email"] = email
    if phone:
        student["Phone"] = phone

    print("\nStudent updated successfully!")

def delete_student():
    student_id = input("Enter student ID to delete: ").strip()
    global students
    students = [s for s in students if str(s["ID"]) != student_id]
    print("\nStudent deleted successfully!")

def view_all_students():
    if not students:
        print("No students available.")
        return

    table = prettytable.PrettyTable(["ID", "Enrollment", "Name", "Email", "Phone", "Address", "Program", "Stream", "Courses"])
    for s in students:
        table.add_row([s["ID"], s["Enrollment"], s["Name"], s["Email"], s["Phone"], s["Address"], s["Program"], s["Stream"], ", ".join(s["Courses"])])
    print(table)

def view_student_by_id():
    student_id = input("Enter student ID to view: ").strip()
    student = next((s for s in students if str(s["ID"]) == student_id), None)
    if not student:
        print("Invalid student ID.")
        return

    table = prettytable.PrettyTable(["Field", "Value"])
    for key, value in student.items():
        table.add_row([key, value])
    print(table)

def assign_course():
    student_id = input("Enter student ID to assign courses: ").strip()
    student = next((s for s in students if str(s["ID"]) == student_id), None)
    if not student:
        print("Invalid student ID.")
        return

    course = input("Enter course name to assign: ").strip()
    if course:
        student["Courses"].append(course)
        print("Course assigned successfully!")

while True:
    display_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        view_student_by_id()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
