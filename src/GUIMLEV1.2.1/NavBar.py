import tkinter as tk

class NavBar(tk.Frame):
    file = None
    def __init__(self,container,pageNumber,controller):
        super(NavBar,self).__init__()
        # self.initButton()
        self.grid(row=1,column=0,sticky="nsew")

