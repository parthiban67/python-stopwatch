import tkinter as tk
from tkinter import ttk
from menu.menubar import MenuBar

if __name__ == '__main__':
    root = tk.Tk()
    frame = ttk.Frame(root, width = 300, height = 300)

    menubar = MenuBar(frame, lambda r=root: r.destroy())
    root['menu'] = menubar.getMenuBar()

    frame.grid()
    root.title("Stopwatch")
    root.mainloop()
