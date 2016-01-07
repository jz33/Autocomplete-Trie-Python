from Utilities import LoadFile
from View import View
from Model import Model
from Tkinter import Tk
'''
Author: junzhengrice@gmail.com
'''
# FILE_NAME = 'words_109582.txt'
FILE_NAME = 'words_598153.txt'

class Controller(object):
    def __init__(self, filename):
        self.filename = filename
        self.model = Model()
        self.window = Tk()
        self.view = View(self.window,self)
       
    def Run(self): 
        self.window.mainloop()
        
    def Construct(self):
        self.model.Construct(self.filename)
    
    def Contains(self,tag):
        return self.model.Contains(tag)
    
    def List(self,tag):
        return self.model.List(tag)
    
    def SwitchCommand(self):
        self.model.SwitchCommand()
    
    def LoadFile(self):
        return list(LoadFile(self.filename));
        
        
#main
app = Controller(FILE_NAME)
app.Run()       
