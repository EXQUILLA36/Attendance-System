from addEmp import addEmployee
from datetime import datetime

class attenDance:
    def __init__(self):
        self.inpEmp()
        
    def inpEmp(self):
        print("Adding employee...")
        empId = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        rate = float(input("Enter Employee Rate: "))
        date = datetime.now().date()
        
        photo_path = input("Enter Photo Path (leave blank if none): ").strip()
        photo_bytes = None

        if photo_path:
            try:
                with open(photo_path, "rb") as f:
                    photo_bytes = f.read()
            except FileNotFoundError:
                print(f"⚠️ File not found: {photo_path}")
                photo_bytes = None
        
        emp = addEmployee('employee.db')
        emp.add_employee(empId, name, rate, date, photo_bytes)  # ✅ send bytes, not path
        emp.close()
        
if __name__ == "__main__":
    attenDance()
