import tkinter as tk
from tkinter import ttk
from menu.menubar import MenuBar
from view.display import Display
from controller.controller import Controller

if __name__ == '__main__':
    root = tk.Tk()
    frame = ttk.Frame(root)

    menubar = MenuBar(frame, lambda r=root: r.destroy())
    root['menu'] = menubar.getMenuBar()

    display = Display(frame,300,200,root)
    display.getFrame().grid(column=0,row=0,sticky=(tk.N,tk.S,tk.E,tk.W))
    
    controller = Controller(frame,300,200,display)
    controller.getFrame().grid(column=0,row=1,sticky=(tk.N,tk.S,tk.E,tk.W))
    
    frame.rowconfigure(0,weight=1)
    frame.rowconfigure(1,weight=1)
    frame.columnconfigure(0,weight=1)
    frame.pack(fill=tk.BOTH, expand=True)
    
    root.title("Stopwatch")
    root.resizable(False,False)
    root.mainloop()
