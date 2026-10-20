import sqlite3


def create_table():
    connection = sqlite3.connect("univercity.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            mark REAL,
            age INTEGER
        )
    """)

    connection.commit()
    connection.close()


def add_student():
    connection = sqlite3.connect("univercity.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, mark, age) VALUES (?, ?, ?)",
        ("Иванов", 41, 19)
    )

    connection.commit()
    connection.close()


def delete_student():
    connection = sqlite3.connect("univercity.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (1,))

    connection.commit()
    connection.close()


def update_info():
    connection = sqlite3.connect("univercity.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE students SET age = ? WHERE id = ?", (25, 3))

    connection.commit()
    connection.close()


update_info()
