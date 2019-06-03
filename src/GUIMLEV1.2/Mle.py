import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

MLE = tk.Tk()
MLE.wm_title("    GUI MLE V1    ")
MLE.columnconfigure(0,weight=1)
MLE.columnconfigure(1,weight=2)
MLE.rowconfigure(0,weight=0)
MLE.rowconfigure(1,weight=1)