import sqlite3

def clear_table():
    conn = sqlite3.connect('data/employee.db')  # adjust the path as needed
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees")  # Replace 'employees' with your table name
    conn.commit()
    conn.close()

clear_table()