import sqlite3

conn = sqlite3.connect("data/employee.db")
cur = conn.cursor()
cur.execute("SELECT id, typeof(photo) FROM employees")
print(cur.fetchall())
conn.close()