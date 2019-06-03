import tkinter as tk
from Page import *

class Gui(tk.Tk):
    def __init__(self,controller):
        super(Gui,self).__init__()
        self.listPage = []
        self.bind("<Configure>",self.resize)
        #self.geometry("800x600")
        for i in range(5):
            self.listPage.append(Page(self,i,controller))
        self.changePage(0)


    def changePage(self,i):
        i = 0 if i>= len(self.listPage) else i
        for p in self.listPage:
            p.hide()
        self.listPage[i].show()

    def resize(self,event):
        print("here")
        self.listPage[0].resize(event)