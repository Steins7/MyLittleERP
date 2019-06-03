import tkinter as tk
from DataTable import *
#from ToolBar import *
from UtilBar import *
from NavBar import *


class Page(tk.Canvas):

    def __init__(self,container,pageNumber,controller):
        # tk.Frame.__init__(self,container)
        super(Page,self).__init__(bg="blue",width=1200,height=1500)
        self.initFrames(pageNumber,controller)
        self.addtag_all("all")
        self.container=container
        #self.bind("<Configure>",self.resize)



    def initFrames(self,pageNumber,controller):
        utilBar = UtilBar(self,pageNumber,controller)
        navBar = NavBar(self,pageNumber,controller)
        dataTable = DataTable(self,pageNumber,controller)
        self.frames = [utilBar,navBar,dataTable]

    def hide(self):
        pass
        #for frame in self.frames :
        #    frame.hide()
        #self.grid_remove()

    def show(self):
        self.pack(anchor="nw",fill="both",expand="true",in_=self.container)
        for frame in self.frames :
            frame.show()


    def resize(self,event):
        print("hi")
        self.frames[2].resize(event)
        wscale = float(event.width)/self.winfo_width()
        hscale = float(event.height)/self.winfo_height()
        # resize the canvas 
        self.config(width=event.width, height=event.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

