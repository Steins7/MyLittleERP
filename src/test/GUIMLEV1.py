import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

MLE = tk.Tk()
MLE.wm_title("    GUI MLE V1    ")
MLE.columnconfigure(0,weight=1)
MLE.columnconfigure(1,weight=2)
MLE.rowconfigure(0,weight=0)
MLE.rowconfigure(1,weight=1)

utilBar = tk.Frame(MLE,name="utilBar")
utilBar.columnconfigure(0,weight=1)
utilBar.columnconfigure(1,weight=1)
utilBar.columnconfigure(2,weight=1)
utilBar.columnconfigure(3,weight=1)
utilBar.columnconfigure(4,weight=1)
utilBar.columnconfigure(5,weight=1)
utilBar.columnconfigure(6,weight=1)
utilBar.columnconfigure(7,weight=1)
utilBar.columnconfigure(8,weight=1)
utilBar.columnconfigure(9,weight=1)

utilBar.grid(row=0,column=0,columnspan=2,sticky="nsew")
b1 = tk.Button(utilBar, text="HW!",fg="black",bg="white",command=lambda:B2())
b1.grid(column=0,row=0)

navigationBar = tk.Label(MLE)
navigationBar.columnconfigure(0,weight=0)
navigationBar.columnconfigure(1,weight=1)
navigationBar.rowconfigure(0,weight=1)
navigationBar.rowconfigure(1,weight=1)
navigationBar.rowconfigure(2,weight=1)
navigationBar.rowconfigure(3,weight=1)
navigationBar.rowconfigure(4,weight=1)
navigationBar.rowconfigure(5,weight=1)
navigationBar.rowconfigure(6,weight=1)
navigationBar.rowconfigure(7,weight=1)
navigationBar.rowconfigure(8,weight=1)
navigationBar.rowconfigure(9,weight=1)

navigationBar.grid(row=1,column=0,sticky="nsew")

displayWindow = tk.Canvas(MLE)

displayWindow.grid(row=1,column=1)

def B2():
    b2=tk.Button(utilBar,text="it works !",fg="black",bg="white",command=lambda:B1())
    b2.grid(column=1,row=0,sticky="nsew")
def B1():
    b1=tk.Button(utilBar,text="change",fg="black",bg="white",command=lambda:B2())
    b1.grid(column=0,row=0,sticky="nsew")


print(MLE.winfo_children()[0].winfo_name())

MLE.mainloop()