from tkinter import Menu
from tkinter import messagebox

class MenuBar():

    def __init__(self, parent, exitHandler):
        self.parent = parent
        self.exitHandler = exitHandler
        self.setupMenuBar()

    def setupMenuBar(self):
        self.menubar = Menu(self.parent)
        self.setupSelection()
        self.setupHelpMenu()

    def setupSelection(self):
        selectionMenu = Menu(self.menubar)
        selectionMenu.add_command(label = "Standard")
        selectionMenu.add_separator()
        selectionMenu.add_command(label = "Exit", command = self.exitHandler)
        self.menubar.add_cascade(label = "Selection", menu = selectionMenu)

    def setupHelpMenu(self):
        helpMenu = Menu(self.menubar)
        helpMenu.add_command(label="About", command = lambda : self.showAboutMessage())
        self.menubar.add_cascade(menu = helpMenu, label = "Help")

    def showAboutMessage(self):
        messagebox.showinfo("About","Stopwatch written in python using tkinter", parent = self.parent)

    def getMenuBar(self):
        return self.menubar

