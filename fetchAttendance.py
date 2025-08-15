from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import base64

app = Flask(__name__)
CORS(app)

DB_PATH = 'data/employee.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, photo FROM employees ORDER BY id ASC")  # ✅ Fetch photo too
    rows = cursor.fetchall()
    conn.close()
    
    employees = []
    for r in rows:
        photo_base64 = None
        if r[2] is not None:
            photo_base64 = base64.b64encode(r[2]).decode("utf-8")
        
        employees.append({
            "id": r[0],
            "name": r[1],
            "photo": photo_base64
        })
    return employees  # ✅ Return plain list

@app.route('/api/attendance', methods=['GET'])
def employees_route():
    return jsonify(get_db_connection())  # ✅ JSONify only here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
