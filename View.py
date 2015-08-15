import Utilities
from Tkinter import Tk, StringVar
from ttk import Frame,Button,Combobox
'''
Author: junzhengrice@gmail.com
'''
class View(Frame):    
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.title("Autocomplete")
        
        self.pack(fill = 'both', expand = 1)
        
        self.initializeComponents()
        Utilities.CenterWindow(self.parent)
        
        self.controller = controller
    
    def initializeComponents(self):
        self.boxValue = StringVar()
        self.boxValue.trace('w', \
            lambda name, index, mode, \
            boxValue = self.boxValue : \
            self.box_valueEditted(boxValue))
            
        self.box = Combobox(self,\
            justify = 'left',\
            width = 50, \
            textvariable = self.boxValue,\
        )
        self.box.pack(side = 'left',expand = 1, padx = 5, pady = 5)
        self.box.bind('<<ComboboxSelected>>',self.box_selected)
        self.box.bind('<Return>',self.box_returned)
        
        self.importButton = Button(self, \
            text = "Import", \
            command = self.importDict,\
        )
        self.importButton.pack(side = 'left',expand = 1)
        
        self.quitButton = Button(self, \
            text = "Close", \
            command = self.quit, \
        )
        self.quitButton.pack(side = 'right', padx = 5, pady = 5)
       
    #******************Callbacks******************
    '''
    Edit current text in combo box will trigger autocomplete
    '''
    def box_valueEditted(self,sv):
        tag = sv.get()
        container = self.controller.List(tag)
        self.box['value'] = [] # clear
        self.box['value'] = container
        '''
        Turn on dropdown list will cause refreshing lag 
        when test case is too large. Mouse click down arrow or 
        press "down" in key board to explore list
        '''
        #self.box.event_generate('<Down>')
    
    '''
    Select 1 value in dropdown list will find this value in Trie.
    This callback is for testing
    '''
    def box_selected(self,event):
        tag = event.widget.get()
        print self.controller.Contains(tag) # expect True
     
    '''
    Press 'return' will show combo box's dropdown list
    '''
    def box_returned(self,event):
        self.box.event_generate('<Down>')
     
    '''       
    Press 'import' button will import test file and initialize trie
    '''        
    def importDict(self):
        self.box['value'] = self.controller.LoadFile()   
        self.controller.Construct()
        
