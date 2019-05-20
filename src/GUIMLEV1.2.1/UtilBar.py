import tkinter as tk

strFile = "file"
strEdit = "edit"
strSelect = "select"
strHelp = "help"
strQuit = "quit"

class UtilBar(tk.Frame):

    def __init__(self,container,pageNumber,controller):
        # tk.Frame.__init__(self,container)
        super().__init__(container)
        self.initButton()
        self.show()
    
    def initButton(self):
        btnFile = tk.Button(self,text=strFile,fg="black",bg="white",name=strFile,command=lambda:menu(strFile))
        btnEdit = tk.Button(self,text=strEdit,fg="black",bg="white",name=strEdit,command=lambda:menu(strEdit))
        btnSelect = tk.Button(self,text=strSelect,fg="black",bg="white",name=strSelect,command=lambda:menu(strSelect))
        btnHelp = tk.Button(self,text=strHelp,fg="black",bg="white",name=strHelp,command=lambda:menu(strHelp))
        btnQuit = tk.Button(self,text=strQuit,fg="black",bg="white",name=strQuit,command=lambda:MLE.quit())
        self.buttonList = [btnFile,btnEdit,btnSelect,btnHelp,btnQuit]

    def show(self):
        self.grid(row=0,column=0,columnspan=3,sticky="snew")
        for i in range(len(self.buttonList)) :
            self.buttonList[i].grid(column=i,row=0,sticky="nsew")
    
    def hide(self):
        for btn in self.buttonList :
            btn.grid_remove()
        self.grid_remove()