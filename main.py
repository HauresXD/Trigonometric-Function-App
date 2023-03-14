# !/usr/bin/env python3
from os.path import basename, splitext
import tkinter as tk
import tkinter.ttk as ttk
import platform
# from matplotlib import pyplot as plt

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Goniometrické funkce"

    def __init__(self):
        super().__init__(className=self.name)
        # Basic "all-n-all" setup
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("1300x800")
        self.resizable(width=tk.FALSE, height=tk.FALSE)
        if platform.system() == "Windows":
            self.iconbitmap("images/icon.ico")

        # Label Frame setup + Label + Separator
        self.headerFrame = tk.LabelFrame(self, borderwidth = 0, highlightthickness = 0)
        self.headerFrame.pack(side=tk.TOP)
        self.headerLabel = tk.Label(self.headerFrame, text="Goniometrické funkce", font=("Arial", 24))
        self.headerLabel.pack()
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, padx=2)

        # Content Frame setup + Options Frame setup + Graph Frame setup
        self.contentFrame = tk.Frame(self, width=1300, height=800)
        self.contentFrame.pack(side=tk.TOP, pady=5)
        self.optionsFrame = tk.LabelFrame(self.contentFrame, text="Výběr", width=700, height=800)
        self.optionsFrame.pack(side=tk.LEFT, padx=5, pady=5)
        self.optionsFrame.pack_propagate(False)
        self.graphFrame = tk.LabelFrame(self.contentFrame, text="Graf", width=600, height=800)
        self.graphFrame.pack(side=tk.RIGHT, padx=5, pady=5)
        self.graphFrame.pack_propagate(False)

        # Options Frame - display options
        self.displayFrame = tk.Frame(self.optionsFrame)
        self.displayFrame.pack(fill=tk.X)
        self.displayOptVar = tk.StringVar(value="program")
        self.displayOpt1 = tk.Radiobutton(self.displayFrame, text="V Programu", font=(None, 12), variable=self.displayOptVar, value="program")
        self.displayOpt1.pack(side=tk.LEFT, padx=20)
        self.displayOpt2 = tk.Radiobutton(self.displayFrame, text="Samostatně", font=(None, 12), variable=self.displayOptVar, value="standalone")
        self.displayOpt2.pack(side=tk.LEFT, padx=20)
        self.displaySelectBtn = tk.Button(self.displayFrame, text="Vybrat Soubor")
        self.displaySelectBtn.pack(side=tk.RIGHT, padx=20)

        # Options Frame - graph selections
        

        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()