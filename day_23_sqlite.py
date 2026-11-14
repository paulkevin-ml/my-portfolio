import sqlite3

DB_NAME = "students.db"


def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade INTEGER NOT NULL
            );
            """
        )
        conn.commit()


def add_student(name, grade):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, grade) VALUES (?, ?)",
            (name, grade)
        )
        conn.commit()
        return cursor.lastrowid


def list_students():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, grade FROM students ORDER BY id")
        return cursor.fetchall()


def update_student(student_id, new_name=None, new_grade=None):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        if new_name is not None:
            cursor.execute(
                "UPDATE students SET name = ? WHERE id = ?",
                (new_name, student_id)
            )

        if new_grade is not None:
            cursor.execute(
                "UPDATE students SET grade = ? WHERE id = ?",
                (new_grade, student_id)
            )

        conn.commit()


def delete_student(student_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        return cursor.rowcount


def display_students():
    students = list_students()

    if not students:
        print("No students found.")
        return

    print("\nStudents:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}")


def main():
    create_table()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            while True:
                try:
                    grade = int(input("Enter student grade: "))
                    break
                except ValueError:
                    print("Grade must be a number.")

            add_student(name, grade)
            print("Student added successfully!")

        elif choice == "2":
            display_students()

        elif choice == "3":
            students = list_students()
            if not students:
                print("No students to update.")
                continue

            display_students()

            try:
                student_id = int(input("Enter student ID to update: "))
            except ValueError:
                print("Student ID must be a number.")
                continue

            if not any(student[0] == student_id for student in students):
                print("Student ID not found.")
                continue

            new_name = input("Enter new name (press Enter to keep current): ").strip()
            new_grade_input = input("Enter new grade (press Enter to keep current): ").strip()

            if new_name:
                update_student(student_id, new_name=new_name)

            if new_grade_input:
                try:
                    update_student(student_id, new_grade=int(new_grade_input))
                except ValueError:
                    print("Grade must be a number.")

            print("Student updated successfully!")

        elif choice == "4":
            students = list_students()
            if not students:
                print("No students to delete.")
                continue

            display_students()

            try:
                student_id = int(input("Enter student ID to delete: "))
            except ValueError:
                print("Student ID must be a number.")
                continue

            if not any(student[0] == student_id for student in students):
                print("Student ID not found.")
                continue

            delete_student(student_id)
            print("Student deleted successfully!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()