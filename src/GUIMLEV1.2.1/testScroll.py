from tkinter import *
 
class ScrollableCanvas(Frame):
     def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
         
        canvas=Canvas(self,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
  
        vbar=Scrollbar(self,orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)
         
        canvas.config(width=200,height=200)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)
         
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW )
 
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)
 
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
 
 
 
class Main_frame(Frame):
    # Init
    def __init__(self, fenetre_principale=None):
        Frame.__init__(self, fenetre_principale)
        self.grid()
        self.scrollable_canvas = ScrollableCanvas(self)
        self.scrollable_canvas.grid(row=1,column=1)
         
        colours = ['red','green','orange','white','yellow','blue','green','orange','white','yellow','blue','green','orange','white','yellow','blue','green','orange','white','yellow','blue']
        test = ['0','0','1','0','0','1','1','0','1','0','0','1','1','0','1','1','0','1','1','0','1']
          
        r = 0
        for a in colours:
            Label(self.scrollable_canvas.interior, text=a, relief=RIDGE,width=15,bg='white').grid(row=r,column=0)
            r = r + 1
             
        r = 0
        for b in test:
            Label(self.scrollable_canvas.interior, text=b, relief=RIDGE,width=10,bg='white').grid(row=r,column=1)
            r = r + 1
  
  
if __name__ == "__main__":
    root = Tk()
    root.title("tk")
    interface = Main_frame(fenetre_principale=root)
    interface.mainloop()