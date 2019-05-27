import tkinter as tk

class DataTable(tk.Canvas):


    def __init__(self,container,pageNumber,controller):
        super().__init__(container,bg="red")
        self.yScrollBar=tk.Scrollbar(container,orient='vertical',command=self.yview)
        self.yScrollBar.grid(row=1,rowspan=2,column=2,sticky="ns")
        self.xScrollBar=tk.Scrollbar(container,orient='horizontal',command=self.xview)
        self.xScrollBar.grid(row=3,rowspan=1,column=1,sticky="ew")

        self.config(yscrollcommand=self.yScrollBar.set,xscrollcommand=self.xScrollBar.set)
        self.interior = tk.Frame(self)
        self.create_window(0, 0, window=self.interior, anchor="nw")
        self.grid(row=1,rowspan=2,column=1,sticky="nsew")
        self.bind('<Configure>',self.resizeCanvas)
        self.table(100,10)
        self.addtag_all("all")
        self.height = self.winfo_height()
        self.width = self.winfo_width()



    #----callbacks

    def resizeCanvas(self,event):
        size = [self.interior.winfo_reqwidth(), self.interior.winfo_reqheight()]
        self.config(scrollregion="0 0 "+str(size[0])+" "+str(size[1]))


    def resizeFrame(self,event):
        wscale = float(event.width)/self.interior.winfo_width()
        hscale = float(event.height)/self.interior.winfo_height()
        width = event.width
        height = event.height
        if(height >= 500):
            height = 500
        # resize the canvas 
        self.interior.config(width=width, height=height)
        # rescale all the objects tagged with the "all" tag
        self.interior.scale("all",0,0,wscale,hscale)


    def table(self,nbRow,nbCol):
        self.table = list()
        for i in range(0,nbRow):
            for j in range(0,nbCol):
                cell=tk.Entry(self.interior, width=10)
                print(i,"\n")
                cell.insert(0, nbRow*j+i) 
                cell.grid(row = i, column = j) 
                self.table.append(cell)




