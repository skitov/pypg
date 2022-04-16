#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk


class UI():
    def __init__(self, root):
        self.cvs = Canvas(root, bg="Green", width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.cvs.create_oval(100, 100, 200, 200, fill="blue")
        self.cvs.pack()

def main():
    root = Tk()
    root.geometry("800x600+300+200")
    ui = UI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
