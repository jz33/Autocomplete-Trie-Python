from Utilities import CenterWindow
from Tkinter import Tk, StringVar
from ttk import Frame,Button,Combobox
'''
Author: junzhengrice@gmail.com
'''
class View(Frame):    
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.title("Autocompleter")
        
        self.pack(fill = 'both', expand = 1)
        
        self.initializeComponents()
        CenterWindow(self.parent)
        
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
            command = self.importButton_clicked,\
        )
        self.importButton.pack(side = 'left',expand = 1)
        
        self.cmd_str = StringVar(None,"Prefix Only")
        self.switchButton = Button(self, \
            textvariable = self.cmd_str, \
            command = self.switchButton_clicked, \
        )
        self.switchButton.pack(side = 'right', padx = 5, pady = 5)
       
    #******************Callbacks******************
    def box_valueEditted(self,sv):
        '''
        Edit text of combo box will trigger autocomplete
        This implementation is moved to "box_returned"
        '''
        pass

    def box_selected(self,event):
        '''
        Selecting 1 value of dropdown list finds all strings 
        with this prefix. Testing only.
        '''
        # tag = event.widget.get()
        # print self.controller.Contains(tag)
        pass

    def box_returned(self,event):
        '''
        Press 'return' will show combo box's dropdown list
        '''
        tag = self.boxValue.get()
        container = self.controller.List(tag)
        self.box['value'] = [] # clear
        self.box['value'] = container
        self.box.event_generate('<Down>')
            
    def importButton_clicked(self):
        '''       
        Press 'import' button will import test file and initialize Trie
        '''
        self.box['value'] = self.controller.LoadFile()   
        self.controller.Construct()
        
    def switchButton_clicked(self):
        '''
        Press will switch between 
        'Prefix Only' and 'Prefix and Infix' mode
        '''
        self.controller.SwitchCommand()
        cmd_str = self.cmd_str.get()
        if cmd_str == 'Prefix Only':
            self.cmd_str.set('Prefix and Infix')
        else:
            self.cmd_str.set('Prefix Only')
        
