import tkinter as tk

class NavBar(tk.Frame):
    file = None
    def __init__(self,container,pageNumber,controller):
        super(NavBar,self).__init__()
        # self.initButton()
        #self.grid(row=1,column=0,sticky="nsew")

    def show(self):
        pass
        #self.pack(anchor="nw",expand="true")
        #self.grid(row=0,column=0,columnspan=3,sticky="snew")
        #for i in range(len(self.buttonList)) :
        #    self.buttonList[i].pack(anchor="nw")
        #    self.buttonList[i].grid(column=i,row=0,sticky="nsew")

    def hide(self):
        pass
        #for btn in self.buttonList :
        #    btn.grid_remove()
        #self.grid_remove()