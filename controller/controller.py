from tkinter import ttk

class Controller():
    
    def __init__(self,parent,width,height):
        self.width = width
        self.frame = ttk.Frame(parent,width=self.width,height=height)
        self.setupButtons()
        
    def setupButtons(self):
        buttonFrame = ttk.Frame(self.frame,width=self.width)
        startBtn = ttk.Button(buttonFrame,text="Start")
        startBtn.grid(row=0,column=0,padx=5)
        
        stopBtn = ttk.Button(buttonFrame,text="Stop")
        stopBtn.grid(row=0,column=1,padx=5)
        
        restartBtn = ttk.Button(buttonFrame,text="Restart")
        restartBtn.grid(row=0,column=2,padx=5)
        
        buttonFrame.pack(fill='x',expand=True, pady=30, padx=10)
    
    def getFrame(self):
        return self.frame