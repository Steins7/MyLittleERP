import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Mle

class UtilBar(tk.Frame):
    def __init__(self,container):
        tk.Frame.__init__(self,container,name="utilBar")
        self.rowconfigure(2,weight=2)
        self.grid(row=2, column=1,columnspan=2,sticky="nsew")


mle = Mle()
utilBar = UtilBar(mle)

print(utilBar.winfo_name())