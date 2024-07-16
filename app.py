import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()
    frame = ttk.Frame(root, width = 300, height = 300)

    menubar = tk.Menu(root)
    exitMenu = tk.Menu(menubar)
    menubar.add_cascade(menu=exitMenu, label="Exit")

    root['menu'] = menubar
    frame.grid()
    root.title("Stopwatch")
    root.mainloop()
