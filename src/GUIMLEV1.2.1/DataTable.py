import tkinter as tk

class DataTable(tk.Canvas):


    def __init__(self,container,pageNumber,controller):
        super().__init__(container,bg="red")
        self.yScrollBar=tk.Scrollbar(container,orient='vertical',command=self.yview)
        self.yScrollBar.grid(row=1,rowspan=2,column=2,sticky="ns")
        self.xScrollBar=tk.Scrollbar(container,orient='horizontal',command=self.xview)
        self.xScrollBar.grid(row=3,rowspan=1,column=1,sticky="ew")

        self.config(yscrollcommand=self.yScrollBar.set,xscrollcommand=self.xScrollBar.set)
        self.interior =  tk.Frame(self)
        self.create_window(0, 0, window=self.interior, anchor="nw")
        self.grid(row=1,rowspan=2,column=1,sticky="nsew")
        self.interior.bind('<Configure>',self.resizeCanvas)
        #self.bind('<Configure>',self.resizeFrame)
        self.table(100,10)

    #callbacks

    def resizeCanvas(self,event):
        #size = [self.interior.winfo_reqwidth(), self.interior.winfo_reqheight()]
        #self.config(scrollregion="0 0 "+str(size[0])+" "+str(size[1]))
        wscale = float(event.width)/self.winfo_reqwidth()
        hscale = float(event.height)/self.winfo_reqheight()
        width = event.width
        height = event.height
        if(height >= 500):
            height = 500
        # resize the canvas 
        self.config(width=width, height=height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

    def resizeFrame(self,event):
        width = self.winfo_width()
        height = self.winfo_height()
        if(height >= 500):
            height = 500
        self.interior.config(width=self.winfo_width(),height=self.winfo_height())


    def table(self,nbRow,nbCol):
        self.table = list()
        for i in range(0,nbRow):
            for j in range(0,nbCol):
                cell=tk.Entry(self.interior, width=10)
                print(i,"\n")
                cell.insert(0, nbRow*j+i) 
                cell.grid(row = i, column = j) 
                self.table.append(cell)




