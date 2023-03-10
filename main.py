# !/usr/bin/env python3
from os.path import basename, splitext
import tkinter as tk
import platform
# from matplotlib import pyplot as plt

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Goniometrické funkce"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("800x600")
        if platform.system() == "Windows":
            self.iconbitmap("images/icon.ico")

        self.headerFrame = tk.Frame(self).pack()
        self.headerLabel = tk.Label(self.headerFrame, text="Goniometrické funkce", font=("Arial", 24)).pack()
        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()