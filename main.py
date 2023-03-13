#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="tkGraf")
        self.lbl.pack()

        self.fileFrame = tk.LabelFrame(self, text="soubor")
        self.fileFrame.pack(padx=5, pady=5)
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack()
        self.fileBtn = tk.Button(self.fileFrame, text="...")
        self.fileBtn.pack(anchor="e")

        self.dataformatVar = tk.IntVar()
        self.radkyRbtn = tk.Radiobutton(self.fileFrame, text = "data jsou v radcich", variable=self.dataformatVar, value=0)
        self.radkyRbtn.pack(anchor="w")
        self.sloupceRbtn = tk.Radiobutton(self.fileFrame, text="data jsou ve sloupcich", variable=self.dataformatVar, value=1)
        self.sloupceRbtn.pack(anchor="w")

        self.grafFrame = tk.LabelFrame(self, text="Graf")
        self.grafFrame.pack()
        tk.Label(self.grafFrame, text="Titulek").grid(row=0, column=0)
        self.titleEntry = tk.Entry(self.grafFrame)
        self.titleEntry.grid(row=0, column=1)

        tk.Label(self.grafFrame, text="Popisek x").grid(row=1, column=0)
        self.xlabelEntry = tk.Entry(self.grafFrame)
        self.xlabelEntry.grid(row=1, column=1)

        tk.Label(self.grafFrame, text="Popisek y").grid(row=2, column=0)
        self.ylabelEntry = tk.Entry(self.grafFrame)
        self.ylabelEntry.grid(row=2, column=1)

        tk.Label(self.grafFrame, text="Mrizka").grid(row=3, column=0)
        self.gridChck = tk.Checkbutton(self.grafFrame)
        self.gridChck.grid(row=3, column=1, sticky="w")



        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()