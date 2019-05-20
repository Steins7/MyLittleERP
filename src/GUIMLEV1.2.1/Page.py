import tkinter as tk
from DataTable import *
#from ToolBar import *
from UtilBar import *
from NavBar import *


class Page(tk.Frame):

    def __init__(self,container,pageNumber,controller):
        # tk.Frame.__init__(self,container)
        super(Page,self).__init__()
        self.initFrames(pageNumber,controller)
    
    def initFrames(self,pageNumber,controller):
        utilBar = UtilBar(self,pageNumber,controller)
        navBar = NavBar(self,pageNumber,controller)
        dataTable = DataTable(self,pageNumber,controller)
        self.frames = [utilBar,navBar,dataTable]

    def hide(self):
        for frame in self.frames :
            frame.hide()
        self.grid_remove()
    
    def show(self):
        self.grid(row=0, column=0,sticky="nsew")
        for frame in self.frames :
            frame.show()
        

    
        
