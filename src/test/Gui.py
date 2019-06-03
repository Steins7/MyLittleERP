import tkinter as tk
from Page import *

class Gui(tk.Tk):
    def __init__(self,controller):
        tk.Tk.__init__(self)
        self.listPage = []
        for i in range(5000):
            self.listPage.append(Page(self,i,controller))
        self.listPage[0].grid( sticky="nsew")

    def changePage(self,i):
        i = 0 if i>= len(self.listPage) else i
        for p in self.listPage:
            p.grid_remove()
        self.listPage[i].grid( sticky="nsew")
