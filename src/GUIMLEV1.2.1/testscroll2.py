from tkinter import *
 
root = Tk()
vsb = Scrollbar(root, orient="vertical")
vsb.grid(row=0, column=1, sticky="ns")
c = Canvas(root,yscrollcommand=vsb.set)
c.grid(row=0, column=0, sticky="news")
vsb.config(command=c.yview)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
"""
fr = Frame(c)
#On ajoute des widgets :
for i in range(0,26):
    row=int(i/8)
    col=i%8
    Button(fr, width=10,height=2,text="%s" %(chr(i+65))).grid(row=row, column=col)
# c.create_window(0, 0,  window=fr)
fr.update_idletasks()
c.config(scrollregion=c.bbox("all"))
"""
root.mainloop()
