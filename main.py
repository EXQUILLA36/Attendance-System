from tkinter import PhotoImage

import customtkinter
from customtkinter import *
import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from pathlib import Path
from PIL import Image, ImageTk

class main:
    def __init__(self):
        self.mainWindow = ctk.CTk()
        self.mainWindow.title("ABLAZA ATTENDANCE SYSTEM")
        self.mainWindow.geometry("1080x720")
        self.mainWindow.configure(corner_radius=15)

        self.img = customtkinter.CTkImage(                                                  # --IMAGE LOADER--                          IMAGE
            light_image=Image.open("./Images/default.png"),
            size=(250,250),
        )

        self.mainWindowFrame()

    def mainWindowFrame(self):
        self.windowFrame = ctk.CTkFrame(                                                    # --MAIN PROGRAM FRAME--                    FRAME
            self.mainWindow,
            height=720, width=400,
            fg_color="#757575"
        )
        self.windowFrame.place(relx=0.37, rely=0.5, anchor="e")                             # --FRAMES FOR ENTRY BOXES--                FRAME

        self.inputFrame = ctk.CTkFrame(
            self.windowFrame,
            height=400, width=400,
            fg_color="#7A73D1",
            corner_radius=0
        )
        self.inputFrame.place(relx=0, rely=0.45, x=0, y=0)

        self.displayFrame = ctk.CTkFrame(                                                   # --MAIN DISPLAY OF ATTENDANCE FRAME--      FRAME
            self.mainWindow,
            height=720, width=680,
            fg_color="#211C84",
            corner_radius=0
        )
        self.displayFrame.place(relx=0.685, rely=0.5, x=0, y=0, anchor="center")

        self.inCode = customtkinter.CTkEntry(                                               # --TIME IN ENTRY BOX--                     ENTRY
            self.inputFrame,
            width= 350, height=80,
            placeholder_text="TIME IN",
            font=("Arial", 24)
        )
        self.inCode.place(relx=0.06, rely=0.2)

        self.outCode = customtkinter.CTkEntry(                                              # --TIME OUT FRAME--                        ENTRY
            self.inputFrame,
            width=350, height=80,
            placeholder_text="TIME OUT",
            font=("Arial", 24)
        )
        self.outCode.place(relx=0.06, rely=0.5)

        self.personEntryInfo()

    def personEntryInfo(self):                                                              # --USER DISPLAY--                          FUNCTION
        self.imageContainer = customtkinter.CTkLabel(
            self.windowFrame,
            image=self.img,
            corner_radius=100,
            text=""
        )
        self.imageContainer.place(relx=0.18, rely=0.05)

    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    app = main()
    app.run()