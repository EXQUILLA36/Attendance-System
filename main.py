from flask import Flask, request, jsonify
from flask_cors import CORS
from addEmp import addEmployee
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_employee_with_image(name, emp_id, rate, image_blob):
    conn = sqlite3.connect('data/employee.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO employees (id, name, rate, date, photo)
        VALUES (?, ?, ?, ?, ?)
    ''', (emp_id, name, rate, datetime.now(), image_blob))
    conn.commit()
    conn.close()

@app.route('/api/upload', methods=['POST'])
def upload_photo():
    # Get form fields
    name = request.form.get('employeeName')
    emp_id = request.form.get('employeeId')
    rate = request.form.get('employeeRate')

    if not name or not emp_id or not rate:
        return jsonify({"error": "Missing employee info"}), 400

    if 'photo' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['photo']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    image_blob = file.read()

    try:
        save_employee_with_image(name, emp_id, rate, image_blob)
        return jsonify({"message": "Employee and photo saved successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to save data"}), 500


    @app.route('/')
    def index():
        return "Server is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)