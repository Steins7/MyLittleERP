import tkinter as tk
from Page import *

class Gui(tk.Tk):
    def __init__(self,controller):
        super(Gui,self).__init__()
        self.listPage = []
        self.geometry("800x600")
        for i in range(5):
            self.listPage.append(Page(self,i,controller))
        self.listPage[0].grid(row=0,column=0, sticky="nsew")
        

    def changePage(self,i):
        i = 0 if i>= len(self.listPage) else i
        for p in self.listPage:
            p.hide()
        self.listPage[i].show()
