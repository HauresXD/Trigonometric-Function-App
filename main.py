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
        self.geometry("1300x800")
        self.resizable(width=tk.FALSE, height=tk.FALSE)
        if platform.system() == "Windows":
            self.iconbitmap("images/icon.ico")

        self.headerFrame = tk.LabelFrame(self, borderwidth = 0, highlightthickness = 0)
        self.headerFrame.pack(side=tk.TOP)
        self.headerLabel = tk.Label(self.headerFrame, text="Goniometrické funkce", font=("Arial", 24))
        self.headerLabel.pack()

        self.contentFrame = tk.Frame(self, bg="blue", width=1300, height=800)
        self.contentFrame.pack(side=tk.TOP)
        self.entryFrame = tk.Frame(self.contentFrame, bg="#c3c3c3", width=700, height=800)
        self.entryFrame.pack(side=tk.LEFT)
        self.graphFrame = tk.Frame(self.contentFrame, bg="#aeaeae", width=600, height=800)
        self.graphFrame.pack(side=tk.RIGHT)
        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()