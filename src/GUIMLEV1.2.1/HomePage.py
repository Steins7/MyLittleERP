import Tkinter as tk
from Page import *


class HomePage(Page):
    file = None
    navBar  = NavBar(self)
    utilbar = UtilBar(self)
    toolBar = ToolBar(self)
    showFrame = ShowFrame(self)
    def __init__(self,container):
        tk.Frame.__init__(self,container)
    
    def show(self):
        utilBar.grid(row=0,column=0,columnspan=2,sticky="nsew")
        navBar.grid(row=1,column=0,sticky="nsew")