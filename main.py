from tkinter import PhotoImage
import customtkinter
from customtkinter import *
import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from pathlib import Path
from PIL import Image, ImageTk
import os
from datetime import datetime, timedelta
import json
import pandas as pd
import tkinter.messagebox as messagebox

class main:
    def __init__(self):
        self.mainWindow = ctk.CTk()
        self.mainWindow.title("ABLAZA ATTENDANCE SYSTEM")
        self.mainWindow.geometry("1080x600")
        self.mainWindow.configure(corner_radius=15)
        self.mainWindow.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.attendance_log = {}
        self.attendance_status = {}

        self.default = customtkinter.CTkImage(  # --IMAGE LOADER--                          IMAGE
            light_image=Image.open("./Images/default.png"),
            size=(180, 180),
        )

        # CODE-AND-NAMES
        employees = [
            {"id": "AATS - 0001", "name": "AL-ROSHD MANUEL ABLAZA", "image": "./Images/AATS-0001.jpg"},
            {"id": "AATS - 0002", "name": "ASIAVELLE TIAMA ABLAZA", "image": None},
            {"id": "AATS - 0003", "name": "ACE ZANDE G. CACHO", "image": None},
            {"id": "AATS - 0004", "name": "BRYAN JAMES FAJARDO", "image": "./Images/AATS-0004.jpg"},
            {"id": "AATS - 0005", "name": "TRIZTAN DALE S VERZOSA", "image": "./Images/AATS-0005.jpg"},
            {"id": "AATS - 0006", "name": "CHRISTIAN JADE TALABO", "image": "./Images/AATS-0006.jpg"},
            {"id": "AATS - 0007", "name": "MAYNARD ANTHONY DANTES VALDEZ", "image": "./Images/AATS-0007.jpg"},
            {"id": "AATS - 0008", "name": "ALDAVE DE JESUS LOZADA", "image": "./Images/AATS-0008.jpg"},
            {"id": "AATS - 0009", "name": "KENJI S CA-ANG", "image": None},
            {"id": "AATS - 0010", "name": "MARK KENNETH G. CACHO", "image": None},
            {"id": "AATS - 0011", "name": "BENEDICT FLORES SALES", "image": "./Images/AATS-0011.jpg"},
            {"id": "AATS - 0012", "name": "JUNRAIN PANSOy", "image": "./Images/AATS-0012.jpg"},
            {"id": "AATS - 0013", "name": "MARIC BELASANO", "image": None},
            {"id": "AATS - 0014", "name": "PAULO SAYSAY ORTEGA", "image": "./Images/AATS-0014.jpg"},
            {"id": "AATS - 0015", "name": "JEFF ROGAS", "image": "./Images/AATS-0015.jpg"}
        ]

        with open("employees.json", "r") as f:
            self.data = json.load(f)

        self.employeeNames = {}
        self.employeeImages = {}

        for emp in self.data["employees"]:
            emp_id = emp["id"]
            self.employeeNames[emp_id] = emp["name"]

            try:
                if emp["image"]:
                    img = customtkinter.CTkImage(light_image=Image.open(emp["image"]), size=(180, 180))
                else:
                    raise FileNotFoundError
            except:
                img = customtkinter.CTkImage(light_image=Image.open("./Images/default.png"), size=(180, 180))

            self.employeeImages[emp_id] = img

        self.mainWindowFrame()


    def on_entry_change(self, *args):
        self.timeIn = self.in_var.get()
        self.employeeChecking()

    def mainWindowFrame(self):
        self.windowFrame = ctk.CTkFrame(                                                    # --MAIN PROGRAM FRAME--                    FRAME
            self.mainWindow,
            height=600, width=400,
            fg_color="#757575"
        )
        self.windowFrame.place(relx=0.37, rely=0.5, anchor="e")                             # --FRAMES FOR ENTRY BOXES--                FRAME

        self.inputFrame = ctk.CTkFrame(
            self.windowFrame,
            height=450, width=400,
            fg_color="#7A73D1",
            corner_radius=0
        )
        self.inputFrame.place(relx=0, rely=0.6, x=0, y=0)

        self.displayFrame = ctk.CTkFrame(                                                   # --MAIN DISPLAY OF ATTENDANCE FRAME--      FRAME
            self.mainWindow,
            height=720, width=680,
            fg_color="#211C84",
            corner_radius=0
        )
        self.displayFrame.place(relx=0.685, rely=0.5, x=0, y=0, anchor="center")

        self.in_var = ctk.StringVar()
        self.in_var.trace_add("write", self.on_entry_change)

        self.inCode = customtkinter.CTkEntry(                                               # --TIME IN ENTRY BOX--                     ENTRY
            self.inputFrame,
            width= 350, height=80,
            placeholder_text="TIME IN",
            textvariable=self.in_var,
            font=("Arial", 24)
        )
        self.inCode.place(relx=0.06, rely=0.1)

        self.out_var = ctk.StringVar()
        self.out_var.trace_add("write", self.on_entry_change)


        self.personEntryInfo()

    def personEntryInfo(self):                                                              # --USER DISPLAY--                          FUNCTION
        self.imageContainer = customtkinter.CTkLabel(
            self.windowFrame,
            image=self.default,
            corner_radius=100,
            text=""
        )
        self.imageContainer.place(relx=0.3, rely=0.18, anchor="center")

        self.employeeName = customtkinter.CTkLabel(
            self.windowFrame,
            text_color="#ffffff",
            font=("Arial", 24),
            justify="left",
            text="FIRST NAME MIDDLE NAME LAST NAME"
        )
        self.employeeName.configure(wraplength=350)
        self.employeeName.place(relx=0.06, rely=0.35)

        self.display()


    def employeeChecking(self):
        try:
            if self.timeIn in self.employeeNames:
                self.employeeName.configure(text=self.employeeNames.get(self.timeIn))
                self.imageContainer.configure(image=self.employeeImages.get(self.timeIn))
                self.inCode.delete(0, 'end')

                self.now = datetime.now()
                self.time = self.now.strftime("%I:%M %p")
                self.date = self.now.strftime("%d-%m-%Y")

                for emp in self.data["employees"]:
                    if emp["id"] == self.timeIn:
                        for log in emp["log"]:
                            if log["status"] == "absent":
                                log["date"] = self.date
                                log["status"] = "present"
                                log["timeIn"] = self.time
                                print(f"{emp["id"]} name:{emp["name"]} Status: {log["status"]} - Timed In: {log["timeIn"]}")
                            else:
                                log["status"] = "absent"
                                log["timeOut"] = self.time
                            print(f"{emp["id"]} name:{emp["name"]} Status: {log["status"]} - Timed Out: {log["timeIn"]}")

                with open("employees.json", "w") as f:
                    json.dump(self.data, f, indent=4)

        except Exception as e:
            print("SYSTEM ERROR:", e)


    def display(self):
        self.scrollableDisplay = customtkinter.CTkScrollableFrame(
            self.displayFrame,
            height=560, width=700,
        )
        self.scrollableDisplay.place(relx=0, rely=0.1, anchor="nw")

        for emp in self.data["employees"]:
            self.personFrame = ctk.CTkFrame(
                self.scrollableDisplay,
                height=200, width=670,
                fg_color="#ffffff"
            )
            self.personFrame.pack(pady=5, anchor="w")

            self.imgLbl = customtkinter.CTkLabel(
                self.personFrame,
                image=self.employeeImages.get(emp["id"]),
                text=""
            )
            self.imgLbl.place(relx=0.2, rely=0.5, anchor="center")

            self.nameLbl = customtkinter.CTkLabel(
                self.personFrame,
                text_color="#000000",
                text=self.employeeNames.get(emp["id"])
            )
            self.nameLbl.place(relx=0.5, rely=0.5, anchor="center")

    def export_json_to_excel(self, json_path="employees.json", excel_path="attendance.xlsx"):
        with open(json_path, "r") as f:
            data = json.load(f)

            flat_rows = []

            for emp in data["employees"]:
                for log in emp.get("log", []):
                    flat_rows.append({
                        "Employee ID": emp["id"],
                        "Name": emp["name"],
                        "Date": log.get("date", ""),
                        "Status": log.get("status", ""),
                        "Time In": log.get("timeIn", ""),
                        "Time Out": log.get("timeOut", "")
                    })

                    df = pd.DataFrame(flat_rows)

        try:
            df.to_excel(excel_path, index=False)
            return True
        except PermissionError:
            messagebox.showerror("Save Error",
                                 f"Cannot save the file because {excel_path} is open.\nPlease close it and try again.")
            print(f"CANNOT CLOSE APPLICATION AS THE {excel_path} EXCEL SHEET IS OPENED. PLEASE CLOSE THE EXCEL FIRST")
            return False

    def run(self):
        self.mainWindow.mainloop()

    def on_exit(self):
        success = self.export_json_to_excel("employees.json", "attendance_export.xlsx")
        if success:
            self.mainWindow.destroy()
        else:
            pass

if __name__ == "__main__":
    app = main()
    app.run()