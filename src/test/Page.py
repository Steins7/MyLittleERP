import tkinter as tk

class Page(tk.Frame):

    def __init__(self,container,number,controller):
        tk.Frame.__init__(self,container)
        self.btn1=tk.Button(self,text="click "+str(number),fg="black",bg="white",command=lambda:controller.changePage(number+1))
        self.btn1.grid(sticky="nsew")
    
