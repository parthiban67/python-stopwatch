from tkinter import ttk
from tkinter import font
from tkinter import W
from tkinter import E

class Display():
    
    def __init__(self,parent,width,height,root):
        self.root = root
        style = ttk.Style()
        style.configure('frame1.TFrame', background="black")
        self.frame = ttk.Frame(parent,width=width,height=height,style='frame1.TFrame')
        self.parent = parent
        self.setupLabel()
        
    def setupLabel(self):
        labelFont = font.Font(family='Helvetica',weight='normal',size=28)
        frame = ttk.Frame(self.frame)
        self.hourLabel = ttk.Label(frame,text="00",foreground="red",background="black",font=labelFont,anchor='center', justify='center')
        self.hourLabel.grid(row=0,column=1,sticky=(E,W))
        
        separator1= ttk.Label(frame,text=":",foreground="red",background="black",font=labelFont,anchor='center', justify='center')
        separator1.grid(row=0,column=2,columnspan=2,sticky=(E,W))
        
        self.minuteLabel = ttk.Label(frame,text="00",foreground="red",background="black",font=labelFont, anchor='center', justify='center')
        self.minuteLabel.grid(row=0,column=4,sticky=(E,W))
        
        separator2= ttk.Label(frame,text=":",foreground="red",background="black",font=labelFont,anchor='center', justify='center')
        separator2.grid(row=0,column=5,columnspan=2,sticky=(E,W))
        
        self.secondLabel = ttk.Label(frame,text="00",foreground="red",background="black",font=labelFont,anchor='center', justify='center')
        self.secondLabel.grid(row=0,column=7,sticky=(E,W))
        
        frame.columnconfigure(1,weight=1)
        frame.columnconfigure(2,weight=1)
        frame.columnconfigure(4,weight=1)
        frame.columnconfigure(5,weight=1)
        frame.columnconfigure(7,weight=1)
        frame.pack(fill='x' ,pady=24,padx=32, expand=True)
    
    def setHourLabel(self,text):
        self.root.after(0,lambda t=text : self.hourLabel.config(text=t))
        
    def setMinuteLabel(self,text):
        self.root.after(0,lambda t=text : self.minuteLabel.config(text=t))
        
    def setSecondLabel(self,text):
        self.root.after(0,lambda t=text : self.secondLabel.config(text=t))
        
    def getFrame(self):
        return self.frame