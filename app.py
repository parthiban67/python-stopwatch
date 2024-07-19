import tkinter as tk
from tkinter import ttk
from menu.menubar import MenuBar
from view.display import Display

if __name__ == '__main__':
    root = tk.Tk()
    frame = ttk.Frame(root)

    menubar = MenuBar(frame, lambda r=root: r.destroy())
    root['menu'] = menubar.getMenuBar()

    style = ttk.Style()
    style.configure('frame1.TFrame', background="black")
    displayFrame = ttk.Frame(frame, style='frame1.TFrame', width = 300)
    Display(displayFrame)
    displayFrame.grid(column=0,row=0,sticky=(tk.N,tk.S,tk.E,tk.W))
    controlFrame = ttk.Frame(frame, width = 300)
    controlFrame.grid(column=0,row=1,sticky=(tk.N,tk.S,tk.E,tk.W))

    frame.rowconfigure(0,weight=1)
    frame.rowconfigure(1,weight=1)
    frame.columnconfigure(0,weight=1)
    frame.pack(fill=tk.BOTH, expand=True)
    root.title("Stopwatch")
    root.mainloop()
