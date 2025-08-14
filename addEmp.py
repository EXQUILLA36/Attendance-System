import os
import sqlite3

class addEmployee:
    def __init__(self, db_name):
        self.db_name = db_name
        
        folder = "data"
        os.makedirs(folder, exist_ok=True)  # Ensure the directory exists
        
        self.db_path = os.path.join(folder, db_name)  # Full path to the database
        
        self.conn = sqlite3.connect(self.db_path)  # Store connection
        self.cursor = self.conn.cursor()           # Store cursor
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id VARCHAR PRIMARY KEY, 
                name TEXT NOT NULL, 
                rate DOUBLE NOT NULL,
                date DATE NOT NULL,
                photo BLOB
            )
        ''')
        self.conn.commit()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                employee_id VARCHAR NOT NULL, 
                date DATE NOT NULL, 
                shift_in TIME NOT NULL, 
                shift_out TIME NOT NULL,
                status TEXT NOT NULL, 
                overtime DOUBLE NOT NULL, 
                late DOUBLE NOT NULL, 
                deduction DOUBLE NOT NULL,
                additional_pay DOUBLE NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees(id)
            )
        ''')
        self.conn.commit()

    def add_employee(self, empId, name, rate, date, photo):
        self.cursor.execute('''
            INSERT INTO employees (id, name, rate, date, photo)
            VALUES (?, ?, ?, ?, ?)
        ''', (empId, name, rate, date, photo))
        self.conn.commit()
        print(f"Employee {name} added successfully.")
        
        self.cursor.execute("SELECT * FROM employees")
        result = self.cursor.fetchall()
        print(result)

    def close(self):
        self.conn.close()
