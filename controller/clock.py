from threading import Thread,local,Condition,Lock,Event
from time import sleep  

class Clock():
    
    def __init__(self):
        self.initiated = False
        self.condition = Condition(Lock())
        self.pauseDict = dict(pause=False)
        self.resetEvent = Event()
    
    def start(self):
        if not self.initiated:
            self.resetEvent.clear()
            self.initiated = True
            self.worker = Worker(self.condition,self.pauseDict,self.resetEvent)
            self.worker.start()
        else:
            waker = Waker(self.condition,self.pauseDict)
            waker.start()
    
    def stop(self):
        self.worker.doPause()
    
    def reset(self):
        self.initiated = False
        self.resetEvent.set()
        sleep(0.010)

class TimeData(local):
    
    def __init__(self,hr,min,sec):
        local.__init__(self)
        self.hr = hr
        self.min = min
        self.sec = sec
    
    def getHr(self):
        return self.hr
    
    def setHr(self,hr):
        self.hr = hr
        
    def setMin(self, min):
        self.min = min
        
    def getMin(self):
        return self.min
    
    def setSec(self, sec):
        self.sec = sec
    
    def getSec(self):
        return self.sec
    
class Worker(Thread):
    
    def __init__(self,condition,pauseDict,resetEvent):
        Thread.__init__(self)
        self.condition = condition
        self.daemon = True
        self.data = TimeData(0,0,0)
        self.pauseDict = pauseDict
        self.resetEvent = resetEvent
    
    def doPause(self):
        self.pauseDict['pause'] = True
        
    def run(self):
        while True:
            if self.resetEvent.is_set():
                break
            with self.condition:
                while self.pauseDict['pause']:
                    self.condition.wait()
                sleep(1)
                secReset = False
                if self.data.getSec() < 59:
                    self.data.setSec(self.data.getSec() + 1)
                else :
                    self.data.setSec(0)
                    secReset = True
                minReset = False    
                if secReset:
                    if self.data.getMin() < 59:
                        self.data.setMin(self.data.getMin() + 1)
                    else :
                        self.data.setMin(0)
                        minReset = True
                if minReset:
                    self.data.setHr(self.data.getHr() + 1)
                    
                print(str(self.data.getHr())+":"+str(self.data.getMin())+":"+str(self.data.getSec()))

class Waker(Thread):
    
    def __init__(self,condition,pauseDict):
        Thread.__init__(self)
        self.daemon = True
        self.condition = condition
        self.pauseDict = pauseDict
        
    def run(self):
        with self.condition:
            if self.pauseDict['pause']:
                self.pauseDict['pause'] = False
                self.condition.notify()