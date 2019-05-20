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
        self.create_window(0, 0, window=self.interior)
        self.grid(row=1,rowspan=2,column=1,sticky="nsew")
        self.interior.bind('<Configure>',self.resizeCanvas)
        self.bind('<Configure>',self.resizeFrame)
        self.table(50,50)


    def resizeCanvas(self,event):
        size = [self.interior.winfo_reqwidth(), self.interior.winfo_reqheight()]
        self.config(scrollregion="0 0 "+str(size[0])+" "+str(size[1]))
    
    def resizeFrame(self,event):
        self.interior.config(width=self.winfo_width(),height=self.winfo_height())
    
    def table(self,nbRow,nbCol):
        self.table = list()
        for i in range(nbRow):
            for j in range(nbCol):
                cell=tk.Entry(self.interior)
                cell.insert(0, 0) 
            cell.grid(row = i, column = j) 
            self.table.append(cell)



        
