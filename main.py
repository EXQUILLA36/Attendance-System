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

class main:
    def __init__(self):
        self.mainWindow = ctk.CTk()
        self.mainWindow.title("ABLAZA ATTENDANCE SYSTEM")
        self.mainWindow.geometry("1080x600")
        self.mainWindow.configure(corner_radius=15)

        self.employeeNames = {
            "AATS - 0001": "AL-ROSHD MANUEL ABLAZA",
            "AATS - 0002": "ASIAVELLE TIAMA ABLAZA",
            "AATS - 0003": "ACE ZANDE G. CACHO",
            "AATS - 0004": "BRYAN JAMES FAJARDO",
            "AATS - 0005": "TRIZTAN DALE S VERZOSA",
            "AATS - 0006": "CHRISTIAN JADE TALABO",
            "AATS - 0007": "MAYNARD ANTHONY DANTES VALDEZ",
            "AATS - 0008": "ALDAVE DE JESUS LOZADA",
            "AATS - 0009": "KENJI S CA-ANG",
            "AATS - 0010": "MARK KENNETH G. CACHO",
            "AATS - 0011": "BENEDICT FLORES SALES",
            "AATS - 0012": "JUNRAIN PANSOy",
            "AATS - 0013": "MARIC BELASANO",
            "AATS - 0014": "PAULO SAYSAY ORTEGA",
            "AATS - 0015": "JEFF ROGAS",
        }

        self.img = customtkinter.CTkImage(                                                  # --IMAGE LOADER--                          IMAGE
            light_image=Image.open("./Images/default.png"),
            size=(250,250),
        )

        self.AATS0005 = customtkinter.CTkImage(  # --IMAGE LOADER--                          IMAGE
            light_image=Image.open("./Images/AATS-0005.jpg"),
            size=(250, 250),
        )

        self.mainWindowFrame()

    def on_entry_change(self, *args):
        self.value = self.entry_var.get()
        print(self.value)
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

        self.entry_var = ctk.StringVar()
        self.entry_var.trace_add("write", self.on_entry_change)

        self.inCode = customtkinter.CTkEntry(                                               # --TIME IN ENTRY BOX--                     ENTRY
            self.inputFrame,
            width= 350, height=80,
            placeholder_text="TIME IN",
            textvariable=self.entry_var,
            font=("Arial", 24)
        )
        self.inCode.place(relx=0.06, rely=0.1)

        self.outCode = customtkinter.CTkEntry(                                              # --TIME OUT FRAME--                        ENTRY
            self.inputFrame,
            width=350, height=80,
            placeholder_text="TIME OUT",
            font=("Arial", 24)
        )
        self.outCode.place(relx=0.06, rely=0.3)

        self.personEntryInfo()

    def personEntryInfo(self):                                                              # --USER DISPLAY--                          FUNCTION
        self.imageContainer = customtkinter.CTkLabel(
            self.windowFrame,
            image=self.img,
            corner_radius=100,
            text=""
        )
        self.imageContainer.place(relx=0.15, rely=0.02)

        self.employeeName = customtkinter.CTkLabel(
            self.windowFrame,
            text_color="#ffffff",
            font=("Arial", 24),
            width=50,
            text="FIRST NAME MIDDLE NAME LASt NAME"
        )
        self.employeeName.configure(wraplength=400)
        self.employeeName.place(relx=0.04, rely=0.5)



    def employeeChecking(self):
        if self.value == "AATS - 0005":
            self.imageContainer.configure(image=self.AATS0005)


        if self.value in self.employeeNames.keys():
            self.employeeName.configure(text=self.employeeNames.get(self.value))
            self.name = self.employeeNames.get(self.value)
            self.attendance_log = {}

            if self.value not in self.attendance_log:
                self.attendance_log[self.value] = []

            logs = self.attendance_log[self.value]
            self.now = datetime.now()
            self.now_time = self.now.strftime("%I:%M")
            self.now_timestamp = self.now.strftime("%Y-%m-%d %H:%M:%S")

            if len(logs) % 2 == 0:
                logs.append({"type": "IN", "Time In": self.now_time, "timestamp": self.s
            else:
                logs.append({"type": "OUT", "Time Out": self.now_time, "timestamp": self.now_timestamp})
                print(f"{self.name} TIME OUT at {self.now_time}")
        # for key, value in self.employeeNames.items():
        #     print(key, value)
        if not os.path.exists("attendance"):
            os.mkdir("attendance")




    def display(self):
        self.scrollableDisplay = customtkinter.CTkScrollableFrame(
            self.displayFrame,
            height=1080, width=400,
            bg_color="#ffffff"
        )
        self.scrollableDisplay.grid(row=0, column=0)

    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    app = main()
    app.run()