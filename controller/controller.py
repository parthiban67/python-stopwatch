from tkinter import ttk
from .clock import Clock

class Controller():
    
    def __init__(self,parent,width,height):
        self.width = width
        self.frame = ttk.Frame(parent,width=self.width,height=height)
        self.clock = Clock()
        self.setupButtons()
        
    def setupButtons(self):
        buttonFrame = ttk.Frame(self.frame,width=self.width)
        startBtn = ttk.Button(buttonFrame,text="Start",command=lambda : self.clock.start())
        startBtn.grid(row=0,column=0,padx=5)
        
        stopBtn = ttk.Button(buttonFrame,text="Stop",command=lambda : self.clock.stop())
        stopBtn.grid(row=0,column=1,padx=5)
        
        resetBtn = ttk.Button(buttonFrame,text="Reset")
        resetBtn.grid(row=0,column=2,padx=5)
        
        buttonFrame.pack(fill='x',expand=True, pady=30, padx=10)
    
    def getFrame(self):
        return self.frame